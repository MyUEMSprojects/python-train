# generators em python
# Corrotinas
# iteradores lazy (como ranges vie em C++20)
# O padrão "iterator" da STL, mas com implementação muito mais simples


# Conceito básico(C/C++ style):
def quadrado(n):
    resultado = []
    for i in range(n):
        resultado.append(i * i)
    return resultado


# Genertor function (Python way)
def quadrado_gen(n):
    for i in range(n):
        yield i * i  # Produz um valor de cada vez


# Como funciona internamente?
# - Quando voce chama a função, ela não executa imediatamente
# - Retorna um objeto generator (que é um iterator)
# - A cada chamada a next(), executa até o próximo yield
# - Mantém o estado entre chamada (stack frame suspenso)

gen = quadrado_gen(5)
print(next(gen))  # 0
print(next(gen))  # 1
print(next(gen))  # 2

# Vantagens sobre abordagens C/C++ like
# - Eficiencia de memória: Não alocaa tudo de uma vez
# - Lazy evaluation: calculo sob demanda
# - Pipelineing: Permite encadear operações
# - Estado implicito: Não precisa gerenciar manualmente como em iteradores C++


# Padrões avançados
# Pipeline de processamento (Similar a views em C++20)


def ler_arquivo(nome):
    with open(nome) as f:
        for linha in f:
            yield linha.strip()


def filtrar_vazias(linhas):
    for linha in linhas:
        if linha:
            yield linha


def numerar(linhas):
    for i, linha in enumerate(linhas, 1):
        yield f"{i}: {linha}"


# Encadeamento lazy
pipeline = numerar(filtrar_vazias(ler_arquivo("dados.txt")))
for item in pipeline:
    print(item)


# Corrotinas(via send())
def processador():
    total = 0
    while True:
        valor = yield  # Pausa para receber valor
        if valor is None:
            break
        total += valor
    return total


proc = processador()
next(proc)  # "Prime" o generator
proc.send(10)
proc.send(20)
try:
    proc.send(None)  # Finaliza
except StopIteration as e:
    print(f"Total: {e.value}")  # 30

# Expressões Geradores( Generator Expressions)

# Similar a list comprehension, mas lazy
gen_exp = (x * x for x in range(1000000))

# Equivalente C++20 (conceitual):
# auto gen_exp = std::views::iota(0, 1000000) | std::views::transform([](int x) { return x*x; });

# Casos de usos tipicos
#  1) Procesamento de grandes arquivos/dados
#      - Evita carregar tudo na memória
#      - Similar a memory-mapped files em C++
#  2) Streaming de dados
#       - Dados em tempo real (sensores, rede)
#       - Similar a callbacks, mas mais legivel

# Sequencias infinitas


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


# Maquinas de estado
#    - Cada "yield" age como um ponto de pausa
#    - Mais legivel que máquinas de estado manuais


# Técnicas avançadas
# Delegando para sub-generators(yield  from)
def chain(*iterables):
    for it in iterables:
        yield from it  # Similar a 'co_await' em C++


# Equivalente a std::ranges::join_view

# Context managers com generators
from contextlib import contextmanager


@contextmanager
def timer(nome):
    start = time.time()
    yield  # Código do bloco with executa aqui
    print(f"{nome} levou {time.time() - start:.2f}s")


# Uso
with timer("Processamento"):
    processar_dados()


# Async/await (Baseado no mesmo conteudo)
async def fetch_data():
    # yield "disfarçando" como await
    data = await some_io_operation()
    return data


# Perfomance considerations
#  1) Vantagens:
#      - Menor uso de memória (especialmente para grande datasets)
#      - Inicio mais rápido (não precisa pré-processar tudo)
#  2) Cuidados:
#      - Overhead de função generator vs loop direto
#      - Não reutilizavel (consumido uma vez)


# Implemente um generator batch que recebe um iterável e um tamanho de batch, produzindo sublistas:
def batch(iterable, n=1):
    # Sua implementação aqui
    ...


# Deve funcionar como:
for group in batch([1, 2, 3, 4, 5, 6, 7, 8], 3):
    print(group)
# [1, 2, 3]
# [4, 5, 6]
# [7, 8]
