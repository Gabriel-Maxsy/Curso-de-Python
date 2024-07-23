# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5 indexs positivos
#  O t á v i o
# -6-5-4-3-2-1 index negativos

# nome = 'Otávio'

# print(nome[2])
# print(nome[-4])

# print('á' in nome)
# print('vio' in nome)
# print ('-' * 10)
# print('á' not in nome)
# print('vio' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que você quer encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não esta em {nome}')