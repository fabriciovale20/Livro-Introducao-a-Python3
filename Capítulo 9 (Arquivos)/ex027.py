"""
    Exercício 27

    Modifique o programa para também controlar a data de aniversário e o email de cada pessoa.
"""

agenda = []
cont_novo = cont_altera = cont_apaga = inicialização = 0
lido = 'Arquivo lido!'
gravado = 'Arquivo gravado!'
nome_inicial = ''

def pede_nome():
    nome = input('Nome: ')

    if nome == '':
        nome = 'Não identificado'
    
    return nome

def pede_telefone():
    telefone = input('Telefone: ')

    if telefone == '':
        telefone = 'xxxx-xxxx'
    
    return telefone

def pede_aniversário():
    aniversário = input('Data de aniversário: ')

    if aniversário == '':
        aniversário = 'xx/xx/xxxx'
    
    return aniversário

def pede_email():
    email = input('Email: ')

    if email == '':
        email = 'xxx@email.com'

    return email


def mostra_dados(nome, telefone, aniversário, email):
    print(f'Nome: {nome} | Telefone: {telefone} | Aniversário: {aniversário} | E-mail: {email}')

def pede_nome_arquivo():
    return input('Nome do arquivo: ')

def pesquisa(nome):
    mnome = nome.lower()

    for p, e in enumerate(agenda):
        if e[0].lower() == mnome:
            return p
        
    return None

def novo():
    global agenda, cont_novo, inicialização
    
    nome = pede_nome()

    if inicialização == 1:
        telefone = pede_telefone()
        aniversário = pede_aniversário()
        email = pede_email()
        agenda.append([nome, telefone, aniversário, email])

        cont_novo += 1
    else:
        for c in agenda:
            if nome != c[0]:
                telefone = pede_telefone()
                aniversário = pede_aniversário()
                email = pede_email()
                agenda.append([nome, telefone, aniversário, email])

                cont_novo += 1
                return
            else:
                print('Nome já cadastrado, tente outro.')
                return novo()

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
            aniversário = agenda[p][2]
            email = agenda[p][3]
            print('Encontrado: ')

            mostra_dados(nome, telefone, aniversário, email)
            nome = pede_nome()
            telefone = pede_telefone()
            aniversário = pede_aniversário()
            email = pede_email()
            agenda[p] = [nome, telefone, aniversário, email]

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
        mostra_dados(e[0], e[1], e[2], e[3])
    print('------\n')

def lê():
    global agenda, lido, cont_novo, cont_altera, cont_apaga, inicialização, nome_inicial
    
    if inicialização != 0:
        nome_arquivo = pede_nome_arquivo()
        gravar_arquivo_inicial(nome_arquivo)
    else:
        nome_arquivo = nome_inicial

    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            agenda = []

            for l in arquivo.readlines():
                nome, telefone, aniversário, email = l.strip().split('#')
                agenda.append([nome, telefone, aniversário, email])
    except Exception:
        print('Nenhum arquivo encontrado!')

    if inicialização != 0:
        print(f'Cadastros: {cont_novo}')
        print(f'Alterações: {cont_altera}')
        print(f'Exclusões: {cont_apaga}')
        print(lido)

        cont_novo = cont_altera = cont_apaga = 0

def grava():
    global gravado, cont_novo, cont_altera, cont_apaga
    nome_arquivo = pede_nome_arquivo()

    gravar_arquivo_inicial(nome_arquivo)

    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        for e in agenda:
            arquivo.write(f'{e[0]}#{e[1]}#{e[2]}#{e[3]}\n')

    print(f'Cadastros: {cont_novo}')
    print(f'Alterações: {cont_altera}')
    print(f'Exclusões: {cont_apaga}')
    print(gravado)
    
    cont_novo = cont_altera = cont_apaga = 0

def ordenar():
    global agenda

    agenda = sorted(agenda)
    lista()

def gravar_arquivo_inicial(nome_arquivo):
    with open('arquivo_inicialex023.txt', 'w', encoding='utf-8') as arquivo:
        arquivo.write(nome_arquivo)

def arquivo_inicial():
    global nome_inicial

    with open('arquivo_inicialex023.txt', 'r', encoding='utf-8') as arquivo:
        for c in arquivo:
            nome_inicial = c

        lê()

def valida_faixa_inteiro(pergunta, inicio, fim):
    while True:
        try:
            valor = int(input(pergunta))

            if inicio <= valor <= fim:
                return valor
        except ValueError:
            print(f'Valor inválido, favor digitar entre {inicio} e {fim}')

def menu():
    global inicialização

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

    inicialização += 1
    return valida_faixa_inteiro('Escolha uma opção: ', 0, 7)

while True:
    if inicialização == 0:
        arquivo_inicial()

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
