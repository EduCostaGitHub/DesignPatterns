"""
Mediator é um padrão de projecto comportamental
que tem a intenção de definir um objecto que 
encapsula a forma como um conjunto de objectos
interage. O Mediator promove o baixo acoplamento
ao evitar que os objectos se refiram uns aos 
outros explicitamente e permite variar as interações 
independentes.
"""

from __future__ import annotations
from monostate_2 import StringReprMixin
from typing import List, Dict, Tuple,Any
from abc import ABC, abstractmethod
from collections.abc import Iterator, Iterable

class Colleague(ABC):
    def __init__(self) -> None:
        self.name:str

    @abstractmethod
    def broadcast(self, msg: str) -> None: pass

    @abstractmethod
    def direct(self,msg: str) -> None: pass

class Person(Colleague):
    def __init__(self, name:str, mediator: Mediator) -> None:
        self.name = name 
        self.mediator = mediator
    
    def broadcast(self, msg: str) -> None: 
        self.mediator.broadcast(self,msg)

    def send_direct(self, receiver: str, msg:str) -> None:
        self.mediator.direct(self, receiver, msg)
    
    def direct(self,msg: str) -> None:
        print(msg)   


class Mediator(ABC):
    @abstractmethod
    def broadcast(self, colleague:Colleague, msg:str) -> None:
        pass

    @abstractmethod
    def direct(self, sender:Colleague, receiver:str, msg:str) -> None:
        pass

class Chatroom(Mediator):
    def __init__(self) -> None:
        self.colleagues: List[Colleague] =[]

    def is_colleague(self, colleague: Colleague) -> bool:
        return colleague in self.colleagues
    
    def add(self, colleague: Colleague) -> None:
        if not self.is_colleague(colleague):
            self.colleagues.append(colleague)
    
    def remove(self, colleague: Colleague) -> None:
        if self.is_colleague(colleague):
            self.colleagues.remove(colleague)

    
    def broadcast(self, colleague:Colleague, msg:str) -> None:
        if not self.is_colleague(colleague):
            return
        print(f'{colleague.name} sent this message -> {msg}')

    
    def direct(self, sender:Colleague, receiver:str, msg:str) -> None:
        if not self.is_colleague(sender):
            return
        
        receiver_obj: List[Colleague]= [
            colleague for colleague in self.colleagues
            if colleague.name == receiver
        ]

        if not receiver_obj:
            return
        
        receiver_obj[0].direct(
            f'{sender.name} to {receiver} -> {msg}'
        )

if __name__== "__main__":
    chat = Chatroom()
    paulo = Person('Paulo', chat)
    jose = Person('Jose', chat)
    marta = Person('Marta', chat)
    camilo = Person('camilo', chat)

    chat.add(paulo)
    chat.add(jose)
    chat.add(marta)
    chat.add(camilo)

    jose.broadcast('Olá Pessoas')
    marta.broadcast('Olá a todos')

    jose.send_direct('Marta','Oi tudo bem?')
    marta.send_direct('Jose','Viva, queres pinar?')

    