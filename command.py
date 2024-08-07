"""
Command tem intenção de encapsular uma solicitação como
um objecto, desta forma permitindo parametrizar clientes com diferentes
solicitações, enfileirar ou fazer registo (log) de solicitações e suportar
operações que podem ser desfeitas.

É formado por um cliente (quem orquestra tudo), um invoker (que invoca as
solicitações), um ou vários objetos de comando (que fazem a ligação entre o
receiver e a acção a ser executada) e um receiver (o objeto que vai executar a
ação no final).


"""
from __future__ import annotations
from monostate_2 import StringReprMixin
from typing import List, Dict
from abc import ABC, abstractmethod


if __name__== "__main__":
    pass