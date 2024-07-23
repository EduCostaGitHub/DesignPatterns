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
    def get_Luxury_car() -> LuxuryVehicle: pass

    @staticmethod
    @abstractmethod
    def get_Utility_car() -> UtilityVehicle: pass

    @staticmethod
    @abstractmethod
    def get_Luxury_moto() -> LuxuryVehicle: pass

    @staticmethod
    @abstractmethod
    def get_Utility_moto() -> UtilityVehicle: pass


#Factory Method
class NorthVehicleFactory(VehicleFactory):
    
    @staticmethod    
    def get_Luxury_car() -> LuxuryVehicle:
        return LuxuryCar_NZ()

    @staticmethod    
    def get_Utility_car() -> UtilityVehicle:
        return UtilityCar_NZ()

    @staticmethod
    def get_Luxury_moto() -> LuxuryVehicle:
        return LuxuryMotocyle_NZ()

    @staticmethod    
    def get_Utility_moto() -> UtilityVehicle:
        return UtilityMotocyle_NZ()

class SouthVehicleFactory(VehicleFactory):
    @staticmethod    
    def get_Luxury_car() -> LuxuryVehicle:
        return LuxuryCar_SZ()

    @staticmethod    
    def get_Utility_car() -> UtilityVehicle:
        return UtilityCar_SZ()

    @staticmethod
    def get_Luxury_moto() -> LuxuryVehicle:
        return LuxuryMotocyle_SZ()

    @staticmethod    
    def get_Utility_moto() -> UtilityVehicle:
        return UtilityMotocyle_SZ()

class Subsidiary():
    def get_clients(self):
        for factory in [NorthVehicleFactory(),SouthVehicleFactory()]:
            utility_car = factory.get_Utility_car()
            utility_car.pick_client()

            luxury_car = factory.get_Luxury_car()
            luxury_car.pick_client()

            utility_moto = factory.get_Utility_moto()
            utility_moto.pick_client()

            luxury_moto = factory.get_Luxury_moto()
            luxury_moto.pick_client()
# Code Test
if __name__ == "__main__":
   client = Subsidiary()
   client.get_clients()
    
