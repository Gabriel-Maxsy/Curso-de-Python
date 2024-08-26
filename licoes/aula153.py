# Método especial __call__
# callable é algo que pode ser executado com parênteses
# Em classes normais, __call__ faz a instância de uma
# classe "callable".

class CallMe:
    def __init__(self, phone):
        self.phone = phone
    
    def __call__(self, nome):
        print(nome, 'Está chamando', self.phone)
        return 123 # Exemplo de que o metodo __call__ pode retornar

call1 = CallMe('124214124')
retorno = call1('Gabriel')
print(retorno)