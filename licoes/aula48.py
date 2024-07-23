"""
Listas em python 
Tipo list - mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizaveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +

"""
#         01234
#        -54321
string = 'ABCDE' # 5 caracteres
#         0     1           2         3   4
#        -5    -4          -3        -2  -1       
lista = [123, True, 'Gabriel Maxsy', 1.2, []]

lista[2] = lista[2] + ' da Silva'
print(lista[2].lower(), type(lista[1]))