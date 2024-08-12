"""
Iterator é um padrão comportamental que tem a 
intenção de fornecer um meio de acessar,
sequencialmente, os elementos de um objecto
agregado sem expor a sua representação subjacente.

- Uma coleção deve fornecer um meio de acessar
    os seus elementos sem expor sua estrutura interna
- Uma coleção pode ter maneiras e percursos diferentes
    para expor os seus elementos
- Deve separar a complexidadedos algoritmos
    de iteração da coleção em si

A ideia principal do padrão é retirar a responsabilidade
de acesso e percurso de uma coleção, delegando tais 
tarefas para um objecto iterador

"""

from __future__ import annotations
from monostate_2 import StringReprMixin
from typing import List, Dict, Tuple,Any
from abc import ABC, abstractmethod
from collections.abc import Iterator, Iterable

class MyIterator(Iterator):
    def __init__(self, collection: List[Any]) -> None:
        self._collection = collection
        self._index = 0 


    def __next__(self) -> Any:
        try:
            item = self._collection[self._index]
            self._index +=1
            return item
        except IndexError:
            raise StopIteration
        
class MyReverseIterator(Iterator):
    def __init__(self, collection: List[Any]) -> None:
        self._collection = collection
        self._index = -1

    def next(self):
        try:
            return self.__next__()
        except StopIteration:
            return None 
        
    def __next__(self) -> Any:
        try:
            item = self._collection[self._index]
            self._index -=1
            return item
        except IndexError:
            raise StopIteration
    
class MyList(Iterable):
    def __init__(self) -> None:
        self._items: List[Any] = []
        self._my_iterator = MyIterator(self._items)

    def add(self, value: Any) -> None:
        self._items.append(value)

    def __str__(self) -> str:
        return f'{self.__class__.__name__} ({self._items})'
    
    def __iter__(self) -> Iterator:
        return self._my_iterator

    def reverse_iterator(self) -> Iterator:
        return MyReverseIterator(self._items)


if __name__== "__main__":
    
    my_list = MyList()
    my_list.add('Eduardo')
    my_list.add('Zeca')
    my_list.add('Tulio')
    my_list.add('Gertrudes')

    print('stolen value:', next(iter(my_list)))
    print('stolen value:', next(my_list.__iter__()))
    
    for val in my_list:
        print(val)

    print()

    for val in my_list.reverse_iterator():
        print(val)
    



    
    




    