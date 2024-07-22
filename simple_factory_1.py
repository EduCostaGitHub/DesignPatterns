"""
Na programação POO, o termo factory (fábrica) refere-se a um classe ou método
que é responsável por criar objectos.

Vantagens:
    Permitem criar um sistema com baixo acoplamento entre clases porque 
    ocultam as classes que criam os objetos do código cliente.

    Facilitam a adição de novas classes ao código, porque o cliente não
    conhece e nem utiliza a implementação da classe (utiliza a factory)

    Podem facilitar o processo de 'cache' ou criação de 'Singletons' porque a
    fábrica pode retornar um objeto já criado para o cliente, ai invés de criar
    novos objetos smepre que o cliente precisar.

Desvantagens:
    Podem introduzir muitas classes no código

Vamos ver 2 tipos de Factory da GoF: Factory method e Abstract Factory

Nesta Aula:
Simple Factory -> Uma espécie de Factory Method parametrizado
Simple Factory pode não ser considerado um padrão de projeto por si só
Simple Factory pode quebrar princípios do SOLID

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

class Motocyle(Vehicle):
    def pick_client(self) -> None:
        print('Motocycle is picking client')


#Simple Factory
class VehicleFactory:
    @staticmethod
    def get_vehicle( car_type: str) -> Vehicle:
        if car_type == 'luxury':
            return LuxuryCar()
        if car_type == 'utility':
            return UtilityCar()
        if car_type == 'motocycle':
            return Motocyle()
        assert 0, 'Vehicle doesn exist'
        
# Code Test
if __name__ == "__main__":
    from random import choice
    available_cars = ['luxury','utility','motocycle']
    for i in range(10):
        car = VehicleFactory.get_vehicle(choice(available_cars))
        car.pick_client()

