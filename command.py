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
from typing import List, Dict, Tuple
from abc import ABC, abstractmethod

#Receiver
class Light:
    def __init__(self, name:str, room_name:str) -> None:
        self.name = name
        self.room_name = room_name
        self.default_color = 'Default Color'
        self.color = self.default_color

    def on(self) -> None:
        print(f'Light {self.name} on {self.room_name} is ON')

    def off(self) -> None:
        print(f'Light {self.name} on {self.room_name} is OFF')

    def change_color(self, color:str) -> None:
        self.color = color
        print(f'Light {self.name} on {self.room_name} is with color: {self.color}')

#Command Interface
class ICommand(ABC):
    @abstractmethod
    def execute(self) -> None: raise NotImplementedError

    @abstractmethod
    def undo(self) -> None: raise NotImplementedError


class LightOnCommand(ICommand):
    def __init__(self, light: Light) -> None:
        self.light = light
    
    def execute(self) -> None:
        self.light.on()

    def undo(self) -> None:
        self.light.off()

class LightColorCommand(ICommand):
    def __init__(self, light: Light, color:str) -> None:
        self.light = light
        self.color=color
    
    def execute(self) -> None:
        self.light.change_color(self.color)

    def undo(self) -> None:
        self.light.change_color(self.light.default_color)

# Invoker
class RemoteController:
    def __init__(self) -> None:
        self._buttons: Dict[str,ICommand]={}
        self._undos: List[Tuple[str,str]] = []


    def button_add_command(self, name: str, command: ICommand) -> None:
        self._buttons[name] = command

    def button_execute(self, name:str) -> None:
        if name in self._buttons:
            self._buttons[name].execute()
            self._undos.append((name,'execute'))

    def button_undo(self, name:str) -> None:
        if name in self._buttons:
            self._buttons[name].undo()
            self._undos.append((name,'undo'))

    def global_undo(self):
        if not self._undos:
            return None
        
        button_name, action = self._undos[-1] # last operation

        if action == 'execute':
            self._buttons[button_name].undo()
        else:
            self._buttons[button_name].execute()

        self._undos.pop() # remove last operation

if __name__== "__main__":
    bedroom_light = Light('cealing_Light','bedroom')
    bathroom_light = Light('bathroom_Light','bedroom')

    bedroom_light_on = LightOnCommand(bedroom_light)
    bathroom_light_on = LightOnCommand(bathroom_light)

    bedroom_light_color_red = LightColorCommand(bedroom_light,'RED')

    remote = RemoteController()
    remote.button_add_command('bedroom_ceiling_light_Button',bedroom_light_on)
    remote.button_add_command('bathroom_light_button', bathroom_light_on)
    remote.button_add_command('bedroom_color_red', bedroom_light_color_red)

    remote.button_execute('bedroom_ceiling_light_Button')
    remote.button_execute('bathroom_light_button')
    print()
    remote.button_undo('bedroom_ceiling_light_Button')
    print()
    remote.button_execute('bedroom_color_red')
    remote.button_undo('bedroom_color_red')

    remote.global_undo()
    remote.global_undo()
    remote.global_undo()
