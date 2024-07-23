# Exemplo de uso dos sets

letras = set()

while True:
    letra = input('Digite uma letra: ')
    letras.add(letra.lower())

    if 'y' in letras:
        print('Letra encontrada')
        break
    
    print(letras)
