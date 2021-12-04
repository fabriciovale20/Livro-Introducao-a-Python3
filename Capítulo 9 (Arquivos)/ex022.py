"""
    Exercício 22

    Ao ler ou grava uma nova lista, verifique se a agenda atual já foi gravada. Você pode usar uma variável para controlar quando a lista foi
altarada (novo, altera, apaga) e reinicializar esse valor quando ela for lida ou gravada.
"""

agenda = []
cont_novo = cont_altera = cont_apaga = 0
lido = 'Arquivo lido!'
gravado = 'Arquivo gravado!'

def pede_nome():
    return input('Nome: ')

def pede_telefone():
    return input('Telefone: ')

def mostra_dados(nome, telefone):
    print(f'Nome: {nome} Telefone: {telefone}')

def pede_nome_arquivo():
    return input('Nome do arquivo: ')

def pesquisa(nome):
    mnome = nome.lower()

    for p, e in enumerate(agenda):
        if e[0].lower() == mnome:
            return p
        
    return None

def novo():
    global agenda, cont_novo
    
    nome = pede_nome()
    telefone = pede_telefone()
    agenda.append([nome, telefone])

    cont_novo += 1

def apaga():
    global agenda, cont_apaga

    nome = pede_nome()
    p = pesquisa(nome)

    confirmar = input('Deseja realmente apagar? ').strip().upper()[0]
    if confirmar == 'S':
        if p is not None:
            del agenda[p]
            print('Registro apagado.')
            cont_apaga += 1
        else:
            print('Nome não encontrado.')
    else:
        print('Operação cancelada.')

def altera():
    global cont_altera

    p = pesquisa(pede_nome())

    confirmar = input('Deseja realmente alterar? ').strip().upper()[0]
    if confirmar == 'S':
        if p is not None:
            nome = agenda[p][0]
            telefone = agenda[p][1]
            print('Encontrado: ')
            mostra_dados(nome, telefone)
            nome = pede_nome()
            telefone = pede_telefone()
            agenda[p] = [nome, telefone]

            cont_altera += 1
        else:
            print('Nome não encontrado.')
    else:
        print('Operação cancelada.')

def lista():
    print('\nAgenda\n\n------')
    cont = 0

    for e in agenda:
        cont += 1
        print(f'{cont}º contato - ', end='')
        mostra_dados(e[0], e[1])
    print('------\n')

def lê():
    global agenda, lido, cont_novo, cont_altera, cont_apaga

    nome_arquivo = pede_nome_arquivo()

    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        agenda = []

        for l in arquivo.readlines():
            nome, telefone = l.strip().split('#')
            agenda.append([nome, telefone])

    print(f'Cadastros: {cont_novo}')
    print(f'Alterações: {cont_altera}')
    print(f'Exclusões: {cont_apaga}')
    print(lido)

    cont_novo = cont_altera = cont_apaga = 0

def grava():
    global gravado, cont_novo, cont_altera, cont_apaga
    nome_arquivo = pede_nome_arquivo()

    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        for e in agenda:
            arquivo.write(f'{e[0]}#{e[1]}\n')

    print(f'Cadastros: {cont_novo}')
    print(f'Alterações: {cont_altera}')
    print(f'Exclusões: {cont_apaga}')
    print(gravado)

    cont_novo = cont_altera = cont_apaga = 0

def ordenar():
    global agenda

    agenda = sorted(agenda)
    lista()

def valida_faixa_inteiro(pergunta, inicio, fim):
    while True:
        try:
            valor = int(input(pergunta))

            if inicio <= valor <= fim:
                return valor
        except ValueError:
            print(f'Valor inválido, favor digitar entre {inicio} e {fim}')

def menu():
    print(f"""
    1 - Novo
    2 - Altera
    3 - Apaga
    4 - Lista
    5 - Grava
    6 - Lê
    7 - Ordenar lista
    
    0 - Sai

    Agenda contém: {len(agenda)} contatos
    """)
    return valida_faixa_inteiro('Escolha uma opção: ', 0, 7)

while True:
    opção = menu()
    if opção == 0:
        break
    elif opção == 1:
        novo()
    elif opção == 2:
        altera()
    elif opção == 3:
        apaga()
    elif opção == 4:
        lista()
    elif opção == 5:
        grava()
    elif opção == 6:
        lê()
    elif opção == 7:
        ordenar()
