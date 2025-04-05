# Para projetos novos:
poetry new projeto
cd projeto
poetry add pacote-principal
poetry add --group dev pytest black flake8

# para projetos existentes
git clone projeto-existente
cd projeto-existente
poetry install
poetry shell  # Ativa o ambiente

# Para colaboração
git clone projeto
cd projeto
conda env create -f environment.yml
conda activate projeto

# Dicas Avançadas
# 1. PIP com Requisitos Divididos

# requirements/
base.txt
dev.txt
prod.txt
test.txt

pip install -r requirements/dev.txt

# 2. poetry com Extras

# [tool.poetry.extras]
# ml = ["scikit-learn", "tensorflow"]
# dev = ["pytest", "ipython"]

poetry install --extras "ml dev"

# 3. conda + pip
## environment.yml
#channels:
#  - conda-forge
#dependencies:
#  - python=3.10
#  - numpy
#  - pip
#  - pip:
#    - torch==2.0.0

# Ferramentas Complementares
# 1 - pipx: Para instalar ferramentas CLI globais
pipipx install black
pipx run ruff check .px: Para instalar ferramentas CLI globais

# 2 - pdm: Alternativa moderna ao poetry
pdm init
pdm add numpy

# uv: Instalador ultra-rápido (em Rust)
uv pip install -r requirements.txt

# Exercício Prático
# 1 - Crie um novo projeto com poetry:
poetry new meu-app
cd meu-app

# 2 - Adicione dependências principais e de desenvolvimento:
poetry add requests
poetry add --group dev pytest

# 3 - Crie um arquivo "main.py" simples que use o pacote requests
# Exporte para requirements.txt:
poetry export -f requirements.txt --output requirements.txt

# Teste em um ambiente limpo:
python -m venv venv
source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
python main.py
