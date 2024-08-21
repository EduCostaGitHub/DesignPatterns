"""
Composite é um padrão de projecto estrutural que permite que
voçê utilize a composição para criar objectos em estruturas
de árvores. O Padrão permite aos clientes tratarem de maneira 
uniforme objectos individuais (LEAF) e composições de 
objectos (Composite)

IMPORTANTE: Só aplique este padrão em uma estrutura que possa
ser representada em formato hierárquico (árvore).

No padrão composite, temos dois tipos de objectos:
Composite (que representa nós internos da árvore) e Leaf
(que representa nós externos da árvore)

Objectos Composite são objectos mais comlpexos e com filhos.
Gerlamente, eles delegam trabalho para os filhos usando
um método em comum,

Objectos LEAF são objectos simples, da ponta e sem filhos.
Gerlamente, são esses objectos que realizam o trabalho
real da aplicação.

"""

from __future__ import annotations
from abc import ABC, abstractmethod
from pickle import LIST
from typing import List, Dict


class BoxStruture(ABC):
    """ Component"""
    @abstractmethod
    def print_content(self) -> None: pass

    @abstractmethod
    def get_price(self) -> float: pass

    def add(self, child: BoxStruture) -> None: pass
    def remove(self, child: BoxStruture) -> None: pass


class Box(BoxStruture):
    """ Composite"""

    def __init__(self, name: str) -> None:
        self.name: str = name
        self._children: List[BoxStruture] = []

    def print_content(self) -> None:
        print(f'\n{self.name}:')
        for child in self._children:
            child.print_content()

    def get_price(self) -> float:

        return sum([
            child.get_price() for child in self._children
        ])

    def add(self, child: BoxStruture) -> None:
        self._children.append(child)

    def remove(self, child: BoxStruture) -> None:
        if child in self._children:
            self.remove(child)


class Product(BoxStruture):
    """Leaf"""

    def __init__(self, name: str, price: float) -> None:
        self.name: str = name
        self.price: float = price

    def print_content(self) -> None:
        print(f'{self.name} {self.price}')

    def get_price(self) -> float:
        return self.price


if __name__ == "__main__":
    shirt1 = Product('shirt1', 9.90)
    shirt2 = Product('shirt2', 20.40)
    shirt3 = Product('shirt3', 32.90)

    cx_shirts = Box('Caixa de Shirts')
    cx_shirts.add(shirt1)
    cx_shirts.add(shirt2)
    cx_shirts.add(shirt3)

    cx_shirts.print_content()
    print(cx_shirts.get_price())

    print()

    phone1 = Product('phone1', 229.90)
    phone2 = Product('phone2', 10220.40)
    phone3 = Product('phone3', 532.90)

    cx_phones = Box('Caixa de Phones')
    cx_phones.add(phone1)
    cx_phones.add(phone2)
    cx_phones.add(phone3)

    cx_products = Box('Products')
    cx_products.add(cx_shirts)
    cx_products.add(cx_phones)

    cx_products.print_content()
    print(cx_products.get_price())
