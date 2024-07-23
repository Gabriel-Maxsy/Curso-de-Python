# Try, except, else e finally

try:
    a = 18
    b = 0, 's'
    # print(b[0])
    # print('Linha 1'[1000])
    c = a / b

except ZeroDivisionError as e:
    print(e)
    print(e.__class__.__name__)
except NameError:
    print('Variavel não definida')
except (TypeError, IndexError) as error:
    print('MSG:',error)
    print('ERRO:',error.__class__.__name__)
except Exception as es: # Exception é o tipo de erro geral, ele nao especifica o erro (erro desconhecido)
    print('MSG:', es)

