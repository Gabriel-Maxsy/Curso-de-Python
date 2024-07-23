"""
Interpolação básica de strings com %
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""

nome = 'Luis'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)
# variavel = f'{nome}, o preço é R${preco:.2f}'    /// Este codigo tbm funcionou mas o professor não mostrou não sei porquê
print(variavel)
print('O hexadecimal de %d é %x' % (15, 15))