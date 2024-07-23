texto = 'python'
novo_texto = ''

for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)

print(f'{novo_texto}*')