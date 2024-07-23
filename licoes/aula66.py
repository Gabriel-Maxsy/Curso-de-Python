"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

def soma(x, y, z):
    print(f'{x=} + {y=} + {z=} = {x + y+ z}')

soma(1, 2, 3) # Argumento Não nomeado (e posicional)
soma(1, y=2, z=3) # Argumento nomeado (quando vc nomeia um argumento, todo resto deve ser nomeado)

