# In The Name Of God
# ========================================
# [] File Name : sensor.py
#
# [] Creation Date : 07-09-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
from .base import Thing


class SensorThing(Thing):
    def __init__(self, agent_id, device_id):
        super().__init__(agent_id, device_id)
