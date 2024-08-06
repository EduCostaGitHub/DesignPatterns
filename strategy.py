"""
Strategy é um padrão de projecto comportamental que tem 
a intenção de definir uma família de algoritmos,
encapsular cada uma delas e torná-las intercambiáveis.
Strategy permite que o algoritmo varie independentemente
dos clientes que o utilizam.

Princípio: Aberto/Fechado (open/close principle)
Entidades devem ser abertas para extensão, mas fechadas para modificação

"""
from __future__ import annotations
from monostate_2 import StringReprMixin
from abc import ABC, abstractmethod

class Order:
    def __init__(self, total:float, discount: DiscountStrategy) -> None:
        self._total = total
        self._discount = discount

    @property
    def total(self):
        return self._total
    
    @property
    def total_with_discount(self):
        return self._discount.calculate(self._total)

class DiscountStrategy(ABC):
    @abstractmethod
    def calculate(self, value:float) -> float: raise NotImplementedError()

class TwentyPercent(DiscountStrategy):
    def calculate(self, value:float) -> float:
        return value * 0.8


class Fiftyercent(DiscountStrategy):
    def calculate(self, value:float) -> float:
        return value * 0.5
    
class NoDiscount(DiscountStrategy):
    def calculate(self, value:float) -> float:
        return value

class CustomDiscount(DiscountStrategy):
    def __init__(self, discount) -> None:
        self.discount = discount / 100
    def calculate(self, value:float) -> float:
        return value * (1 - self.discount)


if __name__== "__main__":
    order = Order(1000,TwentyPercent())
    order2= Order(350,Fiftyercent())
    order3= Order(500,NoDiscount())
    order4= Order(300,CustomDiscount(30))

    print(order.total)
    print(order.total_with_discount)
    print()
    print(order2.total)
    print(order2.total_with_discount)
    print()
    print(order3.total)
    print(order3.total_with_discount)
    print()
    print(order4.total)
    print(order4.total_with_discount)