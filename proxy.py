"""
O Proxy é um padrão de projecto que tem a 
intenção de fornecer um objecto substituto que atua
como se fosse o objecto real que o código cliente
gostaria de usar.

O Proxy receberá as solicitações e terá controle
sobre como e quando repassar tais solicitações ao
objecto real.

Com base no modo como os proxies são usados,
nós os classificamos:

-Proxy Virtual: Controla acesso e recursos que podem 
ser caros para a criação ou utilização.

-Proxy Remoto: Controla accesso a resursos que estão 
em servidores remotos.

-Proxy de Proteção: Controla acesso a recursos que possam
necessitar de autenticação ou permissão.

-Proxy Inteligente: além de controlar acesso ao
objecto real, também executa tarefas adicioanais para 
saber quando e como executar determinadas ações.

Proxies podem fazer várias coisas diferentes:
Criar logs, autenticar users, distribuir serviços,
criar cache, criar e destruir objetos, adiar execuções
e muito mais...
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from ast import main
from multiprocessing.spawn import _main
from threading import main_thread
from time import sleep
from typing import List, Dict


class IUser(ABC):
    """ Subject Interaface"""
    firstname: str
    lastname: str


    @abstractmethod
    def get_addresses(self) -> List[Dict]:
        raise NotImplementedError

    @abstractmethod
    def get_all_user_data(self) -> Dict:
        raise NotImplementedError


class RealUser(IUser):
    """Real Subject"""

    def __init__(self, firstname: str, lastname: str) -> None:
        sleep(2)  # request simulation
        self.firstname = firstname
        self.lastname = lastname

    def get_addresses(self) -> List[Dict]:
        sleep(2)  # request simulation
        return [
            {'rua': 'Av Artur Seemdo', 'numero': 10}
        ]

    def get_all_user_data(self) -> Dict:
        sleep(2)  # request simulation
        return {'cc': '11073338', 'nif': 219142718}


class UserProxy(IUser):
    """Proxy"""

    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname

        # Lazy#
        self._realuser: RealUser
        self._cached_addresses: List[Dict]
        self._all_user_data: Dict

    def get_real_user(self) -> None:
        if not hasattr(self, '_realuser'):
            self._realuser = RealUser(self.firstname, self.lastname)

    def get_addresses(self) -> List[Dict]:
        self.get_real_user()
        if not hasattr(self, '_cached_addresses'):
            self._cached_addresses = self._realuser.get_addresses()

        return self._cached_addresses

    def get_all_user_data(self) -> Dict:
        self.get_real_user()
        if not hasattr(self, '_all_user_data'):
            self._all_user_data = self._realuser.get_all_user_data()

        return self._all_user_data


if __name__ == "__main__":
    edu = UserProxy('Edu', 'Costa')

    print(edu.firstname, edu.lastname)
    # 6 seconds delay
    print(edu.get_all_user_data())
    print(edu.get_addresses())

    # all in cache
    for i in range(5):
        print(edu.get_all_user_data())
