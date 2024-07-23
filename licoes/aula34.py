"""
Repetições
While (enquanto)
Executa uma ação enquanto uma ação for verdadeira
"""

condicao = True

while condicao:
    nome = input('Seu nome: ')
    print(nome)

    if nome == 'sair':
        break

print('teste')