class Car:
    def __init__(self):
        self.products = ['teste1', 'teste2', 'teste3']

    def print_products(self):
        i = 1
        print("Your product's list are: ")
        for product in self.products:
            print(f'{i}-{product}')
            i += 1

    def add_product(self, *products):
        for p in products:
            self.products.append(p)


car1 = Car()
car1.add_product('mouse', 'lamp', 'lights')
car1.print_products()