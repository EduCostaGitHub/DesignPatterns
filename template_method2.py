"""
Template Method (comportamental) tema intenção de definir 
um algoritmo em um método, postergando alguns passos para as 
subclasses por herança. Template method permite
que subclasses redefinam certos passos de um algorithmo
sem mudar a estrutura do mesmo.

Também é possível definir hooks para que as subclasses
utilizem caso necessário

The Hollywood principle: "Don't Call Us, We'll CAll You"
(IoC - Inversão de Controlo)

"""
from __future__ import annotations
from monostate_2 import StringReprMixin
from typing import List, Dict, Tuple
from abc import ABC, abstractmethod

class Pizza(ABC):
    """ Abstract class"""
    def prepare(self):
        """template methdo"""
        self.hook_after_cook()
        self.add_ingredients() #abstract
        self.cook() #abstract
        self.cut() #concrete
        self.serve() #concrete
        print()
    
    def hook_after_cook(self):pass

    @abstractmethod
    def add_ingredients(self): pass

    @abstractmethod
    def cook(self): pass        

    def cut(self):
        print(f'{self.__class__.__name__} cuting ')

    def serve(self): 
        print(f'{self.__class__.__name__} serving ')

        

class Carbonara(Pizza):
    def add_ingredients(self):
        print(f'{self.__class__.__name__} adding, cheese, ham, carbonara ')

    def cook(self):
        print(f'{self.__class__.__name__} cooking for 15m')

class Napolitana(Pizza):
    def add_ingredients(self):
        print(f'{self.__class__.__name__} adding, cheese, mushsroom, bacon ')

    def cook(self):
        print(f'{self.__class__.__name__} cooking for 10m')

    def cut(self):
        print(f'{self.__class__.__name__} cut in 4 parts')

class Mediterranea(Pizza):
    def add_ingredients(self):
        print(f'{self.__class__.__name__} adding, cheese, olives, chicken ')

    def cook(self):
        print(f'{self.__class__.__name__} cooking for 20m')

    def cut(self):
        print(f'{self.__class__.__name__} cut in 8 parts')

    def serve(self):
        print(f'{self.__class__.__name__} serving very hot!')

    def hook_after_cook(self):
        print(f'{self.__class__.__name__} serving some wine')



if __name__== "__main__":
    carbonara = Carbonara().prepare()
    napolitana = Napolitana().prepare()
    mediterranea = Mediterranea().prepare()
    