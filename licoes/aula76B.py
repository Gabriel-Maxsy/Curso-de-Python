# Manipulando chaves e valores em dicionários

pessoa = {}

chave = 'nome'

pessoa[chave] = 'Gabriel'
pessoa['sobrenome'] = 'Maxsy da Silva'

print(pessoa[chave])
pessoa[chave] = 'Pedro'

del pessoa['sobrenome']

print(pessoa)
print(pessoa['nome'])

if pessoa.get('sobrenome') is None:
    print('Não existe')
else:
    print(pessoa['sobrenome'])