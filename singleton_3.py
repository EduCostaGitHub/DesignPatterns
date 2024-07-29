"""
O Singleton tem a intenção de garantir que uma classe tenha somente
uma instância e fornece um ponto golbal de acesso para a mesma.

When discussing which pattern to drop, we found
that we still love them all.
(not really-I'm in favor of dropping Singleton.
Its use is almost always a design smell.)
- Erich Gamma, em entrevista para infomIT
http://www.informit.com/articles/article.aspx?p=1404056
"""

# from typing import Any

# class Meta(type):
#     def __call__(call, *args: Any, **kwargs: Any) -> Any:
#         print('META CALL executed')
#         return super().__call__(*args, **kwargs)

# class Pessoa(metaclass=Meta):
#     def __new__(cls,*args, **kwargs):
#         print('New executed')
#         return super().__new__(cls)
    
#     def __init__(self, name) -> None:
#         print('Init executed')
#         self.name = name

#     def __call__(self, *args, **kwargs):
#         print('Call Called')
#         print(args)
#         print(*args)
#         for id in range(len(args)):
#             print(args[id])

# if __name__ == '__main__':
#     p1 = Pessoa('Edu')
#     print(p1.name)

#     #p1(2,3)

#Metaclass
from typing import Any


class Singleton(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            pass

   
class AppSettings(metaclass=Singleton):    
    def __init__(self) -> None:
        self.tema = 'dark'
        self.font = '18px'
    
if __name__ == '__main__':
    ApS_1 = AppSettings()
    ApS_1.tema = 'Bright'
    print(ApS_1.tema)

    ApS_2 = AppSettings()
    print(ApS_1.tema)

    
    print(ApS_1)
    print(ApS_2)

