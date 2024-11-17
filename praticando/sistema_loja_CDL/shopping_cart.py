from pathlib import Path
import json

CAMINHO_RAIZ = Path(__file__).parent
DATA_JSON = CAMINHO_RAIZ / 'products.json'
CART_JSON = CAMINHO_RAIZ / 'cart.json'

class Cart:
    def __init__(self):
        self.products = self._load_cart()

    def _load_cart(self):
        """Carrega os produtos do carrinho do arquivo cart.json."""
        if CART_JSON.exists():
            with open(CART_JSON, 'r', encoding='utf-8') as file:
                return json.load(file)
        return []

    def _save_cart(self):
        """Salva os produtos do carrinho no arquivo cart.json."""
        with open(CART_JSON, 'w', encoding='utf-8') as file:
            json.dump(self.products, file, ensure_ascii=False, indent=2)

    def total(self):
        """Calcula o valor total do carrinho."""
        return f'{sum([p["price"] * p.get("amount", 1) for p in self.products]):.2f}'

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
                        # Verifica se o produto já está no carrinho
                        for cart_product in self.products:
                            if cart_product["name"].lower() == product_name.lower():
                                # Atualiza a quantidade no carrinho
                                cart_product["amount"] = cart_product.get("amount", 0) + amount
                                break
                        else:
                            # Adiciona o produto ao carrinho com a quantidade inicial
                            self.products.append({
                                "name": p["name"],
                                "price": p["price"],
                                "amount": amount
                            })

                        # Reduz a quantidade no estoque
                        p['amount'] -= amount
                        print(f'{amount} unidade(s) de {p["name"]} adicionada(s) ao carrinho.')

                        # Atualiza o estoque no arquivo JSON
                        file.seek(0)
                        json.dump(products, file, ensure_ascii=False, indent=2)
                        file.truncate()

                        # Salva o carrinho
                        self._save_cart()
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
            print(f'{p["name"]} - R$ {p["price"]:.2f} (Quantidade: {p.get("amount", 1)})')
        print(f"Total: R$ {self.total()}")

# if __name__ == '__main__':
#     cart = Cart()

#     cart.insert_product('Mouse', 2)
#     cart.insert_product('Teclado', 1)
#     cart.insert_product('Mouse', 1)  # Testando atualização de quantidade
