# Generators são funções que podem pausar.
# Generator expression, Iterables e Iterators em Python

import sys

iterable = ['Eu', 'tenho', '__iter__']
iterador = iter(iterable) # tem __iter__ e __next__
lista = [n for n in range (1000000)]
generator = (n for n in range (1000000))

print(sys.getsizeof(lista)) # Mostra o tamanho em bytes
print(sys.getsizeof(generator))

print(generator)