from Engine.Engine import Engine
from Battery.Battery import Battery
from Tyre.carrigan import Carrigan
from Tyre.octoprime import Octoprime


class Car(Engine, Battery, Carrigan, Octoprime):
    def __init__(self, engine, battery, last_service_date, current_mileage=0, last_service_mileage=0, warning_light_is_on=False, tyre_type='octoprime'):
        Engine.__init__(self, engine_type=engine, current_mileage=current_mileage,
                        last_service_mileage=last_service_mileage, warning_light_is_on=warning_light_is_on)
        Battery.__init__(self, battery_type=battery,
                         last_service_date=last_service_date)
        self.tyre_type = tyre_type
        if self.tyre_type == 'carrigan':
            Carrigan.__init__(self)
        elif self.tyre_type == 'octoprime':
            Octoprime.__init__(self)

    def needs_service(self):
        return self.engine_should_be_serviced() or self.battery_should_be_serviced() or self.tyres_should_be_serviced()

    def tyres_should_be_serviced(self):
        if self.tyre_type == 'carrigan':
            return Carrigan.tyres_should_be_serviced(self)
        elif self.tyre_type == 'octoprime':
            return Octoprime.tyres_should_be_serviced(self)

# some_car = Car(engine='capulet', battery='nubbin', last_service_date='2022-12-21',
#                current_mileage=50000, last_service_mileage=30000, warning_light_is_on=False)
# some_car.needs_service()
