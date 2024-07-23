"""
Fromatação básica de strings
s - string
d - int
f - float
.<número de digito>f
x ou X - Hexadecimal
(caractere)(><^)(quantidade)
> -> esquerda
< -> direita
^ -> centro
= - Força o número aparecer antes dos zeros
sinal -> + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a

"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: >10}')
print(f'{1000.02483129481248:0=+10,.2f}')
print(f'O hexadecimal de 1500 é {1500:08x}')
print(f'{variavel!r}')