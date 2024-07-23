# Dictionary Comprehension e Set Comprehension
produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}

dc = {
    chave: valor.upper() # Mostre chave e valor maiusculos
    if isinstance(valor, str) else valor # Verifica se o 'valor' é string (isinstance)
    for chave, valor
    in produto.items()  # Para cada chave e valor (volte a linha 9)
    if chave != 'categoria' # Isto é um filtro que diz que se for diferente de categoria, mostre (ou seja não mostra a categoria)
}

lista = [
    ('a', 'valor a'),
    ('b', 'valor a'),
    ('b', 'valor a'),
]
dc = {
    chave: valor # Mostre chave e valor
    for chave, valor in lista # Exemplo com 'dicionario'
}

s1 = {2 ** i for i in range(10)} # Exemplo com 'set' (estudar mais sobre set não me recordo bem)
print(s1)