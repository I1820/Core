# In The Name Of God
# ========================================
# [] File Name : discovery.py
#
# [] Creation Date : 22-02-2017
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
from ..things.base import Things
from ..domain.agent import I1820Agent

from datetime import datetime
from pelix.ipopo.decorators import ComponentFactory, Property, Provides, \
     Validate, Invalidate, Instantiate, Requires


@ComponentFactory("discovery_factory")
@Provides("discovery_service")
@Property("default")
@Requires("_rs", "redis_service")
@Instantiate("default_discovery_instance")
class DiscoveryService:
    def __init__(self):
        self._agents = {}
        self._rs = None

    @Validate
    def validate(self, context):
        """
        The component is validated. This method is called right before the
        provided service is registered to the framework.
        """
        # All setup should be done here
        print(" * 18.20 Service: Discovery Service")

    @Invalidate
    def invalidate(self, context):
        """
        The component has been invalidated. This method is called right after
        the provided service has been removed from the framework.
        """
        pass

    @property
    def agents(self):
        '''
        Retrieves I1820 agent information from redis.
        '''
        agents = self._rs.rconn.zrange('i1820:agent:time:',
                                       0, -1, withscores=True)
        result = {}
        for agent_id, agent_time in agents:
            result[agent_id] = {}
            result[agent_id]['time'] = datetime.fromtimestamp(agent_time)\
                .strftime('%Y-%m-%dT%H:%M:%SZ')
            result[agent_id]['things'] = []
            for t in self._rs.rconn.smembers('i1820:agent:%s' % agent_id):
                t_type, t_id = t.split(":", maxsplit=1)
                result[agent_id]['things'].append(
                    {'type': t_type, 'id': t_id})
        return result

    def ping(self, agent: I1820Agent):
        '''
        Agent pings I1820, this method saves it's status and things.
        '''
        self._rs.rconn.zadd('i1820:agent:time:', datetime.utcnow().timestamp(),
                            '%s' % agent.ident)
        for t in agent.things:
                # Add thing into local things storage
                Things.get(t['type']).new_thing(agent.ident, t['id'])
                self._rs.rconn.sadd('i1820:agent:%s' % agent.ident,
                                    '%s:%s' % (t['type'], t['id']))

    def pong(self, agent_id: str):
        '''
        Removes given agent (based on it's identification) from agent storage.
        '''
        result = self._rs.rconn.zrem('i1820:agent:time:', agent_id)
        for t in self._rs.rconn.smembers('i1820:agent:%s' % agent_id):
            t_type, t_id = t.split(":", maxsplit=1)
            Things.get(t_type).del_thing(agent_id, t_id)
        return result
