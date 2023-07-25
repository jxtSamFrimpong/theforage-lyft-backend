from datetime import datetime, timedelta


class SpindlerBattery:
    def __init__(self, last_service_date):
        self.last_service_date = datetime.strptime(
            last_service_date, "%Y-%m-%d")
        self.current_date = datetime.now()

    def battery_should_be_serviced(self):
        date_difference = self.current_date - self.last_service_date
        three_years = timedelta(days=365 * 3)
        if date_difference >= three_years:
            return True
        else:
            return False
