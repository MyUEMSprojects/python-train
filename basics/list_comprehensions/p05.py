# Os "magic methods" (também chamados de dunder = double underscore methods) permitem que classes Python implementem comportamentos especiais:

class Produto:
    def __init__(self, nome, preco):  # Construtor
        self.nome = nome
        self.preco = preco
    
    def __str__(self):  # Representação em string (print)
        return f"{self.nome}: R${self.preco:.2f}"
    
    def __repr__(self):  # Representação para desenvolvedores
        return f"Produto('{self.nome}', {self.preco})"
    
    def __eq__(self, other):  # Igualdade (==)
        if not isinstance(other, Produto):
            return False
        return self.nome == other.nome and self.preco == other.preco
    
    def __add__(self, other):  # Operador de adição (+)
        if isinstance(other, Produto):
            return self.preco + other.preco
        return self.preco + other

# Python suporta herança múltipla, permitindo que uma classe herde de várias bases:

class Dispositivo:
    def ligar(self):
        print("Dispositivo ligado")

class Conectavel:
    def conectar(self):
        print("Conectado à rede")

# Herança múltipla
class Smartphone(Dispositivo, Conectavel):
    def __init__(self, modelo):
        self.modelo = modelo

# Mixins são classes projetadas para adicionar funcionalidades específicas:

class LogMixin:
    def log(self, mensagem):
        print(f"LOG: {mensagem}")

class SerializableMixin:
    def serializar(self):
        return str(self.__dict__)

class Usuario(LogMixin, SerializableMixin):
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
    
    def salvar(self):
        self.log(f"Salvando usuário {self.nome}")
        return self.serializar()


# Properties permitem definir métodos que se comportam como atributos:

class Conta:
    def __init__(self):
        self._saldo = 0  # Convenção: atributo protegido
    
    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            raise ValueError("Saldo não pode ser negativo")
        self._saldo = valor
    
    @property
    def saldo_com_bonus(self):
        return self._saldo * 1.1

# Uso
conta = Conta()
conta.saldo = 100  # Usa setter
print(conta.saldo)  # Usa getter, mostra 100
print(conta.saldo_com_bonus)  # Mostra 110.0

# Decorators são funções que modificam o comportamento de outras funções ou métodos:

def log_chamada(func):
    def wrapper(*args, **kwargs):
        print(f"Chamando {func.__name__}")
        resultado = func(*args, **kwargs)
        print(f"Finalizado {func.__name__}")
        return resultado
    return wrapper

class API:
    @log_chamada
    def buscar_dados(self):
        print("Buscando dados...")
        return {"status": "ok"}

# ABCs permitem definir interfaces e classes abstratas em Python:

from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimetro(self):
        pass
    
    def descricao(self):
        return "Esta é uma forma geométrica"

class Retangulo(FormaGeometrica):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    
    def area(self):
        return self.largura * self.altura
    
    def perimetro(self):
        return 2 * (self.largura + self.altura)

# Uso
# forma = FormaGeometrica()  # Erro - não pode instanciar classe abstrata
retangulo = Retangulo(10, 5)
print(retangulo.area())  # 50
print(retangulo.descricao())  # "Esta é uma forma geométrica"
