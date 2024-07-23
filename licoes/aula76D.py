# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

import copy

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],
}

d2 = d1.copy() # Esta é a copia raza, ela não copia as coisas internas do dicionario (listas por exemplo)
d2 = copy.deepcopy(d1) # Esta é a copia profunda, somente com o import funciona, e ela copia as listas e consegue modificalas

d2['c1'] = 1000
d2['l1'][1] = 99999

print(d1)
print(d2)