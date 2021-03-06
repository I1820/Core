# In The Name Of God
# ========================================
# [] File Name : cooler.py
#
# [] Creation Date : 02-10-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
from ..actuator import ActuatorThing
from ..fields import Setting


class Cooler(ActuatorThing):
    """
    This class represents Cooler actuator
    """

    name = "cooler"

    on = Setting()
    temperature = Setting(type='integer')
