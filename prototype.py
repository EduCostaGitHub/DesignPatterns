"""
Especificar os tipos de objetos a serem criados
usando uma instância-protótipo e criar novos objetos
pela cópia desse protótipo
----

Quais objetos são copiados com o sinal de atribuição ??
    São os Imutávies !!

Mutáveis(passado por referêcia)
list
set
dict
class ( user can change it)

Imutáveis
bool
int
float
tuple
str

"""
from __future__ import annotations
from copy import deepcopy
from monostate_2 import StringReprMixin
from typing import List


class Address(StringReprMixin):
    def __init__(self, street: str, number: str) -> None:
        self.street = street
        self.number = number

class Person(StringReprMixin):
    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.addresses: List[Address] = []

    def add_address(self,address:Address) -> None:
        self.addresses.append(address)

    def clone(self) -> Person:
        return deepcopy(self)



    
if __name__== "__main__":
    #teste de cópia de valores imutáveis
    name1 = 'Edu '
    name2 = name1
    name1='Zequinha'
    print(name1)
    print(name2)
    # valores mutáveis
    list1 = [1,2,3]
    list2 = list1
    list1[0] = 4
    print(list1)
    print(list2)
    ##
    
    edu = Person('Eduardo','Costa')
    edu_address = Address('Av. Artur Semedo','10')
    edu.add_address(edu_address)
    print(edu)

    rute = edu.clone()
    rute.firstname = 'Rute'
    print(rute)