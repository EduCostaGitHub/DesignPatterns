"""
Na programação POO, o termo factory (fábrica) refere-se a um classe ou método
que é responsável por criar objectos.

Vantagens:
    Permitem criar um sistema com baixo acoplamento entre clases porque 
    ocultam as classes que criam os objetos do código cliente.

    Facilitam a adição de novas classes ao código, porque o cliente não
    conhece e nem utiliza a implementação da classe (utiliza a factory)

    Podem facilitar o processo de 'cache' ou criação de 'Singletons' porque a
    fábrica pode retornar um objeto já criado para o cliente, ai invés de criar
    novos objetos smepre que o cliente precisar.

Desvantagens:
    Podem introduzir muitas classes no código

Vamos ver 2 tipos de Factory da GoF: Factory method e Abstract Factory

Nesta Aula:
Simple Factory -> Uma espécie de Factory Method parametrizado
Simple Factory pode não ser considerado um padrão de projeto por si só
Simple Factory pode quebrar princípios do SOLID

"""

class Vehicle:
    pass