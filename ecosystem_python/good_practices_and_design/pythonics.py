# Ao migrar de C/C++ para Python, é essencial entender o que torna o código "pythonico"
# - um estilo que aproveita ao máximo as características únicas da linguagem.
# Veja as principais diferenças:
# 1. Iteração e Controle de Fluxo
# Evite loops estilo C/C++

# Não Pythonico (estilo C++):
for i in range(len(minha_lista)):
    print(minha_lista[i])

# Pythonico:
for elemento in minha_lista:
    print(elemento)

# Use enumerate para índices

# Não Pythonico:
i = 0
for item in minha_lista:
    print(i, item)
    i += 1

# Pythonico:
for i, item in enumerate(minha_lista):
    print(i, item)


# 2. Manipulação de Listas

# Compreensão de listas vs loops

# Não Pythonico:
quadrados = []
for x in range(10):
    quadrados.append(x**2)

# Pythonico:
quadrados = [x**2 for x in range(10)]

# Filtros com compreensão

# Não Pythonico:
resultado = []
for x in valores:
    if x > 0:
        resultado.append(math.sqrt(x))

# Pythonico:
resultado = [math.sqrt(x) for x in valores if x > 0]

# 3. Manipulação de Dicionários

# Iteração em pares chave-valor

# Não Pythonico:
for chave in meu_dict:
    print(chave, meu_dict[chave])

# Pythonico:
for chave, valor in meu_dict.items():
    print(chave, valor)

# Dicionários com valores padrão

# Não Pythonico:
if chave in meu_dict:
    valor = meu_dict[chave]
else:
    valor = padrao

# Pythonico:
valor = meu_dict.get(chave, padrao)

# 4. Tratamento de Recursos

# Gerenciamento de contexto (RAII em Python)

# Não Pythonico:
f = open('arquivo.txt')
try:
    dados = f.read()
finally:
    f.close()

# Pythonico:
with open('arquivo.txt') as f:
    dados = f.read()

# 5. Funções e Desempacotamento

# Retorno múltiplo de valores

# Não Pythonico:
def processa_dados(dados):
    # ...
    return (resultado, status)

tupla = processa_dados(dados)
resultado = tupla[0]
status = tupla[1]

# Pythonico:
def processa_dados(dados):
    # ...
    return resultado, status  # Tupla implícita

resultado, status = processa_dados(dados)  # Desempacotamento

# Argumentos arbitrários

# Não Pythonico:
def minha_funcao(*args):
    for i in range(len(args)):
        print(args[i])

# Pythonico:
def minha_funcao(*args):
    for arg in args:
        print(arg)

# 6. Orientação a Objetos
# Propriedades vs getters/setters

# Não Pythonico:
class Retangulo:
    def __init__(self):
        self._largura = 0
    
    def get_largura(self):
        return self._largura
    
    def set_largura(self, value):
        if value < 0:
            raise ValueError("Largura deve ser positiva")
        self._largura = value

# Pythonico:
class Retangulo:
    def __init__(self):
        self._largura = 0
    
    @property
    def largura(self):
        return self._largura
    
    @largura.setter
    def largura(self, value):
        if value < 0:
            raise ValueError("Largura deve ser positiva")
        self._largura = value

# 7. Comparações e Booleanos
# Teste de verdadeiro/falso

# Não Pythonico:
if len(minha_lista) > 0:
    pass

if valor == True:
    pass

# Pythonico:
if minha_lista:  # Lista não vazia
    pass

if valor:  # Valor é verdadeiro
    pass

# Operador ternário

# Não Pythonico:
if condicao:
    valor = 42
else:
    valor = 0

# Pythonico:
valor = 42 if condicao else 0

# 8. Módulos e Importação
# Organização de imports

import math
# Pythonico:
import os
# Não Pythonico:
import sys  # Múltiplos imports na mesma linha
from typing import Dict, List

import numpy as np
import pandas as pd
from meu_modulo import *  # Importação selvagem
from meu_modulo import funcao_especifica

# 9. Tratamento de Exceções
# Especifique exceções

# Não Pythonico:
try:
    # código
except:
    pass

# Pythonico:
try:
    # código
except ValueError as e:
    print(f"Erro de valor: {e}")
except (TypeError, IndexError):
    print("Erro de tipo ou índice")


# 10. _ vs __ em Nomes

#    Single underscore prefix (_var):
#        Convenção para indicar "interno" (mas ainda acessível)
#    Double underscore prefix (__var):
#        Name mangling (para evitar conflitos em herança)
#    Single underscore (_):
#        Nome descartável (como em for _ in range(10))

import csv
# Exemplo Completo Pythonico
from collections import defaultdict
from pathlib import Path


def processa_arquivos(diretorio, extensao=".csv"):
    """Processa todos os arquivos com extensão especificada no diretório.
    
    Args:
        diretorio: Caminho do diretório a ser processado
        extensao: Extensão dos arquivos a considerar
        
    Returns:
        Dicionário com contagem de linhas por arquivo
    """
    contador = defaultdict(int)
    
    for arquivo in Path(diretorio).glob(f"*{extensao}"):
        try:
            with arquivo.open(encoding='utf-8') as f:
                leitor = csv.reader(f)
                contador[arquivo.name] = sum(1 for _ in leitor)
        except (csv.Error, UnicodeDecodeError) as e:
            print(f"Erro processando {arquivo}: {e}")
    
    return dict(contador)

#Ferramentas para Manter o Código Pythonico

#    Linters:
#        flake8 (combina PEP 8, pyflakes e complexity checks)
#        pylint (análise mais rigorosa)
#    Formatters:
#        black (formatação automática sem discussões de estilo)
#        isort (organização automática de imports)
#    Type Checkers:
#        mypy (verificação estática de tipos)

# Exercício Prático

# Converta este código estilo C++ para Python idiomático:

# Código não-pythonico (estilo C++)
def calcular_estatisticas(numeros):
    n = len(numeros)
    if n == 0:
        return (0, 0, 0)
    
    soma = 0.0
    for i in range(n):
        soma += numeros[i]
    media = soma / n
    
    variancia = 0.0
    for i in range(n):
        variancia += (numeros[i] - media) ** 2
    variancia /= n
    
    maximo = numeros[0]
    for i in range(1, n):
        if numeros[i] > maximo:
            maximo = numeros[i]
    
    return (media, variancia, maximo)

# Solução Pythonica:
import statistics


def calcular_estatisticas(numeros):
    if not numeros:
        return 0, 0, 0
    
    media = statistics.mean(numeros)
    variancia = statistics.variance(numeros, media) if len(numeros) > 1 else 0
    maximo = max(numeros)
    
    return media, variancia, maximo
