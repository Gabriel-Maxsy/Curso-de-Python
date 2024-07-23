""" Calculadora com while"""

while True:
    
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite um operador (+ - / *): ')
    numeros_validos = None

    try:
        numero_1 = float(numero_1)
        numero_2 = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos números digitados são invalidos')
        continue

    operadores_validos = '+-/*'

    if operador not in operadores_validos:
        print('Operador invalido,')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    if operador == '+':
        print(f'{numero_1} + {numero_2} = {numero_1 + numero_2}')
    elif operador == '-':
        print(f'{numero_1} - {numero_2} = {numero_1 - numero_2}')
    elif operador == '*':
        print(f'{numero_1} * {numero_2} = {numero_1 * numero_2}')
    else:
        print(f'{numero_1} / {numero_2} = {numero_1 / numero_2}')

    sair = input('Você quer sair? sim - não: ').lower().startswith('s')

    if sair is True:
        break