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

#Context
class Order:
    def __init__(self) -> None:
        self.state: OrderState = PaymentPending(self)

    def pending(self):
        self.state.pending()

    def approve(self):
        self.state.approve()

    def reject(self):
        self.state.reject()


class OrderState(ABC):
    def __init__(self, order:Order) -> None:
        self.order = order

    def __str__(self) -> str:
        return self.__class__.__name__
        
    @abstractmethod
    def pending(self) -> None: pass

    @abstractmethod
    def approve(self) -> None: pass

    @abstractmethod
    def reject(self) -> None: pass

class PaymentPending(OrderState):
    
    def pending(self) -> None:
        print('Payment is pending, nothing to do.')

    
    def approve(self) -> None: 
        self.order.state = PaymentApproved(self.order)
        print('Payment approved.')

    
    def reject(self) -> None: 
        self.order.state = PaymentRejected(self.order)
        print('Payment rejected.')


class PaymentApproved(OrderState):
    
    def pending(self) -> None: 
        self.order.state = PaymentPending(self.order)
        print('Payment pending.')

    
    def approve(self) -> None: 
        print('Payment is approved, nothing to do.')

    
    def reject(self) -> None: 
        self.order.state = PaymentRejected(self.order)
        print('Payment rejected.')


class PaymentRejected(OrderState):
    
    def pending(self) -> None:
        print('Payment is rejected, nothing to do.')

    
    def approve(self) -> None: 
        print('Payment is rejected, nothing to do.')

    
    def reject(self) -> None:
        print('Payment is rejected, nothing to do.')


if __name__== "__main__":
    order = Order()
    order.pending()
    order.approve()
    order.pending()
    order.reject()
    order.pending()



    