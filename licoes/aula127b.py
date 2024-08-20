# import json
# # Este arquivo é para carregar os dados
# CAMINHO_ARQUIVO = 'aula127.json'
# with open(CAMINHO_ARQUIVO, 'r', encoding='utf8') as arquivo:
#     p1 = json.load(arquivo)

# print(type(p1))

# Solução do professor:

import json

from aula127a import CAMINHO_ARQUIVO, Pessoa, fazer_dump

# fazer_dump()

with open(CAMINHO_ARQUIVO, 'r', encoding='utf8') as arquivo:
    pessoas = json.load(arquivo)
    p1 = dict(**pessoas[0])
    p2 = Pessoa(**pessoas[1])
    p3 = Pessoa(**pessoas[2])

print(p1['nome'], p1.keys())
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)