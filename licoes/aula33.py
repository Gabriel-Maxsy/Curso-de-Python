"""
"Documentação do python"
Tipos Imutáveis que vimos: str, int, float, bool
"""

string = 'Gabriel Maxsy'
# Mudando a string usando outra váriavel, porque strings são imutaveis por si só
outra_variavel = f'{string[:3]}ABC{string[4:]}'

print(string)
print(outra_variavel)
print(string.zfill(100))