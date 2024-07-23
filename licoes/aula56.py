"""
split e join com list e str
split - divide uma string usando espaços se não definirmos
join - une uma string
"""
frase = 'Olha só que, coisa interessante'
lista_frases_cruas = frase.split(',') # Podemos definir como queremos separar Ex.: split(',') separaria a frase onde esta virgula nela

lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

# print(lista_frases_cruas)
# print(lista_frases)
frases_unidas = ', '.join(lista_frases)
print(frases_unidas)
