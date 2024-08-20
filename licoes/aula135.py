# Relações entre classes: associação, agregação e composição
# Agregação é uma forma mais especializada de associação
# entre dois ou mais objetos. Cada objeto terá
# seu ciclo de vida independente.
# Geralmente é uma relação de um para muitos, onde um
# objeto tem um ou muitos objetos.
# Os objetos podem viver separadamente, mas pode
# se tratar de uma relação onde um objeto precisa de
# outro para fazer determinada tarefa.
# (existem controvérsias sobre as definições de agregação).

class Carrinho:
    def __init__(self):
        self.produtos = []

    def total(self):
        return f'{sum([p.preco for p in self.produtos]):.2f}'
    
    def inserir_produto(self, *Produtos):
        # self._produtos += produtos
        for p in Produtos:
            self.produtos.append(p)

    def listar_produtos(self):
        for p in self.produtos:
            print(p.nome, p.preco)

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

carrinho = Carrinho()
p1, p2, p3 = Produto('Mouse', 149.99), Produto('Notbook', 1000.00), Produto('MousePad', 29.99)

carrinho.inserir_produto(p1, p2, p3)
print(carrinho.total())
carrinho.listar_produtos()