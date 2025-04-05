# namedtuples permitem criar tuplas com campos nomeados

from collections import namedtuple

#  Definição
Pessoa = namedtuple('Pessoa', ['nome', 'idade', 'profissao'])

# Criação
joao = Pessoa('João', 30, 'Engenheiro')
print(joao.nome) # João
print(joao[0])   # João (também funciona como tupla)


from dataclasses import dataclass

@dataclass
class Produto:
    nome: str
    preco: float
    estoque: int=0

    def valor_total(self):
        return self.preco * self.estoque

# Uso
notebook = Produto("Notebook", 3500.0, 5)
print(notebook) # Produto(nome='Notebook', preco=3500.0, estoque=5)
print(notebook.valor_total())


