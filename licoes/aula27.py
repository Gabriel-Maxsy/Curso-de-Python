"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
obs.: a função len retorna a quantidade
de caracteres da string
"""

variavel = 'Olá mundo'
print(variavel[4:9])
print(variavel[:3]) # Ocultando o indice 0
print(variavel[-9:-3])
print(len(variavel))
print(len(variavel[:-5]))
print(variavel[0:9:1]) # O ultimo é a quantidade de passos que ele irá tomar, nesse caso 1 em um
print(variavel[0:9:2])
print((variavel[::-1])) # De um em um invertido


# print(variavel[-5])