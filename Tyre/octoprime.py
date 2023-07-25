from Tyre.Tyre import Tyre

class Octoprime(Tyre):
    def __init__(self):
        super().__init__()
    def tyres_should_be_serviced(self):
        return sum(self.sensors) >= 3.0

# some_tyre = Octoprime()
# print(sum([0.931439042241758, 0.5769507343628022, 0.13411737198641527, 0.6048938295693922]))
# print(some_tyre.tyres_should_be_serviced())