from Engine.Engine import Engine
from Battery.Battery import Battery


class Car(Engine, Battery):
    def __init__(self, engine, battery, last_service_date, current_mileage=0, last_service_mileage=0, warning_light_is_on=False):
        Engine.__init__(self, engine_type=engine, current_mileage=current_mileage,
                        last_service_mileage=last_service_mileage, warning_light_is_on=warning_light_is_on)
        Battery.__init__(self, battery_type=battery,
                         last_service_date=last_service_date)

    def needs_service(self):
        return self.engine_should_be_serviced() or self.battery_should_be_serviced()


# some_car = Car(engine='capulet', battery='nubbin', last_service_date='2022-12-21',
#                current_mileage=50000, last_service_mileage=30000, warning_light_is_on=False)
# some_car.needs_service()
