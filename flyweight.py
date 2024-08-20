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
from typing import List, Dict


class Client:
    """Context"""

    def __init__(self, name: str) -> None:
        self.name: str = name
        self._addresses: List[Address] = []

        # Extrinsic address data
        self.address_number: str
        self.address_detail: str

    def add_address(self, address: Address) -> None:
        self._addresses.append(address)

    def list_addreses(self) -> None:
        for address in self._addresses:
            address.show_address(self.address_number, self.address_detail)


class Address:
    """Flyweight"""

    def __init__(self, street: str, neighbourhood: str, zip_code: str) -> None:
        self._street: str = street
        self._neighbourhood: str = neighbourhood
        self._zip_code: str = zip_code

    def show_address(self, address_number: str, address_detail: str) -> None:
        print(
            self._street,
            address_number,
            self._neighbourhood,
            self._zip_code,
            address_detail,
        )


class AddressFactory:
    _addresses: Dict = {}

    def _get_key(self, **kwargs) -> str:
        return ''.join(kwargs.values())

    def get_address(self, **kwargs) -> Address:
        key = self._get_key(**kwargs)

        try:
            address_flyweight = self._addresses[key]
            print('reusing object')
        except KeyError:
            address_flyweight = Address(**kwargs)
            self._addresses[key] = address_flyweight
            print('New Object')

        return address_flyweight


if __name__ == "__main__":
    address_factory = AddressFactory()

    address1: Address = address_factory.get_address(
        street='Av Artur semedo',
        neighbourhood='Vila Chã',
        zip_code='2700-783'
    )

    address2: Address = address_factory.get_address(
        street='Av Artur semedo',
        neighbourhood='Vila Chã',
        zip_code='2700-783'
    )

    edu = Client('Edu')
    edu.address_number = '10'
    edu.address_detail = 'Casa'
    edu.add_address(address1)
    edu.list_addreses()

    marta = Client('Marta')
    marta.address_number = '12'
    marta.address_detail = 'Casa'
    marta.add_address(address2)
    marta.list_addreses()
