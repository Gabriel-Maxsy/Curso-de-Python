"""
Creat, Read, Update, Delete (CRUD)

"""

lista = [10, 20, 30, 40, 50]
lista[2] = 403
del lista[2]
print(lista)
print(lista[2])
lista.append(60)
lista.pop() # Deleta o ultimo valor da lista (nesse caso 60).
lista.append(70) # Aqui adicionou o 70.
lista.append(80)
lista.pop(5) # Remove o indice 5 da lista
print(lista)
