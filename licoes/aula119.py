import json
# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

# Caminho do arquivo
CAMINHO_ARQUIVO = 'aula119.json'

# Listas de tarefas e itens removidos
itens_removidos = []
def listar(lista):
    print('\nTarefas:')
    if not lista:
        print('Lista vazia\n')
    else:
        for tarefa in lista:
            print(tarefa)
    print()

def desfazer(lista):
    if not lista:
        print('\nNada a desfazer\n')
    else:
        itens_removidos.append(lista.pop())
        listar(lista)

def refazer(lista):
    if not itens_removidos:
        print('\nNada a refazer\n')
    else:
        lista.append(itens_removidos.pop())
        listar(lista)

def ler(caminho):
    try:
        with open(caminho, 'r', encoding='utf8') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        print('Arquivo não existe. Criando um novo.')
        salvar([], caminho)
        return []

def salvar(lista, caminho):
    with open(caminho, 'w', encoding='utf8') as arquivo:
        json.dump(lista, arquivo, indent=2, ensure_ascii=False)

# Inicializa a lista de tarefas
lista_tarefas = ler(CAMINHO_ARQUIVO)

while True:
    print('Comandos: listar, desfazer, refazer')
    resposta = input('Digite uma tarefa ou comando: ').strip()

    if resposta == 'listar':
        listar(lista_tarefas)
    elif resposta == 'desfazer':
        desfazer(lista_tarefas)
    elif resposta == 'refazer':
        refazer(lista_tarefas)
    else:
        lista_tarefas.append(resposta)
        print('Tarefa adicionada.')
    
    # Atualiza o arquivo JSON
    salvar(lista_tarefas, CAMINHO_ARQUIVO)

# Solução do professor:

# import json
# import os


# def listar(tarefas):
#     print()
#     if not tarefas:
#         print('Nenhuma tarefa para listar')
#         return

#     print('Tarefas:')
#     for tarefa in tarefas:
#         print(f'\t{tarefa}')
#     print()


# def desfazer(tarefas, tarefas_refazer):
#     print()
#     if not tarefas:
#         print('Nenhuma tarefa para desfazer')
#         return

#     tarefa = tarefas.pop()
#     print(f'{tarefa=} removida da lista de tarefas.')
#     tarefas_refazer.append(tarefa)
#     print()
#     listar(tarefas)


# def refazer(tarefas, tarefas_refazer):
#     print()
#     if not tarefas_refazer:
#         print('Nenhuma tarefa para refazer')
#         return

#     tarefa = tarefas_refazer.pop()
#     print(f'{tarefa=} adicionada na lista de tarefas.')
#     tarefas.append(tarefa)
#     print()
#     listar(tarefas)


# def adicionar(tarefa, tarefas):
#     print()
#     tarefa = tarefa.strip()
#     if not tarefa:
#         print('Você não digitou uma tarefa.')
#         return
#     print(f'{tarefa=} adicionada na lista de tarefas.')
#     tarefas.append(tarefa)
#     print()
#     listar(tarefas)


# def ler(tarefas, caminho_arquivo):
#     dados = []
#     try:
#         with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
#             dados = json.load(arquivo)
#     except FileNotFoundError:
#         print('Arquivo não existe')
#         salvar(tarefas, caminho_arquivo)
#     return dados


# def salvar(tarefas, caminho_arquivo):
#     dados = tarefas
#     with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
#         dados = json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)
#     return dados


# CAMINHO_ARQUIVO = 'aula119.json'
# tarefas = ler([], CAMINHO_ARQUIVO)
# tarefas_refazer = []

# while True:
#     print('Comandos: listar, desfazer e refazer')
#     tarefa = input('Digite uma tarefa ou comando: ')

#     comandos = {
#         'listar': lambda: listar(tarefas),
#         'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
#         'refazer': lambda: refazer(tarefas, tarefas_refazer),
#         'clear': lambda: os.system('clear'),
#         'adicionar': lambda: adicionar(tarefa, tarefas),
#     }
#     comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else \
#         comandos['adicionar']
#     comando()
#     salvar(tarefas, CAMINHO_ARQUIVO)