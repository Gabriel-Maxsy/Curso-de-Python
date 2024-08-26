from contextlib import contextmanager

@contextmanager
def my_open(caminho_arquivo, modo):
    try:
        print('Abrindo o arquivo')
        arquivo = open(caminho_arquivo, modo, encoding='utf8')
        yield arquivo
    except Exception as e: # Normalmente nao é usado nesses casos
        print('Ocorreu um erro', e)
    finally:
        print('Fechando o arquivo')
        arquivo.close()

with my_open('aula150.txt', 'w') as arquivo:
    arquivo.write('linha 1 \n')
    arquivo.write('linha 2 \n') # 'linha2',123 caso quiser ver o erro tratado
    arquivo.write('linha 3 \n')
    print('With', arquivo)