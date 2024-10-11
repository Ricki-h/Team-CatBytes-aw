import random
from time import sleep

# JOGO DA VELHA
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

    escolhac = random.randint(1,9)

    while grid[escolhac - 1] != '_':
        escolhac = random.randint(1,9)

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