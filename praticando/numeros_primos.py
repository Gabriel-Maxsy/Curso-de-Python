# Número primo se ele é maior do 
# que um e é divisível apenas por
# um e por ele mesmo.


def e_primo(numero):
    # Números menores ou iguais a 1 não são primos
    if numero <= 1:
        return False
    # Verifica divisibilidade de 2 até a raiz quadrada do número
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Testando a função
numero = int(input("Digite um número: "))

if e_primo(numero):
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")
