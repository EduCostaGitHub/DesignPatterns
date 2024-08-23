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
from typing import List, Dict



if __name__ == "__main__":
    pass