import json

CAMINHO_ARQUIVO = 'praticando/json_testes/users.json'

users = {
    'user_1': {'nome': 'usuario1', 'senha': 1223},
    'user_2': {'nome': 'usuario2', 'senha': 1262},
    'user_3': {'nome': 'usuario3', 'senha': 1243},
    'user_4': {'nome': 'usuario4', 'senha': 1234},
    'user_5': {'nome': 'usuario5', 'senha': 1252},
    'user_6': {'nome': 'usuario6', 'senha': 1253},
    'user_7': {'nome': 'usuario7', 'senha': 1255},
}

with open(CAMINHO_ARQUIVO, 'w', encoding='utf8') as arquivo:
    json.dump(
        users,
        arquivo,
        ensure_ascii= False,
        indent=2
    )