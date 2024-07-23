lista = []

for x in range(3):
    for y in range(3):
        lista.append((x,y))

lista = [
    (x,y) # Adiciona o x e y na lista (esquerda do for)
    for x in range(3)
    for y in range(3)
]

lista = [
    [x for y in range(3)] # Complicado de explicar tente entender com os exemplos acima de forma exponencial de aprendizado.
    for x in range(3)
]

print(lista)