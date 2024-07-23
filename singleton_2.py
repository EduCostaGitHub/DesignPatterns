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

class AppSettings:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls,*args, **kwargs)
        return cls._instance
    
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

