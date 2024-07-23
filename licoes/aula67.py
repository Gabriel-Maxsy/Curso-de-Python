"""
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem
ter valores padrão. Caso não seja
enviado para o parâmetro, o valor padrão será
usado.
Refatorar: editar o seu código.
"""
#             valor padrão
def soma(x, y, z=None):
    if z is not None:
        print(f'{x=} + {y=} + {z=} = {x + y + z}')
    else:
        print(f'{x=} + {y=} = {x + y}')

soma(1, 2) 
soma(3, 5) 
soma(100, 200) 
soma(23, 10, 20)
soma(y=10, z=5, x=2)