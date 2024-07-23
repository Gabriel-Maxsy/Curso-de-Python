"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
# Palavra secreta
# Verificar se apenas uma letra foi digitada
# Conferir se a letra esta na palavra
# Se a letra não estiver na palavra mostrar * no lugar
# Contagem de tentativas do usuario

import os

palavra_secreta = 'arroz'
letras_acertadas = ''
tentativas = 0

while True:
    letra = input('Digite uma letra: ').lower()

    if len(letra) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra in palavra_secreta: # Se a letra (digitada) esta na palavra secreta. 
        letras_acertadas += letra # Guardando as letra digitada em uma váriavel.

    palavra_formada = ''

    for letras_secretas in palavra_secreta:
        if letras_secretas in letras_acertadas: # Conferindo 
            palavra_formada += letras_secretas
        else:
            palavra_formada += '*'

    tentativas += 1
    print(f'{palavra_formada} - {tentativas}')

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('Você acertou, a palavra era:',palavra_secreta)
        letras_acertadas = ''
        tentativas = 0
