# 1. Setup inicial:
poetry new projeto
cd projeto
poetry add numpy pandas matplotlib
# 2. Desenvolvimento:
import pandas as pd
from sklearn.linear_model import LinearRegression

# Análise de dados e ML

# 3. Testes:
poetry add --group dev pytest
pytest tests/

# 4. Empacotamento:
poetry build
