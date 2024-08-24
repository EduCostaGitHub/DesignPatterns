"""
Decorator é um padrão de projecto estrutural que permite que você
adicione novos comportamentos em objectos ao cooca-los dentro de 
um 'wrapper' (decorator) de objectos.

Decoradores fornecem uma alternativa flexível ao uso de subclasses
para a extensão de funcionalidades.

Decorator (padrão de projecto) != Decorator em Python

Python decorator -> Um decorator é um callable que aceita outra 
função como argumento (a função decorada ). O decorator pode
realizar algum processameto com a função decorada e devolvê-la
ou substituí-la por outra função ou objecto invocável.
Do livro 'Python Fluente', por Luciano Ramalho (pág. 223)
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
from dataclasses import dataclass
from copy import deepcopy


"""Ingredients """


@dataclass
class Ingredient:
    price: float


@dataclass
class Bread(Ingredient):
    price: float = 1.5


@dataclass
class Sausage(Ingredient):
    price: float = 4.99


@dataclass
class Bacon(Ingredient):
    price: float = 7.99


@dataclass
class Egg(Ingredient):
    price: float = 1.5


@dataclass
class Cheese(Ingredient):
    price: float = 6.35


@dataclass
class MashedPotatoes(Ingredient):
    price: float = 2.25


@dataclass
class PotatoSticks(Ingredient):
    price: float = 0.99


""" Hot Dogs """


class Hotdog:
    _name: str
    _ingredients: List[Ingredient]

    @property
    def price(self) -> float:
        return round(sum([
            item.price for item in self._ingredients
        ]), 2)

    @property
    def name(self) -> str:
        return self._name

    @property
    def ingredients(self) -> List[Ingredient]:
        return self._ingredients

    def __repr__(self) -> str:
        return f'{self.name}:({self.price}) -> {self.ingredients}'


class SimpleHotdog(Hotdog):
    def __init__(self) -> None:
        self._name = 'SimpleHotdog'
        self._ingredients = [
            Bread(),
            Sausage(),
            PotatoSticks(),
        ]


class SpecialHotdog(Hotdog):
    def __init__(self) -> None:
        self._name = 'SpecialHotdog'
        self._ingredients = [
            Bread(),
            Sausage(),
            Bacon(),
            Egg(),
            Cheese(),
            MashedPotatoes(),
            PotatoSticks(),
        ]


"""Decorators"""


class HotdogDecorator(Hotdog):
    def __init__(self, hotdog: Hotdog, ingredient: Ingredient) -> None:
        self.hotdog: Hotdog = hotdog
        self._ingredient: Ingredient = ingredient

        self._ingredients = deepcopy(self.hotdog.ingredients)
        self._ingredients.append(self._ingredient)

    @property
    def name(self) -> str:
        return f'{self.hotdog.name} + {self._ingredient.__class__.__name__}'


if __name__ == "__main__":
    simple_hotdog = SimpleHotdog()

    print(simple_hotdog)

    bacon_simple_hotdog = HotdogDecorator(simple_hotdog, Bacon())

    print(bacon_simple_hotdog)

    egg_bacon_simple_hotdog = HotdogDecorator(bacon_simple_hotdog, Egg())

    print(egg_bacon_simple_hotdog)
