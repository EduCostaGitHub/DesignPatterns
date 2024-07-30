"""
Monostate (ou Borg) - É uma variação do singleton proposto
por Alex Martelli que tem a intenção de garantir que o
estado do objeto seja igual para todas as instâncias
"""

class StringReprMixin:
    def __str__(self) -> str:
        params =', '.join([f'{k}={v}' for k, v in self.__dict__.items()])
        #print(params)
        return f'{self.__class__.__name__}({params})'
    
    def __repr__(self) -> str:
        return self.__str__()


class MonoStateSimple(StringReprMixin):
    _state : dict = {}

    def __init__(self, name=None, surname=None) -> None:
        self.__dict__ = self._state

        if name is not None:
            self.name = name
        
        if surname is not None:
            self.surname = surname
    
if __name__ == '__main__':
    m1 = MonoStateSimple('Edu')
    m2 = MonoStateSimple(surname='Costa')
    print(m1)
    print(m2)