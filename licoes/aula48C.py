"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3
#       -4  -3   -2 -1
lista = [10, 20, 30, 40]
lista.append('Luiz') # Adiciona um valor na lista
nome = lista.pop() # Apaga o ultimo valor (quando não passamos parâmetros).
lista.append(1233)
del lista[-1] # Deletou o ultimo elemento da lista (indice -1)
# lista.clear() clear limpa a lista inteira
lista.insert(4, 50) # O insert adiciona um valor no indice desejado (indice, valor) 
lista.insert(30, 60) # Se passarmos um indice maior do que a quantidade de itens, o valor vai no ultimo indice como se fosse um append (mas não é recomendado)  
print(lista)