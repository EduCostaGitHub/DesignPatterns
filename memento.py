"""
GoF - Memento é um padrão de projecto comportamental
que tem a intenção de permitir gravar a restaurar 
um estado anteriiro de um objecto originator sem revelar os
detalhes de implementação e se mviolar o encapsulamento.

Originator é um objecto que deseja salvar o seu estado.
Memento é usado para salvar o estdo do Originator.
Caretaker é usado para armazenar mementos.
Caretaker é usado com o Padrão Command.
"""

from __future__ import annotations
from monostate_2 import StringReprMixin
from typing import List, Dict, Tuple,Any
from abc import ABC, abstractmethod
from collections.abc import Iterator, Iterable
from copy import deepcopy

class Memento:
    def __init__(self, state: Dict) -> None:
        self._state: Dict
        super().__setattr__('_state',state)

    def get_state(self) -> Dict:
        return self._state
    
    def __setattr__(self, name: str, value: Any) -> None:
        raise AttributeError('Sorry, I am immutable')
    
class ImageEditor:
    def __init__(self, name: str, width: int, height:int) -> None:
        self.name = name
        self.width = width
        self.height = height

    def save_state(self) -> Memento:
        return Memento(deepcopy(self.__dict__))
    
    def restore(self, memento: Memento) -> None:
        self.__dict__ = memento.get_state()

    def __str__(self) -> str:
        return f'{self.__class__.__name__}({self.__dict__})'
    
class Caretaker:
    def __init__(self, originator: ImageEditor) -> None:
        self._originator = originator
        self._mementos: List[Memento] = []

    def backup(self) -> None:
        self._mementos.append(self._originator.save_state())

    def restore(self) -> None:
        if not self._mementos:
            return
        
        self._originator.restore(self._mementos.pop())

if __name__== "__main__":
    img = ImageEditor('FOTO_1.jpg', 111,111)
    caretaker = Caretaker(img)

    caretaker.backup()

    img.name = 'FOTO_2.jpg'
    img.width = 222
    img.height =222
    caretaker.backup()
    
    img.name = 'FOTO_3.jpg'
    img.width = 333
    img.height =333
    caretaker.backup()

    img.name = 'FOTO_4.jpg'
    img.width = 444
    img.height =444
    caretaker.backup()

    print(img)

    caretaker.restore()
    print('Restore 1->', img)

    caretaker.restore()
    print('Restore 2->', img)

    caretaker.restore()
    print('Restore 3->', img)

    caretaker.restore()
    print('Restore 4->', img)

    
    
