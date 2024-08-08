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

class Abstract(ABC):
    def template_method(self):
        self.hook()
        self.operation1()
        self.base_class_method()
        self.operation2()

    def hook(self): pass
    
    def base_class_method(self):
        print('Method from Abstract Class')

    @abstractmethod
    def operation1(self):
        pass

    @abstractmethod
    def operation2(self):
        pass

class ConcreteClass(Abstract):
    def operation1(self):
        print('Operação 1')

    
    def operation2(self):
        print('Operação 2')
        

class ConcreteClass2(Abstract):
    def operation1(self):
        print('Another Operação 1')

    def hook(self):
        print(f'I\'m {self.__class__.__name__} and i\'m using hook')

    
    def operation2(self):
        print('Another Operação 2')
        



if __name__== "__main__":
    concrete = ConcreteClass()
    concrete2 = ConcreteClass2()
    concrete.template_method()
    concrete2.template_method()