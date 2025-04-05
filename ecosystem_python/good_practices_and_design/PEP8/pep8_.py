# Espaçamento entre funções/classes (2 linhas)
def function_one():
    pass


def function_two():
    pass


# Espaçamento entre métodos (1 linha)
class MyClass:
    def method_one(self):
        pass

    def method_two(self):
        pass


# // C++ geralmente usa menos espaçamento
# class MyClass {
# public:
#    void methodOne() {...}
#    void methodTwo() {...}  // Apenas 1 linha
# };

# 3. Indentação e Quebra de Linha
# Alinhamento com delimitadores de abertura
result = some_function(arg1, arg2, arg3, arg4)

# Indentação adicional para distinguir argumentos
result = some_function(first_argument, second_argument, third_argument)

# Comparação C++:
# // Estilo similar pode ser usado em C++
# auto result = someFunction(
#    arg1, arg2,
#    arg3, arg4);

# 4. Imports
# Ordem: stdlib > third-party > local
import os
import sys
from typing import Dict, List

import numpy as np
import pandas as pd
from mypackage import mymodule

# Regras:

#    Um import por linha
#    Agrupar em seções (stdlib, third-party, local)
#    Evitar from module import *

# Diferenças Chave para Desenvolvedores C/C++

#    Chaves vs Indentação:

#        Python não usa {} para blocos
#        A indentação é a sintaxe

#    Ponto-e-vírgula:

#        Python: Nunca use ; no final das linhas
#        Exceto para múltiplos comandos na mesma linha (não recomendado)

#    Comparação com nullptr/NULL:
#        Python usa None (maiúsculo inicial)

#    Constantes:

#        Não existe const em Python
#        Convenção: UPPER_CASE para indicar constante

# Ferramentas para Verificação Automática

# 1. flake8 (Combina PEP 8 com análise estática)
pip install flake8
flake8 meu_script.py

# 2. black (Auto-formatter sem configurações)
pip install black
black meu_script.py  # Reformata automaticamente

# 3. pylint (Análise mais rigorosa)
pip install pylint
pylint meu_script.py

# Exemplo Completo PEP 8 Compliant
#!/usr/bin/env python3
"""Módulo de exemplo seguindo PEP 8."""

import os
from typing import List, Tuple

MAX_SIZE = 1024


class DataProcessor:
    """Classe que processa dados conforme especificação."""

    def __init__(self, input_file: str):
        self.input_file = input_file
        self._data = None

    def load_data(self) -> List[Tuple[str, int]]:
        """Carrega e processa os dados do arquivo.

        Returns:
            Lista de tuplas contendo (chave, valor).
        """
        if not os.path.exists(self.input_file):
            raise FileNotFoundError(f"Arquivo {self.input_file} não existe")

        with open(self.input_file) as file:
            self._data = [
                (line.split(",")[0], int(line.split(",")[1]))
                for line in file
                if line.strip()
            ]

        return self._data


def main():
    """Função principal."""
    processor = DataProcessor("data.csv")
    try:
        data = processor.load_data()
        print(f"Processados {len(data)} registros")
    except FileNotFoundError as e:
        print(f"Erro: {e}")


if __name__ == "__main__":
    main()


# Quando Violar o PEP 8?
#    Compatibilidade com código existente
#    Legibilidade em casos específicos
#    Restrições de ferramentas externas

# Mas sempre documente a razão:
# Nota: Violando PEP 8 para compatibilidade com API externa
result = some_call(argument1, argument2,
                 argument3, argument4)  # noqa: E131

# Exercício Prático
# Converta este trecho C++ para Python seguindo o PEP 8:
// C++ version
class DataAnalyzer {
public:
    DataAnalyzer(std::vector<double> data) : m_data(data) {}
    
    double calculateMean() const {
        if (m_data.empty()) return 0.0;
        double sum = std::accumulate(m_data.begin(), m_data.end(), 0.0);
        return sum / m_data.size();
    }

private:
    std::vector<double> m_data;
};

# Solução Python PEP 8 Compliant:
class DataAnalyzer:
    """Calcula estatísticas básicas sobre um conjunto de dados."""

    def __init__(self, data: list[float]):
        """Inicializa com os dados fornecidos.
        
        Args:
            data: Lista de valores numéricos.
        """
        self._data = data

    def calculate_mean(self) -> float:
        """Calcula a média aritmética dos dados.
        
        Returns:
            A média dos valores ou 0.0 para lista vazia.
        """
        if not self._data:
            return 0.0
        
        return sum(self._data) / len(self._data)
