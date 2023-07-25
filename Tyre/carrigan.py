from Tyre.Tyre import Tyre

class Carrigan(Tyre):
    def __init__(self):
        super().__init__()
    def tyres_should_be_serviced(self):
        return len([i for i in self.sensors if i > 0.9]) >= 0


# some_tyre = Carrigan()
# print(some_tyre.sensors)
# print(some_tyre.tyres_should_be_serviced())