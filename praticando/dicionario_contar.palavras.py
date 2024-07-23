# Escreva uma função que receba uma string e retorne um dicionário com a contagem de cada palavra na string.

dicionario = {}

def contar_palavras(palavra):

    for letra in palavra:
        letra = palavra
        dicionario[letra] = len(palavra)

    return dicionario

print(contar_palavras('QuantasLetrasTemAqui'))