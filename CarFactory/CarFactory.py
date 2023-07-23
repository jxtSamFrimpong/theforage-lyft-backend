from Car.Car import Car


class CarFactory:
    def __init__(self):
        pass

    def calliope(self, last_service_date, current_mileage, last_service_mileage):
        self.car = Car(engine='capulet', battery='spindler', last_service_date=last_service_date,
                       current_mileage=current_mileage, last_service_mileage=last_service_mileage)

    def glissade(self, last_service_date, current_mileage, last_service_mileage):
        self.car = Car(engine='willoughby', battery='spindler', last_service_date=last_service_date,
                       current_mileage=current_mileage, last_service_mileage=last_service_mileage)

    def palindrome(self, last_service_date, warning_light_is_on):
        self.car = Car(engine='sternman', battery='spindler',
                       last_service_date=last_service_date, warning_light_is_on=warning_light_is_on)

    def rorschach(self, last_service_date, current_mileage, last_service_mileage):
        self.car = Car(engine='willoughby', battery='nubbin', last_service_date=last_service_date,
                       current_mileage=current_mileage, last_service_mileage=last_service_mileage)

    def thovex(self, last_service_date, current_mileage, last_service_mileage):
        self.car = Car(engine='capulet', battery='nubbin', last_service_date=last_service_date,
                       current_mileage=current_mileage, last_service_mileage=last_service_mileage)
