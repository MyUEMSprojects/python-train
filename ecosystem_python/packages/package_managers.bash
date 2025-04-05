# Se você vem de C++, pode comparar os gerenciadores de pacotes Python com:
# - pip ≈ vcpkg/conan (gerenciador de pacotes central)
# - poetry ≈ cargo (Rust) ou npm (mais completo)
# - conda ≈ gestor de ambientes com binários pré-compilados

# Instalar pacote
pip install numpy

# Instalar versão específica
pip install django==4.2

# Requisitos em arquivo (similar a CMakeLists.txt)
pip install -r requirements.txt

# Listar pacotes instalados
pip list

# Congelar dependências (gerar requirements.txt)
pip freeze > requirements.txt

# Boas praticas:
# - Sempre usar ambientes virtuais
# - python -m pip install (melhor que apenas pip install)
# - Atualizar pip regularmente: python -m pip install --upgrade pip

#  2. poetry (Gestão Moderna de Dependências)
# Para projetos sérios (equivalente a package.json + virtualenv):
# Iniciar novo projeto
poetry new meu-projeto
cd meu-projeto

# Adicionar dependência (atualiza pyproject.toml automaticamente)
poetry add numpy pandas

# Adicionar dependência de desenvolvimento
poetry add --group dev pytest

# Instalar todas as dependências
poetry install

# Ativar ambiente virtual
poetry shell

# Exportar para requirements.txt (para compatibilidade)
poetry export -f requirements.txt --output requirements.txt

# 3. conda (Para Ciência de Dados e Binários)
# Melhor para ambientes científicos com dependências não-Python:

# Criar ambiente
conda create -n meu-ambiente python=3.10

# Ativar ambiente
conda activate meu-ambiente

# Instalar pacotes (incluindo não-Python como CUDA)
conda install numpy pandas cudatoolkit

# Listar ambientes
conda env list

# Exportar ambiente
conda env export > environment.yml

# Quando usar conda:
# - Trabalhando com bibliotecas científicas (NumPy, SciPy, TensorFlow)
# - Precisando de dependências não-Python (compiladores, bibliotecas C)
# - Em sistemas onde compilar pacotes é problemático
#
