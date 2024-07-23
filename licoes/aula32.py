"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero = input('Digite um número inteiro: ')

try:
    numero_int = int(numero)
    print(numero_int)

    if numero_int % 2 == 1:
        print('O número que você digitou é ímpar')
    else:
        print('O número que você digitou é par')
        
except:
    print('Você não digitou um número inteiro!')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
horario = input('Digite o horário [0-11], [12-17] ou [18-23]: ')

try:
    horario = float(horario)
    bom_dia = horario >= 0 and horario <= 11
    boa_tarde = horario >= 12 and horario <= 17
    boa_noite = horario >= 18 and horario <= 23

    if bom_dia:
        print('Bom dia')
    elif boa_tarde:
        print('Boa tarde')
    elif boa_noite:
        print('Boa noite')
except:
    print('Algo foi digitado de forma incorreta')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite o seu primeiro nome: ')

if len(nome) <= 4:
    print('Seu nome é curto')
elif len(nome) >= 5 and len(nome) <= 6:
    print('Seu nome é normal')
elif len(nome) > 6:
    print('Seu nome é muito grande')