import unittest
from datetime import datetime

from CarFactory.CarFactory import CarFactory


class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3).strftime(format='%Y-%m-%d')
        current_mileage = 0
        last_service_mileage = 0

        #car = Calliope(last_service_date, current_mileage, last_service_mileage)
        car = CarFactory()
        car.calliope(last_service_date=last_service_date,current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        self.assertTrue(car.car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1).strftime(format='%Y-%m-%d')
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory()
        car.calliope(last_service_date=last_service_date, current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        self.assertFalse(car.car.battery_should_be_serviced())
        tyre_service = sum(car.car.sensors)
        self.assertTrue(car.car.needs_service() if tyre_service >= 3.0 else not car.car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date().strftime(format='%Y-%m-%d')
        current_mileage = 30001
        last_service_mileage = 0

        car = CarFactory()
        car.calliope(last_service_date=last_service_date, current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        self.assertTrue(car.car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date().strftime(format='%Y-%m-%d')
        current_mileage = 30000
        last_service_mileage = 0

        car = CarFactory()
        car.calliope(last_service_date=last_service_date, current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        self.assertFalse(car.car.engine_should_be_serviced())
        tyre_service = sum(car.car.sensors)
        self.assertTrue(car.car.needs_service() if tyre_service >= 3.0 else not car.car.needs_service())


class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3).strftime(format='%Y-%m-%d')
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory()
        car.glissade(last_service_date=last_service_date, current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        self.assertTrue(car.car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1).strftime(format='%Y-%m-%d')
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory()
        car.glissade(last_service_date=last_service_date, current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        self.assertFalse(car.car.battery_should_be_serviced())
        tyre_service = sum(car.car.sensors)
        self.assertTrue(car.car.needs_service() if tyre_service >= 3.0 else not car.car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date().strftime(format='%Y-%m-%d')
        current_mileage = 60001
        last_service_mileage = 0

        car = CarFactory()
        car.glissade(last_service_date=last_service_date, current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        self.assertTrue(car.car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date().strftime(format='%Y-%m-%d')
        current_mileage = 60000
        last_service_mileage = 0

        car = CarFactory()
        car.glissade(last_service_date=last_service_date, current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        self.assertFalse(car.car.engine_should_be_serviced())
        tyre_service = sum(car.car.sensors)
        self.assertTrue(car.car.needs_service() if tyre_service >= 3.0 else not car.car.needs_service())


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5).strftime(format='%Y-%m-%d')
        warning_light_is_on = False

        car = CarFactory()
        car.palindrome(last_service_date=last_service_date, warning_light_is_on=warning_light_is_on)
        self.assertTrue(car.car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        #last_service_date = today.replace(year=today.year - 3).strftime(format='%Y-%m-%d')
        last_service_date = today.replace(year=today.year - 1).strftime(format='%Y-%m-%d')
        
        warning_light_is_on = False

        car = CarFactory()
        car.palindrome(last_service_date=last_service_date, warning_light_is_on=warning_light_is_on)
        self.assertFalse(car.car.battery_should_be_serviced())
        tyre_service = sum(car.car.sensors)
        self.assertTrue(car.car.needs_service() if tyre_service >= 3.0 else not car.car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date().strftime(format='%Y-%m-%d')
        warning_light_is_on = True

        car = CarFactory()
        car.palindrome(last_service_date=last_service_date, warning_light_is_on=warning_light_is_on)
        self.assertTrue(car.car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date().strftime(format='%Y-%m-%d')
        warning_light_is_on = False

        car = CarFactory()
        car.palindrome(last_service_date=last_service_date, warning_light_is_on=warning_light_is_on)
        self.assertFalse(car.car.engine_should_be_serviced())
        tyre_service = sum(car.car.sensors)
        self.assertTrue(car.car.needs_service() if tyre_service >= 3.0 else not car.car.needs_service())


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5).strftime(format='%Y-%m-%d')
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory()
        car.rorschach(last_service_date=last_service_date, current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        self.assertTrue(car.car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3).strftime(format='%Y-%m-%d')
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory()
        car.rorschach(last_service_date=last_service_date, current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        self.assertFalse(car.car.battery_should_be_serviced())
        tyre_service = sum(car.car.sensors)
        self.assertTrue(car.car.needs_service() if tyre_service >= 3.0 else not car.car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date().strftime(format='%Y-%m-%d')
        current_mileage = 60001
        last_service_mileage = 0

        car = CarFactory()
        car.rorschach(last_service_date=last_service_date, current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        self.assertTrue(car.car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date().strftime(format='%Y-%m-%d')
        current_mileage = 60000
        last_service_mileage = 0

        car = CarFactory()
        car.rorschach(last_service_date=last_service_date, current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        self.assertFalse(car.car.engine_should_be_serviced())
        tyre_service = sum(car.car.sensors)
        self.assertTrue(car.car.needs_service() if tyre_service >= 3.0 else not car.car.needs_service())


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5).strftime(format='%Y-%m-%d')
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory()
        car.thovex(last_service_date=last_service_date,current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        self.assertTrue(car.car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3).strftime(format='%Y-%m-%d')
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory()
        car.thovex(last_service_date=last_service_date, current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        self.assertFalse(car.car.battery_should_be_serviced())
        tyre_service = sum(car.car.sensors)
        self.assertTrue(car.car.needs_service() if tyre_service >= 3.0 else not car.car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date().strftime(format='%Y-%m-%d')
        current_mileage = 30001
        last_service_mileage = 0

        car = CarFactory()
        car.thovex(last_service_date=last_service_date, current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        self.assertTrue(car.car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date().strftime(format='%Y-%m-%d')
        current_mileage = 30000
        last_service_mileage = 0

        car = CarFactory()
        car.thovex(last_service_date=last_service_date, current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        self.assertFalse(car.car.engine_should_be_serviced())
        tyre_service = sum(car.car.sensors)
        self.assertTrue(car.car.needs_service() if tyre_service >= 3.0 else not car.car.needs_service())


if __name__ == '__main__':
    unittest.main()
