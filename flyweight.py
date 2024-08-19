"""
Flyweight é um padrão de projecto estrutural
que tem a intenção de usar compartilhamento
para suportar eficientemente grandes qunatidades 
de objectos de forma granular.

Só se utiliza quando TODAS as condições
a seguir forem verdadeiras:

- Uma aplicação utiliza uma grande quantidade de
objectos;

- Os custos de armazenamento são altos por causa
da grande quantidade de objectos;

- A maioria dos estados de objectos podem se tornar
extrínsecos;

- Muitos objectos podem ser substituídos por poucos
objectos compartilhados;

- A aplicação não depende da identidade dos bjecots.

Importante:
- Estado intrínseco é o estado do objecto que não muda,
esse estado deve estar dentro do objecto flyweight;

- Estado extrínseco é o estado do objecto que muda,
esse estado pode ser movido para fora do objecto 
flyweight;



"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Dict, Literal



if __name__ == "__main__":
    pass
