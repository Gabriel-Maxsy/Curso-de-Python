"""
Tipo tupla - uma lista imutável
"""
nomes = 'Maria', 'Helena', 'Luiz' # Tuplas nao necessitam de [] e podem usar parenteses (opcional)
# Podemos converter os tipos, usando list (convertendo para lista) e tuple (convertendo para tuplas)

nomes = list(nomes) # Aqui converti para lista de novo

nomes = tuple(nomes) # Voltou a ser tupla (imutável ou seja nao podemos modificar usando metodos como 'append' ou 'del')

print(nomes)