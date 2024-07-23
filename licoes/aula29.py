"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""
numero = input('Vou dobrar o número que você digitar: ')
# print(f'O dobro de {numero} é {float(numero) * 2:.2f}')

try:
    numero_float = float(numero)
    print(f'Float: {numero_float}')
    print(f'O dobro de {numero} é {numero_float * 2}')
except:
    print('Isso não é um número!')
