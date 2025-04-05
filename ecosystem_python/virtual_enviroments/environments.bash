#Se você vem de C++, pode pensar em virtual environments como:
# - Containers leves para projetos Python
# - Equivalente a "build directories" isolados
# - Similar ao conceito de workspaces em outras linguagens
#
# Por que usar Virtual Environments?
# - Isolamento de dependências: Cada projeto tem suas próprias bibliotecas
# - Controle de versões: Evita conflitos entre versões de pacotes
# - Reprodutibilidade: Garante que todos usem as mesmas versões
# - Segurança: Permite instalar pacotes sem privilégios de administrador
#

# Ferramentas Principais
# 1. venv (Built-in - Python 3.3+)
# Comandos básicos:
# Criar ambiente (similar a mkdir build && cd build)
python -m venv meu_ambiente

# Ativar (Linux/Mac)
source meu_ambiente/bin/activate

# Ativar (Windows)
meu_ambiente\Scripts\activate

# Desativar
deactivate

# Exemplo de workflow:# Criação
python -m venv projeto-api-env

# Ativação
source projeto-api-env/bin/activate  # Agora o prompt muda

# Instalação de pacotes
pip install flask pandas

# Congelar dependências
pip freeze > requirements.txt

# Desativar
deactivate

# 2. virtualenv (Alternativa mais antiga)
# Instalação
pip install virtualenv

# Uso
virtualenv meu_ambiente

# Diferenças para venv:
# - Funciona com versões mais antigas do Python
# - Mais configurável
# - Requer instalação adicional

# 3. Integrado com Ferramentas Modernas

# Com poetry:
poetry shell  # Cria e ativa automaticamente
# Com conda:
conda create -n meu-ambiente python=3.10
conda activate meu-ambiente

# Estrutura de Diretórios
# Um virtualenv típico contém:
meu_ambiente/
├── bin/           # Scripts (Linux/Mac)
│   ├── python     # Python interpreter
│   ├── pip        # Pip isolado
│   └── activate   # Script de ativação
├── Scripts/       # Scripts (Windows)
├── lib/           # Bibliotecas instaladas
└── pyvenv.cfg     # Configuração do ambiente

# Boas Práticas
#  1 - Nomes descritivos:
python -m venv projeto-api-env  # Bom
python -m venv venv            # Ruim (genérico)

#  2 - Não versionar o ambiente:
#      - Adicione meu_ambiente/ ao .gitignore

#  3 - Requisitos divididos:
requirements/
├── base.txt     # Dependências principais
├── dev.txt      # Ferramentas de desenvolvimento
└── test.txt     # Dependências de teste

#  4 - Ativação automática (para projetos):
#      - Use direnv ou scripts shell
#      - Ou configure seu IDE (VS Code/PyCharm)

# Dicas Avançadas
# 1. Customizando a instalação do Python
python -m venv --copies --prompt "MEU_PROJETO" meu_ambiente

#Opções úteis:
#    --copies: Usa cópias em vez de symlinks
#    --prompt: Customiza o prompt do terminal
#    --system-site-packages: Acessa pacotes globais (útil para pacotes grandes como TensorFlow)

# 2. Requirements com hashes (para segurança)
pip freeze --all --local | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 pip hash > requirements.txt

# 3. Virtualenv em containers Docker
FROM python:3.10-slim

# Criando e ativando o venv
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Instalando dependências
COPY requirements.txt .
RUN pip install -r requirements.txt

# Exercício Prático
# 1. Crie um virtualenv para um projeto:
python -m venv ~/environments/meu-projeto-env

# 2. Ative e instale alguns pacotes:
source ~/environments/meu-projeto-env/bin/activate
pip install requests pytest

# 3. Crie um arquivo requirements.txt:
pip freeze > requirements.txt

# 4. Desative e recrie o ambiente em outro diretório:
deactivate
python -m venv novo-env
source novo-env/bin/activate
pip install -r requirements.txt

# 5. Verifique as instalações:
pip list
python -c "import requests; print(requests.__version__)"


