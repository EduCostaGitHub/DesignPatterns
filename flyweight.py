"""
Flyweight é um padrão de projecto estrutural
que tem a intenção de usar compartilhamento
para suportar eficientemente grandes qunatidades 
de objectos de forma granular.

Só se utiliza quando TODAS as condições
a seguir forem verdadeiras:

- Uma aplicação utiliza uma grande quantidade de
objectos;

- Os custos de armazenamento são altos por causa
da grande quantidade de objectos;

- A maioria dos estados de objectos podem se tornar
extrínsecos;

- Muitos objectos podem ser substituídos por poucos
objectos compartilhados;

- A aplicação não depende da identidade dos bjecots.

Importante:
- Estado intrínseco é o estado do objecto que não muda,
esse estado deve estar dentro do objecto flyweight;

- Estado extrínseco é o estado do objecto que muda,
esse estado pode ser movido para fora do objecto 
flyweight;

Dicionário:

Intrínseco - Que faz parte de ou que constitui a 
essência, a natureza de algo: que é próprio de 
algo: inerente.

Extrínseco - Que não pertence à essência de algo:
que é exterior.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Dict, Literal

class Client:
    """Context"""
    def __init__(self, name : str) -> None:
        self.name: str = name
        self._addresses: List[Address] =[]

        # Extrinsic address data
        self._address_number: str
        self._address_detail: str

    def add_address(self, address : Address) -> None:
        self._addresses.append(address)

    def list_addreses(self) -> None:
        for address in self._addresses:
            address.show_address(self._address_number, self._address_detail)

class Address:
    """Flyweight"""
    def __init__(self) -> None:
        pass

    def show_address(self, address_number:str, address_detail:str) -> None:
        pass

if __name__ == "__main__":
    pass
