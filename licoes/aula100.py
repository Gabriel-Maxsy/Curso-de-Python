# Solução simplificada do professor: (não consegui fazer..)

# import copy

# produtos = [
#     {'nome': 'Produto 5', 'preco': 10.00},
#     {'nome': 'Produto 1', 'preco': 22.32},
#     {'nome': 'Produto 3', 'preco': 10.11},
#     {'nome': 'Produto 2', 'preco': 105.87},
#     {'nome': 'Produto 4', 'preco': 69.90},
# ]

# # Criar uma cópia profunda dos produtos
# produtos_copia = copy.deepcopy(produtos)

# # Aplicar aumento de preço em 10%
# novos_produtos = []
# for linhas in produtos_copia:
#     novo_produto = linhas.copy()
#     novo_produto['preco'] = round(novo_produto['preco'] * 1.1, 2)
#     novos_produtos.append(novo_produto)

# # Ordenar os produtos por nome em ordem decrescente
# produtos_ordenados_por_nome = copy.deepcopy(novos_produtos)
# produtos_ordenados_por_nome.sort(key=lambda p: p['nome'], reverse=True)

# # Ordenar os produtos por preço em ordem crescente
# produtos_ordenados_por_preco = copy.deepcopy(produtos_ordenados_por_nome)
# produtos_ordenados_por_preco.sort(key=lambda p: p['preco'])

# # Imprimir os produtos
# print(*produtos, sep='\n')
# print()
# print(*novos_produtos, sep='\n')
# print()
# print(*produtos_ordenados_por_nome, sep='\n')
# print()
# print(*produtos_ordenados_por_preco, sep='\n')

# Solução do professor:

import copy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

novos_produtos = [
    {**p, 'preco': round(p['preco'] * 1.1, 2)}
    for p in copy.deepcopy(produtos)
]

# # print(*produtos, sep='\n')
# # print()
# # print(*novos_produtos, sep='\n')

# # Ordene os produtos por nome decrescente (do maior para menor)
# # Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
# produtos_ordenados_por_nome = sorted(
#     copy.deepcopy(produtos),
#     key=lambda p: p['nome'],
#     reverse=True
# )
# # print(*produtos, sep='\n')
# # print()
# # print(*produtos_ordenados_por_nome, sep='\n')


# # Ordene os produtos por preco crescente (do menor para maior)
# # Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
# produtos_ordenados_por_preco = sorted(
#     copy.deepcopy(produtos),
#     key=lambda p: p['preco']
# )

# # FINAL

# print(*produtos, sep='\n')
# print()
# print(*novos_produtos, sep='\n')
# print()
# print(*produtos_ordenados_por_nome, sep='\n')
# print()
# print(*produtos_ordenados_por_preco, sep='\n')
