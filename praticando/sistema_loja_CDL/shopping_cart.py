from product import Product
class Cart:
    def __init__(self):
        self.products = []

    def total(self):
        return f'{sum([p.price for p in self.products]):.2f}'
    
    def inserir_produto(self, *Produtos):
        # self._produtos += produtos
        for p in Produtos:
            self.products.append(p)

    def listar_produtos(self):
        for p in self.products:
            print(p.name, p.price)

carrinho = Cart()
p1, p2, p3 = Product('Mouse', 149.99), Product('Notbook', 1000.00), Product('MousePad', 29.99)
p4 = Product('Eletrodo', 38.99)

carrinho.inserir_produto(p1, p2, p3)
print(carrinho.total())
carrinho.listar_produtos()
carrinho.inserir_produto(p4)
carrinho.listar_produtos()