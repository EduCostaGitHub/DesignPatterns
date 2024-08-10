"""
O Padrão de Projeto State é um padrão comportamental
que tem a intenção de permitir a um objeto mudar 
seu comportamento quando o seu estado interno 
muda.

O Objecto parecerá ter mudado sua classe

"""
from __future__ import annotations
from monostate_2 import StringReprMixin
from typing import List, Dict, Tuple
from abc import ABC, abstractmethod

class Sound:
    def __init__(self) -> None:
        self.mode: PlayMode = RadioMode(self)
        self.playing = 0

    def change_mode(self,mode: PlayMode) -> None:
        self.playing = 0 
        self.mode = mode

    def press_next(self) -> None:
        self.mode.press_next()
        print(self)

    
    def press_prev(self) -> None:
        self.mode.press_prev()
        print(self)


    def __str__(self) -> str:
        return str(self.playing)

class PlayMode(ABC):
    def __init__(self, sound:Sound) -> None:
        self.sound = sound

    @abstractmethod
    def press_next(self) -> None: pass

    @abstractmethod
    def press_prev(self) -> None: pass

class RadioMode(PlayMode):
    def press_next(self) -> None:
        self.sound.playing += 1000
        print('Radio Mode -> Searching next staion')
        

    
    def press_prev(self) -> None:
        self.sound.playing -= 1000 if self.sound.playing >0 else 0
        print('Radio Mode -> Searching previouse staion')


class MusicMode(PlayMode):
    def press_next(self) -> None:
        self.sound.playing += 1
        print('Music Mode -> Searching next staion')
        

    
    def press_prev(self) -> None:
        self.sound.playing -= 1 if self.sound.playing >0 else 0
        print('Music Mode -> Searching previouse staion')



if __name__== "__main__":
    
    sound = Sound()
    radio = RadioMode(sound)
    music = MusicMode(sound)
    sound.press_next()
    sound.press_next()
    sound.change_mode(music)
    sound.press_next()
    sound.press_next()
    sound.press_prev()
    sound.press_prev()
    sound.press_prev()
    sound.press_prev()
    sound.press_prev()
    




    