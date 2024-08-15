"""
Adapter é um padrão de projecto estrutural que 
tem a intenção de permitir que duas classes 
que seriam incompatíveis trabalhem em conjunto
através de um 'adaptador'
"""

from __future__ import annotations
from typing import List, Dict, Tuple,Any
from abc import ABC, abstractmethod

class IControl(ABC):
   @abstractmethod
   def top(self) -> None:pass

   @abstractmethod
   def right(self) -> None:pass

   @abstractmethod
   def down(self) -> None:pass

   @abstractmethod
   def left(self) -> None:pass

class Control(IControl):
   
   def top(self) -> None:
        print('Moving UP')
   
   def right(self) -> None:
        print('Moving Right')

   def down(self) -> None:
        print('Moving Down')
   
   def left(self) -> None:
        print('Moving Left')

class NewControl:
   
   def move_top(self) -> None:
        print('Moving UP')
   
   def move_right(self) -> None:
        print('Moving Right')

   def move_down(self) -> None:
        print('Moving Down')
   
   def move_left(self) -> None:
        print('Moving Left')
       
class ControlAdapter:
    """Adapter Object"""
    def __init__(self, new_control: NewControl) -> None:
        self.new_control = new_control

    def top(self) -> None:
        self.new_control.move_top()
   
    def right(self) -> None:
        self.new_control.move_right()

    def down(self) -> None:
        self.new_control.move_down()
   
    def left(self) -> None:
        self.new_control.move_left()

class ControlAdapter2(Control, NewControl):
    """Adapter Class"""
    def top(self) -> None:
        self.move_top()
   
    def right(self) -> None:
        self.move_right()

    def down(self) -> None:
        self.move_down()
   
    def left(self) -> None:
        self.move_left()
    

    


if __name__== "__main__":
   
   """Control - Adapter Object"""
   new_control = NewControl()
   control_object = ControlAdapter(new_control)
   control_object.top()
   control_object.right()

   print()
   

   """Control - Adapter class"""
   control_class = ControlAdapter2()
   control_class.down()
   control_class.right()
   