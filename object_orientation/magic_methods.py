# Construção e iniciazalição
class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        print(f"Vector({self.x}, {self.y}) sendo destruido")


# Uso
v = Vector(1, 2)  # Chama __init__
del v  # Chama __del__ (mas nao confie para recursos criticos!)


# Representação do Objeto
class Vector:
    # ... __init__ como antes ...

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):
        return f"Vector(x={self.x}, y={self.y})"


v = Vector(3, 4)
print(v)  # Chama __str__: "Vector(3, 4)"
print(repr(v))  # Chama __repr__: "Vector(x=3, y=4)"


# Operadoras Matematicos
class Vector:
    # ... Métodos anteriores ...

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)  # Vector(4, 6)
print(v1 + 3)  # Vector(3, 6)


# Operadores de comparação
class Vector:
    # ... métodos anteriores ...

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))  # Para usar em conjuntos/dicionarios


v1 = Vector(1, 2)
v2 = Vector(1, 2)
print(v1 == v2)  # True


# Container Behavior
class MyCollection:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def __getitem__(self, index):
        return self._data[index]

    def __setitem__(self, index, value):
        self._data[index] = value

    def __contains__(self, value):
        return value in self._data


coll = MyCollection()
coll[0] = 10  # Chama __setitem__
print(10 in coll)  # Chama __contains__


# Callable Objects
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return x * self.factor


double = Multiplier(2)
print(double(5))  # 10 - Chama __call__


# Técnicas avançadas
# Context Managers
class FileHandler:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        # Trata exceções se necessário
        return False


# Uso (similar a RAII em C++)
with FileHandler("test.txt", "w") as f:
    f.write("Hello")


# Descriptors
class PositiveNumber:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, objtype):
        return obj.__dict__[self.name]

    def __set__(self, obj, value):
        if value <= 0:
            raise ValueError("Positive number required")
        obj.__dict__[self.name] = value


class BankAccount:
    balance = PositiveNumber()  # Descriptor

    def __init__(self, balance):
        self.balance = balance  # Usa __set__


account = BankAccount(100)
account.balance = -50  # ValueError!


# Implemente uma classe Matrix que:
# - Suporte inicialização com lista de listas
# - implemente __add__ para soma de matrizes
# - implemente __mul__ para multiplicação por escalar e por outra matriz
# - implemente __getitem__ para acesso com matrix[i][j]
# - implemente __str__ para impressão bonita
#
class Matrix:
    def __init__(self, data):
        self.data = data

    # Implemente os magic methods aqui


# Teste
m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[5, 6], [7, 8]])
print(m1 + m2)
print(m1 * 2)
print(m1 * m2)
print(m1[1][0])
