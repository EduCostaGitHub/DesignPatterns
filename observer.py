"""
O Padrão Observer tem a intenção de 
definir uma dependência de um-para-muitos entre 
objetos, de maneira que quando um objecto muda de 
estado, todo os seus dependentes são notificados
e atualizados automaticamente

Um observer é um objecto que gostaria de ser
informado, um observable (subject) é a entidade
que gere as infromações

"""
from __future__ import annotations
from typing import List, Dict
from abc import ABC, abstractmethod

from monostate_2 import StringReprMixin


class IObservable(ABC):
    """ Interface Observable"""

    @property
    @abstractmethod
    def state(self) -> Dict:
        raise NotImplementedError

    @abstractmethod
    def addObserver(self, observer: IObserver) -> None:
        raise NotImplementedError

    @abstractmethod
    def removeObserver(self, observer: IObserver) -> None:
        raise NotImplementedError

    @abstractmethod
    def notifyObservers(self) -> None:
        raise NotImplementedError


class IObserver(ABC):
    @abstractmethod
    def update(self) -> None:
        raise NotImplementedError


class WeatherStation(IObservable):
    def __init__(self) -> None:
        self._observers: List[IObserver] = []
        self._state: Dict = {}

    @property
    def state(self) -> Dict:
        return self._state

    @state.setter
    def state(self, state_update: Dict) -> None:
        new_state: Dict = {**self._state, **state_update}

        if new_state != self._state:
            self._state = new_state
            self.notifyObservers()

    def reset_state(self) -> None:
        self._state = {}
        self.notifyObservers()

    def addObserver(self, observer: IObserver) -> None:
        self._observers.append(observer)

    def removeObserver(self, observer: IObserver) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def notifyObservers(self) -> None:
        for observer in self._observers:
            observer.update()


class SmartPhone(IObserver, StringReprMixin):
    def __init__(self, name, observable: IObservable) -> None:
        self.name = name
        self.observable = observable

    def update(self) -> None:
        observable_name = self.observable.__class__.__name__
        print(f'{self.name} -> {observable_name} updated '
              f'new data -> {self.observable.state}')


if __name__ == "__main__":
    weather_station = WeatherStation()

    smartphone = SmartPhone('iPhone', weather_station)
    smartphone2 = SmartPhone('Pixel8', weather_station)

    weather_station.addObserver(smartphone)
    weather_station.addObserver(smartphone2)

    # data
    weather_station.state = {'temperature': '30'}
    print()
    weather_station.state = {'temperature': '30'}
    print()
    weather_station.state = {'humidity': '80%'}
    print()
    weather_station.state = {'temperature': '28'}
