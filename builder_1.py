"""
Builder é um padrão de criação que tem a intenção 
de separar a construção de um objeto complexo
da sua representação, de modo que o mesmo processo
de construção possa criar diferentes representações.

Builder dá a possibilidade de criar objetos passo-a-passo
e isso já é possível no Python sem este padrão.

Geralmente o Builder aceita o encadeamento de métodos
(method chaining)
"""

from abc import ABC, abstractmethod
from monostate_2 import StringReprMixin


class User(StringReprMixin):
    def __init__(self) -> None:
        self.firstname = None
        self.surname = None
        self.age = None
        self.phone_numbers : list = []
        self.addresses :list = []

class IUserBuilder(ABC):
    @property
    @abstractmethod
    def result(self): raise NotImplementedError()

    @abstractmethod
    def add_firstname(self, firstname): raise NotImplementedError()

    @abstractmethod
    def add_surname(self, surname): raise NotImplementedError()

    @abstractmethod
    def add_age(self, age): raise NotImplementedError()

    @abstractmethod
    def add_phone_numbers(self, phone_numbers): raise NotImplementedError()

    @abstractmethod
    def add_adresses(self, adresses): raise NotImplementedError()


class UserBuilder(IUserBuilder):
    def __init__(self) -> None:
        self.reset()

    def reset(self):
        self._result = User()

    @property    
    def result(self):
        return_data = self._result
        self.reset()
        return return_data
    
    def add_firstname(self, firstname):
        self._result.firstname = firstname
        return self
    
    def add_surname(self, surname):
        self._result.surname = surname
        return self
    
    def add_age(self, age):
        self._result.age = age
        return self
    
    def add_phone_numbers(self, phone_numbers):
        self._result.phone_numbers.append(phone_numbers)
        return self
    
    def add_adresses(self, adresses):
        self._result.addresses.append(adresses)
        return self

class UserDirector:
    def __init__(self, builder) -> None:
        self._builder : UserBuilder = builder

    def with_age(self, firstname, surname, age):
        self._builder.add_firstname(firstname)\
            .add_surname(surname)\
            .add_age(age)
        return self._builder.result
    
    def with_address(self, firstname, surname, address):
        self._builder.add_firstname(firstname)\
            .add_surname(surname)\
            .add_adresses(address)        
        return self._builder.result
    
if __name__== "__main__":
    user_builder = UserBuilder()
    user_director = UserDirector(user_builder)
    user1 = user_director.with_age('Edu','Costa', 47)
    user2 = user_director.with_address('Ezequiel','Canário', 'Rua do Alecrim')
    print(user1)
    print(user2)