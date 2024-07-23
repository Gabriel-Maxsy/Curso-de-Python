import importlib
import aula98_m

print(aula98_m.variavel)

for i in range (10):
    importlib.reload(aula98_m) # O reload da biblioteca importlib recarreca o import selecionado (aula98_m)
    print(i)

print("Fim")
