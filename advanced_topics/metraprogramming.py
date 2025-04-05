# Metaprogramação Avançada
# new e Controle de Criação de instancia
# Similar a sobrecarga do operador "new" em C++, mas mais flexivel


class Singleton:
    _instancia = None

    def __new__(cls, *args, **kwargs):
        if not cls._instancia:
            cls._instancia = super().__new__(cls)
        return cls._instancia


a = Singleton()
b = Singleton()
print(a is b)  # True


# Prepare para namespaces personalizadas
# Util para criar DSLs (Domain Specific Languages)
class MeuNamespace(dict):
    def __setitem__(self, key, value):
        print(f"Definindo {key} = {value}")
        super().__setitem__(key.upper(), value)


class MinhaMeta(type):
    @classmethod
    def __prepare__(metacls, name, bases, **kwargs):
        return MeuNamespace()


class MinhaClasse(metaclass=MinhaMeta):
    atributo = 42

    def metodo(self):
        pass


# Os nomes foram convertidos para maiúsculas
print(MinhaClasse.__dict__.keys())  # Mostra 'ATRIBUTO', 'METODO'


# Decorators como Metaclasses
# Alternativa mais simples a metaclasses em alguns casos
def decorator_automatico(cls):
    """Adiciona automaticamente métodos baseados nos atributos"""
    for name, value in cls.__dict__.items():
        if isinstance(value, int):

            def getter(self, val=value):
                return val

            setattr(cls, f"get_{name}", getter)
    return cls


@decorator_automatico
class MinhaClasse:
    VALOR = 42
    OUTRO = 100


obj = MinhaClasse()
print(obj.get_VALOR())  # 42
print(obj.get_OUTRO())  # 100

# Casos Reais Avançados
# Sistema de Plugins com Decoratos
PLUGINS = {}


def registrar_plugin(nome):
    def decorator(cls):
        PLUGINS[nome] = cls
        return cls

    return decorator


@registrar_plugin("csv")
class CSVProcessor:
    def process(self, data):
        print("Processando CSV")


@registrar_plugin("json")
class JSONProcessor:
    def process(self, data):
        print("Processando JSON")


# Uso dinâmico
formato = input("Formato (csv/json): ")
processor = PLUGINS[formato]()
processor.process("dados")

# Validação de Tipos em Runtime
from inspect import signature


def validar_tipos(func):
    sig = signature(func)

    def wrapper(*args, **kwargs):
        bound = sig.bind(*args, **kwargs)
        for name, value in bound.arguments.items():
            if name in func.__annotations__:
                expected = func.__annotations__[name]
                if not isinstance(value, expected):
                    raise TypeError(
                        f"Argumento '{name}' deve ser {expected}, "
                        f"obteve {type(value)}"
                    )
        return func(*args, **kwargs)

    return wrapper


@validar_tipos
def processar(valor: int, texto: str) -> str:
    return texto * valor


print(processar(3, "a"))  # 'aaa'
# processar("3", "a")     # TypeError

# Exercicio pratico
# Implemente um decorator @deprecated que:
# - Emite um aviso quando a função é chamada
# - Pode especificar uma alternativa
# - Mostra a linha de código onde a função foi chamada

import inspect
import warnings


def deprecated(alternativa=None):
    # Implemente aqui
    pass


@deprecated(alternativa="nova_funcao")
def funcao_antiga():
    pass


@deprecated()
def outra_funcao():
    pass


# Deve mostrar:
# Warning: funcao_antiga está obsoleta. Use nova_funcao instead.
# Chamado de arquivo.py, linha 20
funcao_antiga()
