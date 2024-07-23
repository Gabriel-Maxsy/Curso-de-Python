# Faça uma função que dobre os números de uma lista e retorne os números dobrados em uma nova lista

lista = [2, 3, 4, 5]

def dobrar(lista):
    lista_nova = []
    for numero in lista:
        lista_nova.append(numero * 2)

    return lista_nova

print(dobrar(lista))