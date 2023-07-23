from .capulet import CapuletEngine
from .sternman import SternmanEngine
from .willoughby import WilloughbyEngine


class Engine(CapuletEngine, SternmanEngine, WilloughbyEngine):
    def __init__(self, engine_type, current_mileage, last_service_mileage, warning_light_is_on):
        self.engine_type = engine_type
        if engine_type == 'capulet':
            CapuletEngine.__init__(
                self, current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        elif engine_type == 'sternman':
            SternmanEngine.__init__(
                self, warning_light_is_on=warning_light_is_on)
        elif engine_type == 'willoughby':
            WilloughbyEngine.__init__(self, current_mileage=current_mileage,
                                      last_service_mileage=last_service_mileage)

    def engine_should_be_serviced(self):
        if self.engine_type == 'capulet':
            return CapuletEngine.engine_should_be_serviced(self)
        elif self.engine_type == 'sternman':
            return SternmanEngine.engine_should_be_serviced(self)
        elif self.engine_type == 'willoughby':
            return WilloughbyEngine.engine_should_be_serviced(self)


# some_engine = Engine(engine_type='sternman',
#                      current_mileage=100000, last_service_mileage=30000, warning_light_is_on=0)
# print(some_engine.engine_should_be_serviced())
