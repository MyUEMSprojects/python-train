# 1. Perfilamento (Profiling)

# a. cProfile:
import cProfile


def funcao_lenta():
    # Código a ser analisado
    ...

cProfile.run('funcao_lenta()')


# b. line_profiler (para detalhamento por linha):
@profile
def funcao_alvo():
    # Código a ser analisado
    ...

# 2. Otimizações Comprovadas
# a. Use estruturas de dados adequadas:
# Busca rápida
elementos = {'a': 1, 'b': 2}  # dict O(1)

# Contagens
# Manter ordem
from collections import Counter, OrderedDict

# b. Evite cópias desnecessárias:
# Não otimizado
new_list = list(original_list)  # Cópia explícita

# Otimizado
for item in original_list:  # Iteração direta
    process(item)

# 3. Cython para Partes Críticas
# Exemplo de integração Cython:
# modulo_rapido.pyx
def calculo_intensivo(int n):
    cdef int i, resultado = 0
    for i in range(n):
        resultado += i * i
    return resultado

from Cython.Build import cythonize
# Setup.py:
from setuptools import setup

setup(ext_modules=cythonize("modulo_rapido.pyx"))

# 4. Multiprocessing para CPU-bound
from multiprocessing import Pool


def process_chunk(chunk):
    return sum(x*x for x in chunk)

def parallel_sum(numbers, chunksize=1000):
    with Pool() as pool:
        chunks = [numbers[i:i+chunksize] 
                 for i in range(0, len(numbers), chunksize)]
        return sum(pool.map(process_chunk, chunks))

# Caso Real: Sistema de Processamento de Dados

from concurrent.futures import ThreadPoolExecutor
# Versão Pythonica + Otimizada
from dataclasses import dataclass
from typing import Iterable, List

import numpy as np


@dataclass
class DataPoint:
    timestamp: float
    values: List[float]

class DataProcessor:
    def __init__(self, max_workers: int = 4):
        self.max_workers = max_workers
    
    def _process_single(self, point: DataPoint) -> float:
        """Processa um único ponto de dados"""
        return np.mean(point.values) * np.log(point.timestamp)
    
    def process_batch(self, points: Iterable[DataPoint]) -> List[float]:
        """Processa lote de dados em paralelo"""
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            results = list(executor.map(self._process_single, points))
        return results
    
    def optimized_analysis(self, points: List[DataPoint]) -> np.ndarray:
        """Versão otimizada com numpy para grandes datasets"""
        timestamps = np.array([p.timestamp for p in points])
        values = np.vstack([p.values for p in points])
        return np.mean(values, axis=1) * np.log(timestamps)

# Exercício Prático
# Parte 1 (Python Idiomático):
# Refatore este código para ser mais pythonico:
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError("Name must be a string")


# Parte 2 (Otimização):
# Otimize esta função usando numpy:
def calculate_distances(points):
    distances = []
    n = len(points)
    for i in range(n):
        for j in range(i+1, n):
            dist = ((points[i][0]-points[j][0])**2 + 
                   (points[i][1]-points[j][1])**2)**0.5
            distances.append(dist)
    return distances

# Soluções:
# Parte 1 (Pythonico):
class User:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        self._name = value

# Parte 2 (Otimizado):
import numpy as np


def calculate_distances(points):
    pts = np.array(points)
    diff = pts[:, np.newaxis, :] - pts[np.newaxis, :, :]
    distances = np.sqrt((diff**2).sum(axis=-1))
    return distances[np.triu_indices_from(distances, k=1)].tolist()


