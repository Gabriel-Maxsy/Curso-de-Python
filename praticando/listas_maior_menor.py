lista = [1, 2, 3, 4, 5, 6, 5, 6, 1, 4, 9, 3, 1, 12, 54, 23, 12, 31]

def maior_numero(lista):
    maior_numero = 0

    for numero in lista:
        
        if numero > maior_numero:
            
            maior_numero = numero  
    print('O maior número é:', maior_numero)

maior_numero(lista)