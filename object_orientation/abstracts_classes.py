# Se você vem de C++, pode pensar nas Abstract Base Classes (ABCs) como:
# - Classes puramente virtuais em C++
# - Interfaces em Java/C#
# - Um mecanismo formal para definir interfaces em Python

# Oque são ABCs?
# - Definem uma interface (métodos e propriedades que classes derivadas devem implementar)
# - Não podem ser instanciadas diretamente
# - Permitem verificação de implementação (isinstance, issubclass)

# Por que usar em vez de duck typing?
# - Documentação clara da API esperada
# - Verificação em tempo de desenvolvimento
# - Fornece erros mais cedo (em vez de falhar em runtime)

# Módulo ABC
# O módulo padrão fornece:
# - ABC: Classe base para criar ABCs
# - @abstractmethod: Decorator para marcar métodos como abstratos

# Exemplo básico:

from abc import ABC, abstractmethod


class FormaGeometrica(ABC):
    @abstractmethod
    def area(self) -> float:
        """Calcula a área da forma"""
        pass

    @abstractmethod
    def perimetro(self) -> float:
        """Calcula o perímetro da forma"""
        pass

    # Métodos concretos são permitidos
    def descricao(self) -> str:
        return "Forma geométrica abstrata"


class Retangulo(FormaGeometrica):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self) -> float:
        return self.largura * self.altura

    def perimetro(self) -> float:
        return 2 * (self.largura + self.altura)


# Tentar instanciar a ABC diretamente
# FormaGeometrica()  # TypeError: Can't instantiate abstract class

ret = Retangulo(3, 4)
print(ret.area())  # 12
print(ret.perimetro())  # 14ico


# Registro de classes virtuais
# Voce pode registrar uma classe como implementação de uma ABC sem herdar dela:

from abc import ABC, abstractmethod


class MinhaABC(ABC):
    @abstractmethod
    def metodo_obrigatorio(self):
        pass


class ImplementacaoReal:
    def metodo_obrigatorio(self):
        return "Implementado!"


MinhaABC.register(ImplementacaoReal)

print(issubclass(ImplementacaoReal, MinhaABC))  # True
print(isinstance(ImplementacaoReal(), MinhaABC))  # True

# ABCs na lib padrão
# exemplo com collections.abc
from collections.abc import Sequence


class MinhaLista(Sequence):
    def __init__(self, *args):
        self._data = list(args)

    def __getitem__(self, index):
        return self._data[index]

    def __len__(self):
        return len(self._data)

    # __contains__, index, count vêm "de graça" por herdar de Sequence


ml = MinhaLista(1, 2, 3)
print(len(ml))  # 3
print(ml[1])  # 2
print(2 in ml)  # True
print(ml.index(3))  # 2

# ABCs Avançadas
# Propriedades abstratas
from abc import ABC, abstractproperty


class Sensor(ABC):
    @abstractproperty
    def leitura(self) -> float:
        """Retorna a leitura atual do sensor"""
        pass

    @property
    def unidade(self) -> str:
        return "unidades arbitrárias"


class SensorTemperatura(Sensor):
    def __init__(self):
        self._temp = 25.0

    @property
    def leitura(self) -> float:
        return self._temp

    @property
    def unidade(self) -> str:
        return "°C"


# Métodos de classe abstrato
from abc import ABC, abstractmethod


class ModeloDB(ABC):
    @classmethod
    @abstractmethod
    def buscar_por_id(cls, id):
        """Método de classe abstrato"""
        pass


class Usuario(ModeloDB):
    @classmethod
    def buscar_por_id(cls, id):
        return cls()  # Simulação


import inspect

# Padrão de registro (Plugin System)
# ABCs são uteis para implementar sistemas de plugins
from abc import ABC, abstractmethod


class Plugin(ABC):
    _plugins = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if not inspect.isabstract(cls):
            cls._plugins.append(cls)

    @abstractmethod
    def executar(self, dados):
        pass


class PluginA(Plugin):
    def executar(self, dados):
        return f"PluginA processou {dados}"


class PluginB(Plugin):
    def executar(self, dados):
        return f"PluginB transformou {dados}"


# Uso
for plugin_cls in Plugin._plugins:
    instance = plugin_cls()
    print(instance.executar("teste"))

# Exercicio pratico
from abc import ABC, abstractmethod


class TextFormatter(ABC):
    @abstractmethod
    def format(self, text: str) -> str:
        pass


# Implemente:
# 1. UpperFormatter (converte para maiúsculas)
# 2. ReverseFormatter (inverte o texto)
# 3. PrefixFormatter (adiciona um prefixo configurável)


class FormatadorComposto(TextFormatter):
    def __init__(self, *formatters):
        self.formatters = formatters

    def format(self, text: str) -> str:
        # Implemente a aplicação dos formatters em sequência
        pass


# Teste
formatter = FormatadorComposto(
    UpperFormatter(), ReverseFormatter(), PrefixFormatter(">>> ")
)
print(formatter.format("abc"))  # ">>> CBA"
