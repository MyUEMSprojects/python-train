# Decorators avançados
# Em C++ você usaria classes ou structs para manter estado, em Python podemos usar closures ou classes:


class ContadorChamadas:
    """Decorator que conta quantas vezes uma função foi chamada"""

    def __init__(self, func):
        self.func = func
        self.contagem = 0

    def __call__(self, *args, **kwargs):
        self.contagem += 1
        print(f"Chamada {self.contagem} para {self.func.__name__}")
        return self.func(*args, **kwargs)


@ContadorChamadas
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(5))  # Mostra o contador para cada chamada recursiva


# Decorators com parametros
# Similar a templates com parametros em C++, mas mais dinamico
def repetir(num_vezes):
    """Decorator factory que recebe parâmetros"""

    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_vezes):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator


@repetir(num_vezes=3)
def cumprimentar(nome):
    print(f"Olá {nome}!")


cumprimentar("João")  # Imprime 3 vezes

# Decorators para métodos de classe
# Python diferencia entre funções e métodos, então precisamos tratar corretamente:


def decorator_metodo(func):
    def wrapper(self, *args, **kwargs):
        print(f"Chamando {func.__name__} em {self.__class__.__name__}")
        return func(self, *args, **kwargs)

    return wrapper


class MinhaClasse:
    @decorator_metodo
    def metodo(self):
        return "resultado"


obj = MinhaClasse()
obj.metodo()
