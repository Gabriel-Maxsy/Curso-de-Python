## Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos
from itertools import combinations, permutations, product

def print_iter(iterador):
    print(*list(iterador), sep='\n')
    print()

pessoas = [
    'João', 'Gabriel', 'Luiz', 'Otavio'
]

camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino'],
    ['Algodão', 'Peruano']
]

print_iter(combinations(pessoas, 2)) # Faz as combinações sem repetir grupos (não repetir algo como "João", "Gabriel" e em seguida "Gabriel", "João")
print_iter(permutations(pessoas, 2)) # Faz esse tipo de combinação 
print_iter(product(*camisetas)) # Faz todas as combinações possiveis em ordem