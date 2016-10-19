# In The Name Of God
# ========================================
# [] File Name : types.py
#
# [] Creation Date : 19-10-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
from ..controller.log import LogController
from ..exceptions.thing import ThingInvalidAccessException


class Event:
    def __init__(self, name):
        self.name = name
        self.time = None

    def __get__(self, obj, objtype):
        time = self.time
        return time.strftime("%Y-%m-%dT%H:%M:%SZ")

    def __set__(self, obj, value):
        if isinstance(value, dict):
            self.time = value['time']


class State:
    def __init__(self, name):
        self.name = name

    def __get__(self, obj, objtype):
        value = LogController().last(
            obj.name, obj.rpi_id, obj.device_id)
        return value

    def __set__(self, obj, value):
        if isinstance(value, dict):
            LogController().save(self.name, obj.name, obj.rpi_id,
                                 obj.device_id,
                                 value['time'], value['value'])
            return
        else:
            raise ThingInvalidAccessException(obj.name, self.name)


class Setting:
    def __init__(self, name):
        pass

    def __get__(self, obj, objtype):
        pass

    def __set__(self, obj, value):
        pass
