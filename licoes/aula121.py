# Métodos em instâncias de classes Python
# Hard coded - é algo que foi escrito diretamente no codigo

class Carro:
    def __init__(self, nome):
        self.nome = nome
    
    def acelerar(self):
        print(f'{self.nome} está acelerando...')

        # kilometro = 0
        # while True:
        #     print(f'acelerando...se passaram {kilometro} kilometros..')
        #     kilometro += 1


fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerar()

celta = Carro('Celta')
print(celta.nome)
celta.acelerar()