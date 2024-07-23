"""
Higher Order Functions
Funções de prmeira classe
"""

def saudacao (msg, nome):
    return f'{msg}, {nome}!'

def executa(funcao, *args):
    return funcao(*args)

print(
    executa(saudacao, 'Bom dia', 'Gabriel')
)