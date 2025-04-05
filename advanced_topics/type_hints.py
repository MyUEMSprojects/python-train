# Se você vem de C++, vai reconhecer muitos conceitos de tipos,
# mas com uma abordagem mais flexível e opcional.
# Python usa type hints para adicionar informação de tipos sem afetar a execução em runtime.


# Conceitos Básicos
# Anotações Simples
def saudacao(nome: str) -> str:
    return f"Olá, {nome}"


valor: int = 42
lista: list[str] = ["a", "b", "c"]

# Comparação com C++:
# - tipo similar a tipo variavel em C++
# - tipo similar a tipo de retorno em C++

# 2. Tipos Básicos
# Python	            C++ equivalente
# int	                int
# float	                double
# bool	                bool
# str	                std::string
# list[T]	            std::vector<T>
# dict[K, V]	        std::map<K, V>
# tuple[T1, T2, ...]	std::tuple<T1, T2>

# Recursos avançados
# Union Types (Tipos alternativos)
from typing import Union


def processa_input(input: Union[str, bytes]) -> None:
    # Equivalente a std::variant em C++
    pass

# Python 3.10+ simplificou com o operador |
def processa_input(input: str | bytes) -> None:
    pass

# Optional (Valores Nulos)
from typing import Optional


def find_user(id: int) -> Optional[str]:
    # Equivalente a std::optional em C++
    return None  # ou um str

# Pyhton 3.10+
def find_user(id: int) -> str | None:
    pass

# Generics (Templates Simplificados)
from typing import Generic, TypeVar

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self):
        self.items: list[T] = []
    
    def push(self, item: T) -> None:
        self.items.append(item)
    
    def pop(self) -> T:
        return self.items.pop()

# Comparação com C++

#template<typename T>
#class Stack {
#    std::vector<T> items;
#public:
#    void push(T item);
#    T pop();
#}

# Callable (Tipos para funções)

from typing import Callable


def aplicar_func(
    func: Callable[[int, int], float],  # (int, int) -> float
    a: int,
    b: int
) -> float:
    return func(a, b) para funções)

# Literal e Enums
from typing import Literal


def set_direction(direction: Literal["left", "right", "up", "down"]) -> None:
    pass


# Ferramentas de Ecosistema
# Mypy - verificador estatico de tipos:
# pip install mypy 
# mypy seu_script.py

# Type checking em tempo de execução
from typing import get_type_hints


def validate_types(func):
    hints = get_type_hints(func)
    def wrapper(*args, **kwargs):
        # Implementar validação
        return func(*args, **kwargs)
    return wrapper

# Casos reais

# 1 - API Tipada
from typing import TypedDict


class User(TypedDict):
    id: int
    name: str
    email: str | None

def get_user(user_id: int) -> User:
    return {
        "id": user_id,
        "name": "João",
        "email": None
    }

import numpy as np
# Data Science
import pandas as pd
from numpy.typing import NDArray


def process_data(
    data: pd.DataFrame,
    columns: list[str]
) -> tuple[NDArray[np.float64], NDArray[np.int32]]:
    # Processamento tipado
    pass

# Exercicio prático
# Implemente uma classe Vector com type hints completos

import math
from typing import Self, overload


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y
    
    @overload
    def __add__(self, other: float) -> Self: ...
    
    @overload
    def __add__(self, other: Self) -> Self: ...
    
    def __add__(self, other):
        # Implemente a adição
        pass
    
    def magnitude(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)
    
    @classmethod
    def from_polar(cls, r: float, theta: float) -> Self:
        return cls(r * math.cos(theta), r * math.sin(theta))



