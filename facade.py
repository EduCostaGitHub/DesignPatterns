"""
Façade (Fachada) é um padrão de projeto estrutural 
que tem a intenção de fornecer uma interface
unificada para um conjunto de interfaces em um
subsistema. Façade define uma interace de nível
mais alto que torna o subsostema mais fácil de ser 
usado
"""

from __future__ import annotations
from typing import List, Dict, Tuple, Any
from abc import ABC, abstractmethod

from observer import WeatherStation, SmartPhone, IObserver


class WeatherStationFacade:
    def __init__(self) -> None:
        self.weather_station = WeatherStation()
        self.smartphone: SmartPhone

        weather_station = self.weather_station

        smartphone = SmartPhone('iPhone', weather_station)
        smartphone2 = SmartPhone('Pixel8', weather_station)

        weather_station.addObserver(smartphone)
        weather_station.addObserver(smartphone2)

    def add_observer(self, observer: IObserver) -> None:
        self.weather_station.addObserver(observer)

    def remove_observer(self, observer: IObserver) -> None:
        self.weather_station.removeObserver(observer)

    def change_state(self, state: Dict) -> None:
        self.weather_station.state = state

    def remove_smartphone(self):
        self.weather_station.removeObserver(self.smartphone)

    def reset_state(self):
        self.weather_station.reset_state()


if __name__ == "__main__":
    weather_station = WeatherStationFacade()

    # data
    weather_station.change_state({'temperature': '30'})
    print()
    weather_station.change_state({'temperature': '30'})
    print()
    weather_station.change_state({'humidity': '80%'})
    print()
    weather_station.change_state({'temperature': '28'})
