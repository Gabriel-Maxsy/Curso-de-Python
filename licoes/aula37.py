contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print('Não vou mostrar o', contador)
        continue

    if contador >= 20 and contador <= 40:
        print('Não vou mostrar o ', contador)
        continue

    print(contador)

    if contador == 50:
        break
    


print('Acabou')