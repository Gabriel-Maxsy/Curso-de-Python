# lista = ['Gabriel', 'Evandro', 'Teste', 'Gabriel', 'Evandro', 'Teste']

# i = 0
# for nome in lista:
#     print(i, nome)
#     i += 1


# Solução do professor:

lista = ['Gabriel', 'Evandro', 'Teste', 'Gabriel', 'Evandro', 'Teste']

indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))