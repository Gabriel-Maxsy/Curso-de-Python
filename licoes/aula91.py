# Introdução as Generator functions em Python
# generator = (n for n in range(1000)) 

# É o mesmo que:

def generator(n=0, maximum=10):
    while True:
        yield n
        
        n += 1

        if n >= maximum:
            return

gen = generator(maximum=1000)
for n in gen:
    print(n)