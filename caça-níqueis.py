import random

MAX_LINHAS = 3
MAX_APOSTA = 500
MIN_APOSTA = 50

LINHAS = 3
COLUNAS = 3

quantidade_simbolo = {
    'A': 3,
    'B': 4,
    'c': 5,
    'D': 6 
}

valor_simbolos = {
    'A': 6,
    'B': 5,
    'c': 4,
    'D': 3 
}

# Verifaca os ganhos e as linhas ganhas 
def checar_vitorias(colunas, linhas, aposta, valores):
    ganhos = 0
    linhas_ganhas = []
    for linha in range(linhas):
        simbolo = colunas[0][linha]
        for coluna in colunas:
            simbolo_a_checar = coluna[linha]
            if simbolo != simbolo_a_checar:
                break
        else:
            ganhos += valores[simbolo] * aposta
            linhas_ganhas.append(linha +1)
    
    return ganhos, linhas_ganhas

# Printa a ordem dos resultados sorteados
def printar_resultado(colunas):
    for linha in range(len(colunas[0])):
        for i, coluna in enumerate(colunas):
            if i != len(colunas) -1:
                print(coluna[linha], end=' | ')
            else:
                print(coluna[linha], end='')
        print()

# Gera (sortea) a ordem dos resultados das colunas 
def girar_maquica(linhas, coluns, simbolos):
    Todos_simbolos = []
    for simbolo, quantidade_simbolo in simbolos.items():
        for _ in range(quantidade_simbolo):
            Todos_simbolos.append(simbolo)

    colunas = []
    for _ in range(coluns):
        coluna = []
        simbolos_atuais = Todos_simbolos[:]
        for _ in range(linhas):
            valor = random.choice(simbolos_atuais)
            simbolos_atuais.remove(valor)
            coluna.append(valor)

        colunas.append(coluna)

    return colunas

# Função para introduzir a quantidade do deposito
def depositar():
    while True:
        quantia = input('Quanto quer depositar? ')
        if quantia.isdigit():
            quantia = int(quantia)
            if 50 <= quantia <= 5000:
                break
            else:
                print(f'A quantia tem que ser maior ou igual que kz{MIN_APOSTA} e menor ou igual a kz5000.')
        else:
            print('Digite um numero inteiro!')
    return quantia

# Função para inserir a quantidade de linhas a serem apostadas
def numeros_linhas():
    while True:
        linhas = input(f'Em quantas linhas queres apostar (1-{MAX_LINHAS})? ')
        if linhas.isdigit():
            linhas = int(linhas)
            if 1 <= linhas <= MAX_LINHAS:
                break
            else:
                print(f'Digite um numero entre (1-{MAX_LINHAS})? ')
        else:
            print('Digite um numero válido!')
    return linhas

# Função para inserir a quantidade a ser postada
def apostar():
    while True:
        quantia = input('Quanto quer apostar? ')
        if quantia.isdigit():
            quantia = int(quantia)
            if 50 <= quantia <= 5000:
                break
            else:
                print(f'A quantia tem que ser maior ou igual que kz{MIN_APOSTA} e menor ou igual a kz{MAX_APOSTA}.')
        else:
            print('Digite um inteiro válido!')
    return quantia

# Função para receber os resultado das funções acima definidas e retorna os ganhos
def jogar(saldo):
    linhas = numeros_linhas()
    while True:
        aposta = apostar()
        total_aposta = aposta * linhas
        if total_aposta > saldo:
            print(f'Você não tem o suficienta para apostar, o seu saldo atual é: kz{saldo}')
        else:
            break
    print(f'Você está apostando {aposta} em {linhas} linhas. Total da aposta é igual a: kz{total_aposta}')

    giros = girar_maquica(LINHAS, COLUNAS, quantidade_simbolo)
    printar_resultado(giros)
    ganhos, linhas_ganhas = checar_vitorias(giros, linhas, aposta, valor_simbolos)
    print(f'Você ganhou kz{ganhos}')
    print('Você ganhou na: ', *linhas_ganhas)
    return ganhos - total_aposta

# Função resumo geral do jogo e inicia o jogo
def principal():
    saldo = depositar()
    while True:
        print(f'Saldo atual é kz{saldo}')
        resposta = input('Tecla ENTER para girar (Q para sair)!')
        if resposta == 'q':
            break
        saldo += jogar(saldo)

    print(f'Você ficou com kz{saldo}')

principal()