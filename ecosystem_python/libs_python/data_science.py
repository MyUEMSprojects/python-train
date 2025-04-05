# numpy (Arrays multidimensionais)
import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.linalg.inv(a)  # Inversa matricial

# Equivalente C++: Eigen, Armadillo (mas com sintaxe Pythonica)

# pandas (Manipulação de dados)
import pandas as pd

df = pd.read_csv("data.csv")
print(df.groupby("category").mean())

# Analogia: Excel programático + SQL-like operations
