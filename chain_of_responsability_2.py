"""
Chain of responsability (COR) é um padrão comportamental
que tem a intenção de evitar o acoplamento do remetente de 
um solicitação ao seu receptor, ao dar a mais de um objecto
a oportunidade de tratar a solicitação.
Encadear os objectod receptores passando a solicitação 
ao longo da cadeia até que um objecto a trate.


"""
from __future__ import annotations
from monostate_2 import StringReprMixin
from typing import List, Dict, Tuple
from abc import ABC, abstractmethod

class Handler(ABC):
    def __init__(self) -> None:
        self.sucessor : Handler

    @abstractmethod
    def handle(self,char:str) -> str: pass

class HandlerABC(Handler):
    def __init__(self, sucessor: Handler) -> None:
        self.sucessor = sucessor
        self.chars = ['A','B','C']

    def handle(self, char: str) -> str:
        if char in self.chars:
            return f'Handler ABC deal with this value - {char}'
        
        return self.sucessor.handle(char)
    
class HandlerDEF(Handler):
    def __init__(self, sucessor: Handler) -> None:
        self.sucessor = sucessor
        self.chars = ['D','E','F']

    def handle(self, char: str) -> str:
        if char in self.chars:
            return f'Handler DEF deal with this value - {char}'
        
        return self.sucessor.handle(char)


class HandlerUnsolved(Handler):        

    def handle(self, char: str) -> str:
        return f'Cannot deal with this value  - {char}'

if __name__== "__main__":
    handlerABC = HandlerABC(HandlerDEF(HandlerUnsolved()))
    print(handlerABC.handle('A'))
    print(handlerABC.handle('B'))
    print(handlerABC.handle('C'))
    print(handlerABC.handle('D'))
    print(handlerABC.handle('E'))
    print(handlerABC.handle('F'))
    print(handlerABC.handle('G'))
    print(handlerABC.handle('H'))

    
    




    