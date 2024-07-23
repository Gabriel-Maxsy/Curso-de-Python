"""
Iterando strings com while
"""
#       0123456789...

nome = 'Yasmin Pires Fuentes' # strings são iteráveis
contador = 0
novo_nome = ''

while contador < len(nome):
    letra = nome[contador]
    
    novo_nome += f'*{letra}'
    
    contador += 1

novo_nome += '*'
print(novo_nome)