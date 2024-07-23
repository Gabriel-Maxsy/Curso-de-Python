lista = [[1, 2, 3, 4, 5, 6],]

def soma_lista(lista):
    
    for listas in lista:
        soma = 0
        for numeros in listas:
            print(f'{soma} + {numeros} = {soma + numeros}')
            soma += numeros
        