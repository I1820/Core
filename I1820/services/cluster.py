# In The Name Of God
# ========================================
# [] File Name : cluster.py
#
# [] Creation Date : 24-02-2017
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
from ..conf.config import cfg

from pelix.ipopo.decorators import ComponentFactory, Property, Provides, \
     Validate, Invalidate, Instantiate


@ComponentFactory("cluster_factory")
@Provides("cluster_service")
@Property("default")
@Instantiate("default_cluster_instance")
class ClusterService:
    def __init__(self):
        pass

    @Validate
    def validate(self, context):
        """
        The component is validated. This method is called right before the
        provided service is registered to the framework.
        """
        # All setup should be done here
        print(" * 18.20 Service: Cluster Service")

    @Invalidate
    def invalidate(self, context):
        """
        The component has been invalidated. This method is called right after
        the provided service has been removed from the framework.
        """
        print(" > 18.20 Service: Cluster Service")

    @property
    def tenant(self):
        result = {
            'id': cfg.tenant_id,
            'owner': cfg.tenant_owner
        }
        return result
