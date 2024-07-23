lista_a = [1, 2, 3]
print(lista_a)
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b) # Isso muda a nossa variavel 'lista_a', esta adicionando os valores da 'lista_b'
print(lista_c)
print(lista_a)