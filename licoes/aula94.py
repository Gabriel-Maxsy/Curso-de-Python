# Try, except, else e finally

# finally sempre será executado, independente do try ou except

try:
    print('Abrir arquivo')

except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
    print('Dividiu por zero')
except IndexError as error:
    print('IndexError')
except (NameError, ImportError):
    print('NameError, ImportError')
else:
    print('Não deu erro') # O else é aplicado quando nenhum erro ocorre
finally:
    print('fechar arquivo')

