# biblioteca (s) importarda (s)
from random import randint
from time import sleep
import sys

# interface player
player = str(input('Digite o seu nome/apelido (máximo de 10 caracteres): ')).strip()
sleep(1)
print ('PROCESSANDO.')
sleep(1)
print ('PROCESSANDO..')
sleep(1)
print ('PROCESSANDO...')
sleep(1)

# condição de nome/apelido de jogador
if len(player) >=1 and len(player) <= 10:
    print ('O seu nome de usuário não entra em conflito com as regras estabelecidas.')
    sleep(1)
    next = str(input('Por favor digite "NEXT" para seguir em frente: ')).strip()
    next.lower()
    if next == 'next':
        sleep(5)
        
    # condição para continuar jogo
elif len(player) > 10 or len(player) == 0:
    print ('O seu nome de usuário entra em conflito com as regras estabelecidas.')
    sleep(2)
    print ('GAME OVER: Regras devem ser cumpridas...')
    sleep(1)
    print ('Reinicie o programa!!!')
    sys.exit()

# Saudações e explicação do jogo
print ('Bem vindo ao "Jogo da Velha: Two Die", jogador {}!'.format(player))
sleep(1)
print ('Vamos lá, como o próprio nome já diz, esse jogo é um jogo da velha.')
sleep(1)
print ('Sim sim, o típico jogo da velha, você escolhe com qual símbolo vai ficar e quem fizer uma diagonal, com três síbolos iguais, primeiro...')
sleep(1)
print ('Ganha! ^w^')
sleep(2)

# Opções de Menu e como acessar
print ('Aqui estão as opções de Menu, por favor digite: ')
sleep(1)
print ('"Home" para acessar o Menu')
sleep(1)
print ('"Jogar" para começar o jogo ')
sleep(1)
# print ('Estilo: ')
print ('"Sair" para fechar o programa ')
sleep(1)
menu = input('Digite o que você deseja: ')

# Condição do Menu
menu.lower
# Condição do Menu Home
if menu == 'home':
    print ('Aqui estão as opções de Menu, por favor digite: ')
    sleep(1)
    print ('"Home" para acessar o Menu')
    sleep(1)
    print ('"Jogar" para começar o jogo ')
    sleep(1)
    # print ('Estilo: ')
    print ('"Sair" para fechar o programa ')
    sleep(1)
    menu = input('Digite o que você deseja: ')
# Condição do Menu Jogar
elif menu == 'jogar':
    print ('Olá! Para jogar o jogo da velha você irá preencher esses grids: ')
    print (' _ _ _')
    print (' _ _ _')
    print (' _ _ _')
    print (' ')
    print ('Porém você irá preenchê-los de acordo com uma numeração, de modo que cada grid estará representado pelos seguintes números: ')
    print (' 1 2 3')
    print (' 4 5 6')
    print (' 7 8 9')

    # Função de Grid
    def imprime_grid(grid):
        sleep(1)
        print ('O status do grid é\n')

        for indice in range(len(grid)):
            print (grid[indice], end=' ')
            if indice == 2 or indice == 5 or indice == 8:
                print ('')

    # Função que verifica o vencedor
    def verificar_grid(grid, jogador):

        #Linhas
        if grid[0] == jogador and grid[1] == jogador and grid[2] == jogador:
            if jogador == 'X':
                return 1
            else:
                return 2
        if grid[3] == jogador and grid[4] == jogador and grid[5] == jogador:
            if jogador == 'X':
                return 1
            else:
                return 2
        if grid[6] == jogador and grid[7] == jogador and grid[8] == jogador:
            if jogador == 'X':
                return 1
            else:
                return 2
    
        #Colunas
        if grid[0] == jogador and grid[3] == jogador and grid[6] == jogador:
            if jogador == 'X':
                return 1
            else:
                return 2
        if grid[1] == jogador and grid[4] == jogador and grid[7] == jogador:
            if jogador == 'X':
                return 1
            else:
                return 2
        if grid[2] == jogador and grid[5] == jogador and grid[8] == jogador:
            if jogador == 'X':
                return 1
            else:
                return 2
    
        #Diagonais
        if grid[0] == jogador and grid[4] == jogador and grid[8] == jogador:
            if jogador == 'X':
                return 1
            else:
                return 2
        if grid[2] == jogador and grid[4] == jogador and grid[6] == jogador:
            if jogador == 'X':
                return 1
            else:
                return 2
    
        return 0

    quantidades_escolhas = 0

    grid = ['_'] * 9

    while True:

        sleep(1)
        escolha = int(input('Qual a sua escolha: '))
        sleep(1)

        while grid[escolha - 1] != '_':
            print ('Sua escolha foi inválida! Veja como está o grid')
            imprime_grid(grid)
            escolha = int(input('Qual a sua escolha: '))

        grid[escolha - 1] = 'X'
        quantidades_escolhas += 1
        vencedor = verificar_grid(grid, 'X')
        if vencedor != 0:
            break
        if quantidades_escolhas == 9:
            break

        imprime_grid(grid)

        escolhac = randint(1,9)

        while grid[escolhac - 1] != '_':
            escolhac = randint(1,9)
        
        grid[escolhac - 1] = 'O'
        quantidades_escolhas += 1
        vencedor = verificar_grid(grid, 'O')
        if vencedor != 0:
            break

        imprime_grid(grid)

    sleep(1)
    if vencedor == 1:
        print ('Parabéns!! Você sobreviveu, dessa vez...')
    elif vencedor == 2:
        print ('Que pena, você morreu... até nunca mais ;)')
    else:
        print ('O jogo empatou, mas ainda não acabou... não desista (ou desista ^w^)')

    imprime_grid(grid)