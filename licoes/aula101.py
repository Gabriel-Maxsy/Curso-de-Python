# Exercício - Adiando execução de funções

# def soma(x):
#     def somar(y):
#         return y + x
#     return somar



# def multiplica(x):
#     def multiplicar(y):
#         return y * x
#     return multiplicar


# def criar_funcao(funcao, *args):
#     return funcao(*args)


# soma_com_cinco = criar_funcao(soma, 5)
# multiplica_por_dez = criar_funcao(multiplica, 10)

# print(soma_com_cinco(4))
# print(multiplica_por_dez(4))

# Solução do rofessor:

def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y


def criar_funcao(funcao, x):
    def interna(y):
        return funcao(x, y)
    return interna


soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_dez = criar_funcao(multiplica, 10)

print(soma_com_cinco(10))
print(multiplica_por_dez(10))