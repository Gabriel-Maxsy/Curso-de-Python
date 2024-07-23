# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# Resultado:
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

# Fiz um codigo enorme e quase consegui, no final pedi ajuda ao chat e percebi que era bem mais facil
# do que eu pensei.. adaptei pouca coisa do chat para o meu codigo (abaixo) em si:

lista_1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista_2 = ['BA', 'SP', 'MG', 'RJ']

def zipper(lista_1, lista_2):
    
    ab = []

    for i in range(len(lista_1)):
        
        tupla = (lista_1[i], lista_2[i])

        ab.append(tupla)
    
    return ab  

print(zipper(lista_1, lista_2))

# Solução do professor:
# 
# # def zipper(l1, l2):
#     intervalo = min(len(l1), len(l2))
#     return [(l1[i], l2[i]) for i in range(intervalo)]
# from itertools import zip_longest

# l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
# l2 = ['BA', 'SP', 'MG', 'RJ']
# print(list(zip(l1, l2)))
# print(list(zip_longest(l1, l2, fillvalue='SEM CIDADE'))) 