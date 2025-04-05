meu_dict = {"chave": "valor", "nome": "João", "idade": 30}

## std::unordered_map em c++
from collections import defaultdict}

# Não precisa verificar se a chave existe
d = defaultdict(int)
d["chave_inexistente"] += 1  # Automaticamente inicializa com 0

# Manipulação avançada(Python 3.9+)
# Merge de dicionarios (| operator)
d1 = {"a": 1}
d2 = {"b": 2}
merged = d1 | d2

# Update in-place (|=)
d1 |= d2

#  Dictionary  comprehensions (similar a list comprehensions)
quadrados = {x: x * x for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# views(Eficiencia de memória)
# Não criam cópias,, são "janelas"(ponteiros) para dos dados originais
chaves = meu_dict.keys()
valores = meu_dict.values()
itens = meu_dict.items()

# Unpacking (Python 3.5+)
d = {"a": 1, "b": 2, "c": 3}
foo(**d)  # Equivalente a foo(a=1, b=2, c=3)

# Sets - Conjuntos de Hash

# básico
meu_set = {1, 2, 3}

# Operações de conjunto
a = {1, 2, 3}
b = {3, 4, 5}

# União
a | b  # {1, 2, 3, 4, 5}

# Intersecção
a & b  # {3}

# Diferenças
a - b  # {1, 2}

# Diferenças simétrica (XOR)
a ^ b  # {1, 2, 4, 5}

# Set comprehensions
chars = {c for c in "abracadabra" if c not in "abc"}
# {'d', 'r'}

# FrozenSet - Conjunto imutável
fs = frozenset([1, 2, 3])
# Util para usar como chave em dicionarios

## Técnicas avançadas(Pythonicas)

# Memoization com dicionarios
def fib(n, cache={0: 0, 1: 1}):
    if n not in cache:
        cache[n] = fib(n-1) + fib(n-2)
    return cache[n]


# Contagem eficiente
from collections import Counter

contagem = Counter("abracadabra")
# Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})

# Dicionarios como registros
from types import SimpleNamespace

dados = {'nome': 'João', 'idade': 30}
obj = SimpleNamespace(**dados)
print(obj.nome) # João

# Set para remoção de duplicados
lista = [1, 2, 2, 3, 3, 3]
unicos = list(set(lista)) # [1, 2, 3]

# Perfomance considerations
# - Dicionarios e sets são O(1) para operações básicas (em média)
# - A partir do python 3.6, dicionarios usam menos memória
# - Sets são mais rapidos paraa membership tests que listas
#
