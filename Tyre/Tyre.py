from abc import ABC, abstractmethod
import random

class Tyre(ABC):
    def __init__(self):
        self.sensors = [random.uniform(0,1) for i in range(4)]
    
    @abstractmethod
    def tyres_should_be_serviced(self):
        pass