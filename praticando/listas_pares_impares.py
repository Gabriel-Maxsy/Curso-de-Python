lista = [1, 2, 3, 4, 5, 6, 5, 6, 1, 4, 9, 3, 1, 12, 54, 23, 12, 31]

def impar_ou_par(lista):
    
    lista_par = []
    lista_impar = []

    for numero in lista:

        if numero % 2 == 0:
            lista_par.append(numero)
        else:
            lista_impar.append(numero)
    
    return lista_impar, lista_par

print(impar_ou_par(lista))