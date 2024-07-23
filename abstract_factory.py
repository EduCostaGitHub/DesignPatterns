"""
Abstract Factory é um padrão de criação que fornece um interface para criar 
famílias de objetos relacionados ou dependentes sem especificar suas classes
concretas. Geralmente Abstract Factory conta com um ou mais Factory Methods
para criar seus objetctos

Uma diferença importante entre Factory Method e Abstract Factory é que o 
Factory Method usa herança, enquanto Abstract Factory usa a composição

Princípio: Programe para insterfaces. não para implementações
"""

from abc import ABC, abstractmethod

class LuxuryVehicle(ABC):
    @abstractmethod
    def pick_client(self) -> None:pass

class UtilityVehicle(ABC):
    @abstractmethod
    def pick_client(self) -> None:pass
    
class LuxuryCar_NZ(LuxuryVehicle):
    def pick_client(self) -> None:
        print('Luxury NZ Car is picking client')

class UtilityCar_NZ(UtilityVehicle):
    def pick_client(self) -> None:
        print('Utility NZ Car is picking client')

class LuxuryMotocyle_NZ(LuxuryVehicle):
    def pick_client(self) -> None:
        print('Luxury NZ Motocycle is picking client')

class UtilityMotocyle_NZ(UtilityVehicle):
    def pick_client(self) -> None:
        print('Utility NZ Motocycle is picking client')

class LuxuryCar_SZ(LuxuryVehicle):
    def pick_client(self) -> None:
        print('Luxury SZ Car is picking client')

class UtilityCar_SZ(UtilityVehicle):
    def pick_client(self) -> None:
        print('Utility SZ Car is picking client')

class LuxuryMotocyle_SZ(LuxuryVehicle):
    def pick_client(self) -> None:
        print('Luxury SZ Motocycle is picking client')

class UtilityMotocyle_SZ(UtilityVehicle):
    def pick_client(self) -> None:
        print('Utility SZ Motocycle is picking client')


#Simple Factory
class VehicleFactory(ABC):   
    
    @staticmethod
    @abstractmethod
    def get_Luxury_vehicle( car_type: str) -> LuxuryVehicle: pass

    @staticmethod
    @abstractmethod
    def get_Utility_vehicle( car_type: str) -> UtilityVehicle: pass


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

    
