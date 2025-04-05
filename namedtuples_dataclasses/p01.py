# structs and classes


# Namedtuples (Structs leves)

from collections import namedtuple

# Equivalente a uma struct em C
Ponto = namedtuple("Ponto", ["x", "y"])
p = Ponto(10, 20)
print(p.x)  # 10
print(p.y)  # 20

# Vantages
# - Mais legivel que tuplas normais(p[0] vs p.x)
# - imutável (thread-safe)
# - consome menos memória que classes normais
# - compatível com unpacking: x, y = p


# Recursos avançados

# Valores padrão (Python 3.7+)
Ponto = namedtuple('Ponto', ['x', 'y'], defaults=[0, 0])

# Métodos adicionais
class Ponto(namedtuple('PontoBase', ['x', 'y'])):
    def distancia(self, outro):
        return ((self.x - outro.x)**2 + (self.y - outro.y)**2)**0.5

# Dataclasses (Classes de dados mordenas)
# structs on steroids

from dataclasses import dataclass


@dataclass
class Ponto:
    x: float
    y:float
    nome: str = "origem" # valor padrão

p = Ponto(1.5, 2.5)

# Vantagens sobre namedtuples
# - mutavel por padrão (mas pode ser imutavel com @dataclass(frozen=True))
# - suporte a herança
# - métodos adicionais gerados automaticamente (__init__, __repr__, __eq__, et)
# - tipagem explicita (opcional, mas recomendado)
#

#// Equivalente aproximado em C++20
#struct Ponto {
#    double x;
#    double y;
#    std::string nome = "origem";
#    
#    auto operator<=>(const Ponto&) const = default;
#};

# Recursos avançados
from dataclasses import asdict, astuple, field


@dataclass(order=True) # gera métodos de comparação
class Pessoa:
    nome: str,
    idade: int,
    hobbies: list[str] = field(default_factory=list)

    @property
    def nome_completo(self):
        return f"{self.nome} ({self.idade})"

# Conversão para dicionario/tupla
p = Pessoa("João", 30)
print(asdict(p)) # {'nome': 'João', 'idade': 30, 'hobbies': []}

from collections import namedtuple
# Examplo avançado combinando conceitos
from dataclasses import dataclass
from typing import List

Coordenada = namedtuple('Coordenada', ['lat', 'long'])

@dataclass
class Cidade:
    nome: str
    coordenadas: Coordenada
    vizinhos: List[str] = field(default_factory=list)

    def adicionar_vizinhos(self, mome: str):
        self.vizinhos.append(nome)

# Uso
sp = Cidade("São paulo", Coordenada(-23.5, -46.6))
sp.adicionar_vizinhos("Campinas")



