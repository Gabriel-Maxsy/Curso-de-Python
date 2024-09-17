import json
DATA_JSON = 'products.json'

class Product:
    def __init__(self, nome, preco):
        self.name = nome
        self.price = preco

        # Abre o arquivo no modo 'r' (leitura), ou cria uma lista vazia se o arquivo estiver vazio
        try:
            with open(DATA_JSON, 'r', encoding='utf8') as arquivo:
                produtos = json.load(arquivo)
        except json.JSONDecodeError:
            # Se o arquivo estiver vazio ou corrompido, começa com uma lista vazia
            produtos = []

        # Adiciona o novo produto à lista de produtos
        produtos.append({
            'nome': self.name,
            'preco': self.price
        })

        # Reescreve o arquivo com a lista atualizada
        with open(DATA_JSON, 'w', encoding='utf8') as arquivo:
            json.dump(produtos, arquivo, ensure_ascii=False, indent=2)