# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplica (*args):
    total = 1
    for numeros in args:
        total *= numeros
    return total
    
print(1*2*3*4*5)
print(multiplica(1, 2, 3, 4, 5))

# Crie uma função que fala se um número é ímpar ou par
# Retorne se o número é ímpar ou par.

def impar_par(x):
    if x % 2 == 0:
        return print(f'{x} é par')
    
    return f'{x} é ímpar'

print(impar_par(7)) 