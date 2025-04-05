# Generator function usuando yield
# Generators são iteradores que geram valores sob demanda, economizando memória:
def contagem(maximo):
    contador = 0
    while contador < maximo:
        yield contador
        contador += 1


# Uso
for numero in contagem(5):
    print(numero) # 0, 1, 2, 3, 4


# Generators expression (como list comprehension, mas com parenteses)
quadrados = (x**2 for x in range(1000000)) # Não aloca memória para todos os valores

# Generators são ideias para processar grandes volumes de dados ou sequencias infinitas

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Primeiros 10 números de Fibonacci
fib = fibonacci()
for _ in range(10):
    print(next(fib)) # 0, 1, 1 , 2, 3, 5, 8, 13, 21, 34
