"""
Introdução ás funções (def) em python
Funções são trechos de códfigo usados para
replicar determinada ação ao longo do seu codigo.
Elas podem receber valores para parâmetros (argumetnos)
e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
"""

def saudacao(nome):
    print(f'Olá, {nome}!', end=' ')
    print('Seja bem vindo!')

saudacao('Gabriel')

def soma(a, b):
    print(f'O número {a} somado com o número {b} é: {a + b}')

a = int(input('Número 1: '))
b = int(input('Número 2: '))
soma(a,b)

