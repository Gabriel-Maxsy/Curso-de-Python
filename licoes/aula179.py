# csv.reader e csv.DictReader
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário
import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'aula179.csv'

with open(CAMINHO_CSV, 'w', encoding='utf-8') as arquivo:
     arquivo.writelines(
         ('Nome,', 'Idade,', 'Endereço\n', 'Gabriel,', '32,', '"Av. sei la, 21 "Centro""\n', 'Mateus,', '21,', '"Av. aa"')
         )

with open(CAMINHO_CSV, 'r') as arquivo:
    leitor = csv.DictReader(arquivo)

    for linha in leitor:
        print(linha['Nome'], linha['Idade']) #, linha['Endereço'])

# with open(CAMINHO_CSV, 'r') as arquivo:
#     leitor = csv.reader(arquivo)

#     for linha in leitor:
#         print(linha)