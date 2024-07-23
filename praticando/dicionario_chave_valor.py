# Escreva uma função que receba um dicionário, 
# uma chave e um valor. Adicione o par chave-valor
# ao dicionário e retorne o dicionário atualizado.

dicionario = {}

def adicionar_chave_valor(dicionario, chave, valor):
    
    if chave and valor:
        dicionario[chave] = valor

    return dicionario

adicionar_chave_valor(dicionario, 'nome1', 'Gabriel')
adicionar_chave_valor(dicionario, 'nome2', 'teste')
adicionar_chave_valor(dicionario, 'nome3', 'Teste')
adicionar_chave_valor(dicionario, 'nome4', 'Yasmin')

for chave, valor in dicionario.items():
    print(chave, valor)

print(dicionario.items())