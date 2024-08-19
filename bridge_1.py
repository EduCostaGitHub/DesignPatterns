"""
Bridge é um padrão de projecto estrutural que 
tem a intenção de desacoplar uma abstração
da sua implementação, de modo que as duas 
possam variar e evoluir independentemente

Abstração é uma camada de alto nível para algo.
Geralmente, a abstração não faz nenhum trabalho
por conta própria, ela delega parte ou todo o
trabalho para a camada de implementação.

RELEMBRANDO: Adapter é um padrão de projeto
estrutural que tem a intenção de permitor
que duas classes que seriam incompatíveis
trabalhem em conjunto através de um 'adaptador'

Diferença (GOF pag. 208) - A diferença chave
entre esses padrões está nas suas intenções...
...O padrão adapter faz as coisas funcionarem
APÓS elas terem sido proejtadas; o Bridge faz
as coisas funcionarem ANTES que existam...

"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Dict, Literal


class IRemoteControl(ABC):
    @abstractmethod
    def increase_volume(self) -> None:
        pass

    @abstractmethod
    def decrease_volume(self) -> None:
        pass

    @abstractmethod
    def power(self) -> None:
        pass

class RemoteControl(IRemoteControl):
    def __init__(self, device: IDevice) -> None:
        self._device = device
    
    def increase_volume(self) -> None:
        self._device.volume +=10
    
    def decrease_volume(self) -> None:
        self._device.volume -=10

    def power(self) -> None:
        self._device.power = not self._device.power

class RemoteWithMute(RemoteControl):
    def mute(self) -> None:
        self._device.volume = 0

class IDevice(ABC):
    @property
    @abstractmethod
    def volume(self) -> int: pass

    @volume.setter    
    def volume(self,volume:int) -> None:pass

    @property 
    @abstractmethod   
    def power(self) -> bool: pass

    @power.setter
    def power(self, power: bool) ->bool: pass

class TV(IDevice):
    def __init__(self) -> None:
        self._volume: int = 10
        self._power: bool = False
        self._name: str = self.__class__.__name__

    @property   
    def volume(self) -> int:
        return self._volume

    @volume.setter    
    def volume(self,volume:int) -> None:
        if not self._power:
            print(f'Please Turn {self._name} ON ')
            return

        if volume > 100 or volume <= 0:
            print(f'TV on range {self._name}')
            return
        
        self._volume = volume
        print(f'Volume of {self._name} set to: {self._volume}')         

    @property        
    def power(self) -> bool:
        return self._power

    @power.setter
    def power(self, power: bool) -> None: 
        self._power = power
        self._status: Literal['ON'] | Literal['OFF'] = 'ON' if self._power else 'OFF'
        print(f'{self._name} is now {self._status}')


if __name__ == "__main__":
    tv = TV()

    remote = RemoteControl(tv)

    remote.increase_volume()
    remote.power()
    remote.decrease_volume()
    remote.increase_volume()
    remote.increase_volume()
    remote.power()
    remote.increase_volume()

