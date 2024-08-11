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

# Implement with functions - No Pattern

def handler_ABC(char: str) -> str:
    chars = ['A','B','C']

    if char in chars:
        return f'Handler ABC deal with this value - {char}'
    
    return handler_DEF(char)

def handler_DEF(char:str) -> str:
    chars = ['D','E','F']

    if char in chars:
        return f'Handler DEF deal with this value - {char}'
    
    return handler_unsolved(char)

def handler_unsolved(char:str) -> str:
    return f'Cannot deal with this value  - {char}'

if __name__== "__main__":

    print(handler_ABC('A'))
    print(handler_ABC('B'))
    print(handler_ABC('C'))
    print(handler_ABC('D'))
    print(handler_ABC('E'))
    print(handler_ABC('F'))
    print(handler_ABC('G'))
    




    