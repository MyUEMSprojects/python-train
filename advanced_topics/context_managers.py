# Se você vem de C++, pode pensar em context managers como uma versão mais poderosa
# e idiomática do padrão RAII (Resource Acquisition Is Initialization),
# mas com sintaxe dedicada (with) e maior flexibilidade.

# Conceito básico
# Context managers são objetos que definem métodos para entrar (__enter__)
# e sair (__exit__) de um contexto,
# garantindo que recursos sejam liberados corretamente.


# Implementação Clássica(Class)
class FileHandler:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        print(f"Abrindo arquivo {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Fechando arquivo {self.filename}")
        if self.file:
            self.file.close()

        # Se retornar True, suprime a exceção
        return False


# Uso
with FileHandler("exemplo.txt", "w") as f:
    f.write("Hello, world!")
    # Arquivo é fechado automaticamente, mesmo se ocorrer exceção


# Implementação com "contextlib" (Generator)
# Para casos mais simples, podemos usar o decorator "@contextmanager":

from contextlib import contextmanager


@contextmanager
def file_handler(filename, mode):
    print(f"Abrindo arquivo {filename}")
    file = open(filename, mode)
    try:
        yield file
    finally:
        print(f"Fechando arquivo {filename}")
        file.close()


# Uso
with file_handler("exemplo.txt", "w") as f:
    f.write("Hello again!")

# Casos de usos comuns


# Gerenciamento de conexões
class DatabaseConnection:
    def __enter__(self):
        self.conn = connect_to_database()
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
        if exc_type:
            print(f"Erro ocorreu: {exc_val}")
        return False


with DatabaseConnection() as conn:
    conn.execute_query("SELECT * FROM users")

# Temporizador
import time


class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, *args):
        self.end = time.perf_counter()
        self.elapsed = self.end - self.start
        print(f"Tempo decorrido: {self.elapsed:.6f} segundos")


with Timer():
    # Código a ser cronometrado
    sum(x * x for x in range(1_000_000))


# Transaction Management
class Transaction:
    def __init__(self, db):
        self.db = db

    def __enter__(self):
        self.db.begin()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.db.rollback()
        else:
            self.db.commit()


with Transaction(database):
    database.execute("UPDATE accounts SET balance = balance - 100 WHERE id = 1")
    database.execute("UPDATE accounts SET balance = balance + 100 WHERE id = 2")

# Ténicas Avançadas

# Multiplos context managers
with open("input.txt") as fin, open("output.txt", "w") as fout:
    fout.write(fin.read().upper())


# Context Mangaers Assincronos
class AsyncConnection:
    async def __aenter__(self):
        self.conn = await connect_to_db()
        return self.conn

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.conn.close()


async with AsyncConnection() as conn:
    await conn.execute("...")

# Redirecionamento de saida

import sys
from io import StringIO


class RedirectStdout:
    def __init__(self):
        self._stdout = None

    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = StringIO()
        return sys.stdout

    def __exit__(self, *args):
        sys.stdout = self._stdout


with RedirectStdout() as output:
    print("Isso vai para a memória")
    result = output.getvalue()

# Exemplo prático
# Implemente um context manager ChangeDirectory que:
# - Muda para um diretório especificado no __enter__
# - Retorna ao diretório original no __exit__
# - Lida com exceções apropriadamente

import os
from pathlib import Path


class ChangeDirectory:
    def __init__(self, new_path):
        self.new_path = Path(new_path).absolute()
        self.original_path = None

    def __enter__(self):
        # Implemente aqui
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Implemente aqui
        pass


# Teste
print("Antes:", os.getcwd())
with ChangeDirectory("/tmp"):
    print("Dentro:", os.getcwd())
print("Depois:", os.getcwd())
