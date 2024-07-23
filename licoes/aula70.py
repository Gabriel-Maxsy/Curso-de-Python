"""
Retorno de valores das funções (return)
"""

def soma (x, y):
    if x > 10:
        return [10, 20] # Nosso return pode retornar qualquer valor que quisermos

    return x + y

soma1 = soma (2, 2)
soma2 = soma (3, 3)

print(soma(11, 20))
print(soma1)
print(soma2)