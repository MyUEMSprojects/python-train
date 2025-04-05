# Dicionarios e sets

# Criação básica
usuario = {"nome:", "Ana", "idade": 28, "ativo": True}


# Dict comprehension
quadrados = {x: x**2 for x in range(5)}


# Acesso e manipulação
print(usuario["nome"]) # Ana
usuario["email"] = "ana@examplo.com" # Adiciona nova chave


# Criação de set
frutas = {"maçã", "banana", "laranja"}

# Set comprehension
pares = {x for x in range(10) if x % 2 == 0}

# Operações de conjunto
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A | B) # União: {1, 2, 3, 4, 5, 6}
print(A & B) # Interseção: {3, 4}
print(A - B) # Diferença


