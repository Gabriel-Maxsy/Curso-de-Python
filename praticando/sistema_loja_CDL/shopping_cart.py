from product import Product
import json

DATA_JSON = 'products.json'

class Cart:
    def __init__(self):
        self.products = []
        self._found_product = False

    def total(self):
        return f'{sum([p.price for p in self.products]):.2f}'
    
    def insert_product(self, product_name: str):
        with open(DATA_JSON, 'r', encoding='utf-8') as file:
            products = json.load(file)

        # self._products += products
        for p in products:

            if product_name in p['name']:
                self._found_product = True
                if p['amount'] > 0:
                    self.products.append(p)
                    # p -= 1 IMPLEMENTAR ISTO
                    # print(f'Produto encontrado e tem quantidade {self._found_product}')
                else:
                    print('Não temos a quantidade de produto que voce deseja')
        
        if not self._found_product:
            print('Produto não encontrado')
        
        self._found_product = False

    def list_products(self):
        for p in self.products:
            print(p['name'], p['price'])

if __name__ == '__main__':
    cart = Cart()

    cart.insert_product('Mouse')
    cart.list_products()
    cart.insert_product('teclado')