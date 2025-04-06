# 1. State Machine (usando dicionários)
def state_A(input):
    print("Estado A")
    return state_B if input == "next" else state_A


def state_B(input):
    print("Estado B")
    return state_A if input == "back" else state_B


current_state = state_A
while True:
    cmd = input("> ")
    current_state = current_state(cmd)

# 2. Command Pattern (com funções parciais)
from functools import partial


def operation(a, b, op):
    return op(a, b)


commands = {
    "add": partial(operation, op=lambda x, y: x + y),
    "mul": partial(operation, op=lambda x, y: x * y),
}

# Uso
print(commands["add"](3, 4))  # 7

# Caso Real: Data Pipeline
from abc import ABC, abstractmethod


class DataSource(ABC):
    @abstractmethod
    def read(self):
        pass


class Transformer(ABC):
    @abstractmethod
    def transform(self, data):
        pass


class Pipeline:
    def __init__(self, source: DataSource, *transformers: Transformer):
        self.source = source
        self.transformers = transformers

    def run(self):
        data = self.source.read()
        for transformer in self.transformers:
            data = transformer.transform(data)
        return data


# Implementações concretas
class FileSource(DataSource):
    def read(self):
        return "dados,do,arquivo"


class CSVTransformer(Transformer):
    def transform(self, data):
        return data.split(",")


# Uso
pipeline = Pipeline(FileSource(), CSVTransformer())
print(pipeline.run())  # ['dados', 'do', 'arquivo']

# Exercício Prático

# Implemente o padrão Repository para acesso a dados:
#    Crie uma interface Repository com métodos CRUD
#    Implemente um InMemoryRepository
#    Use o padrão Strategy para permitir diferentes backends (memória, SQL, arquivo)

from abc import ABC, abstractmethod
from typing import Dict, Optional


class Repository(ABC):
    @abstractmethod
    def add(self, entity: Dict) -> str:
        """Retorna ID da entidade"""
        pass

    @abstractmethod
    def get(self, id: str) -> Optional[Dict]:
        pass

    @abstractmethod
    def update(self, id: str, entity: Dict) -> bool:
        pass


# Implemente:
# 1. InMemoryRepository
# 2. Um repositório que alterna entre backends
# 3. Testes unitários para sua implementação
