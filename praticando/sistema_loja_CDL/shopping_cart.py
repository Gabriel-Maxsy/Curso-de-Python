from pathlib import Path
import json

CAMINHO_RAIZ = Path(__file__).parent
DATA_JSON = CAMINHO_RAIZ / 'products.json'

class Cart:
    def __init__(self):
        self.products = []  # Produtos no carrinho

    def total(self):
        """Calcula o valor total do carrinho."""
        return f'{sum([p["price"] for p in self.products]):.2f}'

    def insert_product(self, product_name: str, amount: int):
        """Insere um produto no carrinho se ele existir no estoque."""
        if amount <= 0:
            print("Quantidade inválida.")
            return

        with open(DATA_JSON, 'r+', encoding='utf-8') as file:
            products = json.load(file)

            for p in products:
                if p['name'].lower() == product_name.lower():  # Ignora maiúsculas/minúsculas
                    if p['amount'] >= amount:
                        # Adiciona ao carrinho
                        for _ in range(amount):
                            self.products.append({"name": p["name"], "price": p["price"]})
                        # Reduz a quantidade no estoque
                        p['amount'] -= amount
                        print(f'{amount} unidade(s) de {p["name"]} adicionada(s) ao carrinho.')

                        # Atualiza o estoque no arquivo JSON
                        file.seek(0)
                        json.dump(products, file, ensure_ascii=False, indent=2)
                        file.truncate()
                        return
                    else:
                        print("Estoque insuficiente.")
                        return

            print("Produto não encontrado.")

    def list_products(self):
        """Lista os produtos no carrinho."""
        if not self.products:
            print("Carrinho vazio.")
            return

        print("Produtos no carrinho:")
        for p in self.products:
            print(f'{p["name"]} - R$ {p["price"]:.2f}')
        print(f"Total: R$ {self.total()}")

if __name__ == '__main__':
    cart = Cart()

    # Testando o carrinho
    cart.insert_product('Mouse', 2)
    cart.list_products()
    cart.insert_product('Teclado', 1)
    cart.list_products()
