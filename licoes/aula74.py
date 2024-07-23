"""
Closure e funções que retornam outras funções
"""

def criar_saudacao(saudacao):
    def saudar(nome): # Adiando o uso do 'nome'
        return f'{saudacao}, {nome}!'
    return saudar # Adiando o 'sauda'

falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')

for nome in ['Maria', 'Pedro', 'Gabriel']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))
