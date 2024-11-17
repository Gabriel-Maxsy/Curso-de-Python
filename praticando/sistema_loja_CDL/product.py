import json
from typing import Literal
from pathlib import Path

CAMINHO_RAIZ = Path(__file__).parent
DATA_JSON = CAMINHO_RAIZ / 'products.json'

categories = Literal['Electric', 'Tools', 'Paints', 'Utilities']
VALID_CATEGORIES = ['Electric', 'Tools', 'Paints', 'Utilities']

class Product:
    def __init__(self, name: str, price: float, category: categories, amount: int):
        self.__found_product = False
        self.__name = name
        self.__price = price
        self.__amount = amount
         
        if category not in VALID_CATEGORIES:
            raise ValueError(f'Product category "{category}" is invalid.')
        
        self.category = category
        
        # Abre o arquivo no modo 'r' (leitura) ou cria uma lista vazia se o arquivo estiver vazio
        try:
            with open(DATA_JSON, 'r', encoding='utf8') as file:
                _products = json.load(file)
        except json.JSONDecodeError:
            # Se o arquivo estiver vazio ou corrompido, começa com uma lista vazia
            _products = []

        for map_ in _products:
            if self.__name in map_['name']:
                map_['amount'] += self.__amount
                self.__found_product = True
                break
            
        if not self.__found_product:
            # Adiciona o novo produto à lista de produtos
            _products.append({
                        'name': self.__name,
                        'price': self.__price,
                        'category': self.category,
                        'amount': self.__amount
                    })
        
        # Reescreve o arquivo com a lista atualizada
        with open(DATA_JSON, 'w', encoding='utf8') as file:
            json.dump(_products, file, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    p2 = Product('Eucatex azul', 248.00, 'Paints', 1)
    p1 = Product('Mouse', 123,'Electric', -20)
    print('funcionou')