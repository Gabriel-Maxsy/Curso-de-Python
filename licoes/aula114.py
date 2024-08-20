# Funções recursivas e recursividade
# - funções que podem se chamar de volta
# - úteis p/ dividir problemas grandes em partes menores
# Toda função recursiva deve ter:
# - Um problema que possa ser dividido em partes menores
# - Um caso recursivo que resolve o pequeno problema
# - Um caso base que para a recursão
# - fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120
# https://brasilescola.uol.com.br/matematica/fatorial.html

# import sys
# sys.setrecursionlimit(1004) Você pode quebrar o limite das 
# funções recursivas com o sys

# Função exemplo de contagem 
# def recursiva(inicio=0, fim=4):
#     print(inicio,fim)

#     # caso base:
#     if inicio >= fim:
#         return fim

#     inicio += 1
#     return recursiva(inicio, fim)

# print(recursiva())

# Função exemplo de fatoriais (conta matematica):
def factorial(n):

    if n <= 1:
        return 1
    
    return n * factorial(n - 1)

print(factorial(5))