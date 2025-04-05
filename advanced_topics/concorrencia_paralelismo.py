# Se você vem de C++, entenderá os conceitos de threads e processos,
# mas Python tem abordagens específicas que vale a pena dominar.
# Vamos comparar as três principais abordagens:

# 1. Threading (Concorrência I/O-bound)
# Quando usar: Operações limitadas por I/O (rede, arquivos, etc.)

import threading

import requests


def download(url):
    response = requests.get(url)
    print(f"Baixado {url} - {len(response.content)} bytes")


urls = ["https://example.com", "https://example.org", "https://example.net"]

# Cria uma thread para cada URL
threads = []
for url in urls:
    t = threading.Thread(target=download, args=(url,))
    t.start()
    threads.append(t)

# Espera todas as threads terminarem
for t in threads:
    t.join()

# Comparação com C++
# - Similar a std::thread
# - GIL (Global Interpreter Lock)
# - Melhor para I/O, não para CPU-bond

# 2. Multiprocessing (Paralelismo CPU-bound)
# Quando usar: Processamento intensivo de CPU

import math
import multiprocessing


def calcular_fatorial(n):
    print(f"{n}! = {math.factorial(n)}")


numeros = [150000, 160000, 170000]

if __name__ == "__main__":
    processos = []
    for num in numeros:
        p = multiprocessing.Process(target=calcular_fatorial, args=(num,))
        p.start()
        processos.append(p)

    for p in processos:
        p.join()

# Comparação com C++:
# - Similar a fork() + processos independentes
# - cada processo tem seu próprio GIL
# - custa mais para criar que threads
# - comunicação via IPC(pipes, queues)

# 3. Asyncio (Programação Assíncrona)
# Quando usar: I/O bound com muitas conexões simultâneas

import asyncio

import aiohttp


async def download(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            content = await response.read()
            print(f"Baixado {url} - {len(content)} bytes")


async def main():
    urls = ["https://example.com", "https://example.org", "https://example.net"]
    tasks = [download(url) for url in urls]
    await asyncio.gather(*tasks)


asyncio.run(main())

import urllib.request

# Padrões avançados
# 1. ThreadPoolExecutor (Padrão similar a C++)
from concurrent.futures import ThreadPoolExecutor


def download(url):
    with urllib.request.urlopen(url) as response:
        return response.read()


with ThreadPoolExecutor(max_workers=5) as executor:
    futures = [executor.submit(download, url) for url in urls]
    results = [f.result() for f in futures]

# 2. ProcessPoolExecutor para CPU-bound
from concurrent.futures import ProcessPoolExecutor


def calcular(n):
    return math.factorial(n)


with ProcessPoolExecutor() as executor:
    results = list(executor.map(calcular, range(100, 110)))


# 3. Asyncio com Tasks
async def monitorar_tarefas():
    tarefa1 = asyncio.create_task(download("https://example.com"))
    tarefa2 = asyncio.create_task(download("https://example.org"))

    await tarefa1
    await tarefa2


# Casos reais
# 1. Web Scraper Concorrente
import concurrent.futures

import requests
from bs4 import BeautifulSoup


def scrape(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup.title.string


urls = [f"https://example.com/page/{i}" for i in range(1, 10)]

# Usando ThreadPool para I/O bound
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    futures = {executor.submit(scrape, url): url for url in urls}
    for future in concurrent.futures.as_completed(futures):
        url = futures[future]
        try:
            title = future.result()
            print(f"{url}: {title}")
        except Exception as e:
            print(f"Erro em {url}: {e}")

# 2. Processamento de Imagens Paralelo
from multiprocessing import Pool

from PIL import Image, ImageFilter


def process_image(image_path):
    with Image.open(image_path) as img:
        img = img.filter(ImageFilter.GaussianBlur(radius=2))
        output_path = f"processed_{image_path}"
        img.save(output_path)
    return output_path


if __name__ == "__main__":
    images = ["photo1.jpg", "photo2.jpg", "photo3.jpg"]
    with Pool(processes=len(images)) as pool:
        results = pool.map(process_image, images)
    print(f"Imagens processadas: {results}")

# Exercício Prático

# Implemente um sistema que:
# - Use threading para buscar dados de APIs simultaneamente
# - Use multiprocessing para processar os dados recebidos
# - Use asyncio para monitorar o progresso

import asyncio
import json
import multiprocessing
import threading

import requests

# Implemente:
# 1. Função para buscar dados (threading)
# 2. Função para processar dados (multiprocessing)
# 3. Função assíncrona para monitorar progresso
# 4. Coordene tudo em uma função main()


def main():
    urls = ["https://api.example.com/data/1", "https://api.example.com/data/2"]

    # Implementação aqui
    pass


if __name__ == "__main__":
    main()
