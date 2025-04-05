# Ao inves de:
numeros_pares = []

for i in range(10):
    if i % 2 == 0:
        numeros_pares.append(i)

# Use list comprehension:
numeros_pares = [i for i in range(10) if i % 2 == 0]

# List comprehension com expressão
quadrados = [x**2 for x in range(10)]

# List comprehension com multiplos condições
numeros = [x for x in range(100) if x % 2 == 0 if x % 5 == 0]
