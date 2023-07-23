from .nubbin import NubbinBattery
from .spindler import SpindlerBattery


class Battery(NubbinBattery, SpindlerBattery):
    def __init__(self, last_service_date, battery_type):
        self.battery_type = battery_type
        if battery_type == 'nubbin':
            NubbinBattery.__init__(self, last_service_date=last_service_date)
        elif battery_type == 'spindler':
            SpindlerBattery.__init__(self, last_service_date=last_service_date)

    def battery_should_be_serviced(self):
        if self.battery_type == 'nubbin':
            return NubbinBattery.battery_should_be_serviced(self)
        elif self.battery_type == 'spindler':
            return SpindlerBattery.battery_should_be_serviced(self)


# some_random_bat = Battery(
#     last_service_date='2021-12-21', battery_type='spindler')
# print(some_random_bat.battery_should_be_serviced())
