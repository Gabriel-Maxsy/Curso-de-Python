import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# CUIDADO: fazendo delete sem where
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)
# Zerando o ID do banco
cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)
connection.commit()

# Cria a tabela
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)
connection.commit()

# Registrar valores nas colunas da tabela
# CUIDADO: sql injection
sql = (
    f'INSERT INTO {TABLE_NAME} '
    '(name, weight) '
    'VALUES '
    '(:name, :weight)'
)

# cursor.execute(sql, ['Teste', 2])
# cursor.executemany(
#     sql,
#     (
#         ('Gabriel', 3),
#         ('Yasmin', 2),
#         ('etc', 5)
#     )
# )

# Usando dicionarios 
cursor.execute(sql, {'name': 'teste', 'weight': 3})

# Quando usamos executemany sempre será uma lista:
cursor.executemany(
    sql, 
    [
        {'name': 'teste2', 'weight': 4},
        {'name': 'teste3', 'weight': 2},
        {'name': 'teste4', 'weight': 1}
    ]
)

connection.commit()


if __name__ == '__main__':
    print(sql)
    
    cursor.execute(
        f'DELETE FROM {TABLE_NAME} '
        'WHERE id = "3"'
    )

    cursor.execute(
        f'DELETE FROM {TABLE_NAME} '
        'WHERE id = "1"'
    )
    connection.commit()

    cursor.execute(
        f'SELECT * FROM {TABLE_NAME}'
    )

    for row in cursor.fetchall():
        _id, name, weight = row
        print(_id, name, weight)

    cursor.close()
    connection.close()