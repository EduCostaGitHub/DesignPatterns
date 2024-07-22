"""
Factory method é um padrão de criação que permite definir uma interface para
criar objectos, mas deixa as subclasses decidirem quais objetos criar. O
Factory method permite adiar a instanciação para as subclasses, garantindo o 
baixo acoplamento entre classes.

"""
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def pick_client(self) -> None:pass
    
class LuxuryCar(Vehicle):
    def pick_client(self) -> None:
        print('Luxury Car is picking client')

class UtilityCar(Vehicle):
    def pick_client(self) -> None:
        print('Utility Car is picking client')

class LuxuryMotocyle(Vehicle):
    def pick_client(self) -> None:
        print('Luxury Motocycle is picking client')

class UtilityMotocyle(Vehicle):
    def pick_client(self) -> None:
        print('Utility Motocycle is picking client')


#Simple Factory
class VehicleFactory(ABC):
    def __init__(self, car:str) -> None:
        self.car = self.get_vehicle(car)
    
    @staticmethod
    @abstractmethod
    def get_vehicle( car_type: str) -> Vehicle: pass

    def pick_client(self):
        self.car.pick_client()

#Factory Method
class NorthVehicleFactory(VehicleFactory):
    @staticmethod
    def get_vehicle( car_type: str) -> Vehicle:
        if car_type == 'luxury':
            return LuxuryCar()
        if car_type == 'utility':
            return UtilityCar()
        if car_type == 'motocycle':
            return UtilityMotocyle()
        if car_type == 'luxurymotocycle':
            return LuxuryMotocyle()
        assert 0, 'Vehicle doesn exist'

class SouthVehicleFactory(VehicleFactory):
    @staticmethod
    def get_vehicle( car_type: str) -> Vehicle:        
        if car_type == 'utility':
            return UtilityCar()
        if car_type == 'motocycle':
            return UtilityMotocyle()        
        assert 0, 'Vehicle doesn exist'

        
# Code Test
if __name__ == "__main__":
    from random import choice
    available_cars_north = ['luxury','utility','motocycle','luxurymotocycle']
    available_cars_south = ['utility','motocycle']
    
    print('North Zone')
    for i in range(10):
        car = NorthVehicleFactory(choice(available_cars_north))
        car.pick_client()
    print()

    print('South Zone')
    for i in range(10):
        car_2 = SouthVehicleFactory(choice(available_cars_south))
        car_2.pick_client()

    

