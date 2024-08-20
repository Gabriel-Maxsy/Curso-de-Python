import json
c = 0
usuarios = []
CAMINHO_ARQUIVO = 'teste.json'

class User:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha

while c < 3:
    dados = []
    user_name = input('Nome: ')
    user_password = input('Senha: ')

    user_1 = User(user_name, user_password)
    for i, n in vars(user_1).items():
        dados += i, n
    usuarios += [dados]
    c += 1

with open(CAMINHO_ARQUIVO, 'w', encoding='utf8') as arquivo:
    json.dump(
        usuarios,
        arquivo,
        ensure_ascii = True,
        indent = 2
    )