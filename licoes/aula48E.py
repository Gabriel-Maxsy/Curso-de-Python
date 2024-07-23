"""
Cuidado com dados mutáveis
= - copiando o valor (imutaveis)
= - aponta para o mesmo valor na memória (mutável)
"""

lista_a = ['Gabriel', 'Yasmin', 1, True, 1.5]
lista_b = lista_a.copy() # Sem o 'copy()' no momento em que dou outro valor na lista a ela tbm muda na b mas com o copy não 

lista_a[0] = 'Qualquer outra coisa'

print(lista_a)
print(lista_b)