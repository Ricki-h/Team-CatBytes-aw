# Bibliotecas importadas
import pygame as pg 
import math
import pandas as pd

# Cores utilizadas no jogo
preto = (0, 0, 0)
branco_smoke = (245, 245, 245)
roxo = (107, 63, 160)
rosa = (207, 52, 118)
azul = (135, 206, 235)
amarelo = (238, 173, 45)

# Definição de tamanho da tela
window = pg.display.set_mode((1000, 600))
# Preenchimento do fundo da tela
window.fill(branco_smoke)

# Inicialização da fonte
pg.font.init()
# Fonte escolhida
fonte = pg.font.SysFont('Comic Sans MS', 30)

board_array = [['n', 'n', 'n'],
               ['n', 'n', 'n'],
               [ 'n', 'n', 'n']]

# Variável de clique
clicque_last_status = 0
# Clique on e off variável
clique_on_off = 0
# Variável de posição de clique
clique_position_x = -1
clique_position_y = -1
# Variável de turno de O ou X
X_or_O_turn = 'x'
# Fim de jogo
end_game = 0

# Desenahndo linhas do jogo, com window sendo a janela, preto a cor das linhas, (205, 0) o começo da ponta da linha, (205, 600) o final da ponta da linha e 10 a largura da linha
def grade_do_tabuleiro(window):
    pg.draw.line(window, preto, (205, 0), (205, 600), 10)
    pg.draw.line(window, preto, (405, 0), (405, 600), 10)
    pg.draw.line(window, preto, (0, 205), (600, 205), 10)
    pg.draw.line(window, preto, (0, 405), (600, 405), 10)

# Organização de lógica de clique, cada coluna devolverá um valor x diferente, sendo eles, respectivamente, da esquerda para a direita: 1, 2 e 3
def clique_logica(clique_on_off, clique_last_status, x, y):
    if clique[0] == 0 and clique_last_status == 1:
        clique_on_off = 1
        x = (math.ceil(seta[0] / 200) - 1)
        y = (math.ceil(seta[0] / 200) - 1)
    elif clique[0] == 0 and clique_last_status == 0:
        clique_on_off =  0
        x = -1
        y = -1
    return clique_on_off, clique_last_status, x, y

def draw_selected_cell(window, board_array):
    for n in range(3):
        for nn in range(3):
            if board_array[nn][n] == 'x':
                jogador_x(window, n, nn)
            elif board_array[nn][n] == 'o':
                jogadro_o(window, n, nn)
            else:
                pass
# Função para definir se o clique estiver dentro de <3 quer dizer que ele está dentro do tabuleiro
def board_array_data(board_array, X_or_O_turn, end_game, x, y):
    if x < 3 and y < 3:
        # se for a vez do x, se a posição do board_array, se x é dirente de -1, se y é diferente de zero e se o jogo ainda não acabou
        if X_or_O_turn == 'x' and board_array[y][x] == 'n' and x != -1 and y != -1 and end_game == 0:
            board_array[y][x] = 'x'
            # muda a vez do jogo
            X_or_O_turn = 'o'
        if X_or_O_turn == 'o' and board_array[y][x] == 'n' and x != -1 and y != -1 and end_game == 0:
            # muda a vez do jogo
            board_array[y][x] = 'x'
            X_or_O_turn = 'o'
    return  board_array, X_or_O_turn

# Função para linha que diz quem venceu
def win_line(board_array, X_or_O_turn, end_game, x, y):
    if board_array[0][0] == 'x' and board_array[0][1] == 'x' and board_array[0][2] == 'x' \
    or board_array[0][0] == 'o' and board_array[0][1] == 'o' and board_array[0][2] == 'o':
        pg.draw.line(window, azul, (30, 100), (570, 100), 10 )
        end_game = 1
        X_or_O_turn = 'x'
    elif board_array[1][0] == 'x' and board_array[1][1] == 'x' and board_array[1][2] == 'x' \
    or board_array[1][0] == 'o' and board_array[1][1] == 'o' and board_array[1][2] == 'o':
        pg.draw.line(window, azul, (30, 300), (570, 300), 10)
        end_game = 1
        X_or_O_turn = 'x'
    elif board_array[2][0] == 'x' and board_array[2][1] == 'x' and board_array[2][2] == 'x' \
    or board_array[2][0] == 'x' and board_array[2][1] == 'x' and board_array[2][2] == 'x' \
        pg.draw.line(window, azul, (30, 500), (570, 500), 10)
        end_game = 1
        X_or_O_turn = 'x'
    elif board_array[0][2] == 'x' and board_array[1][2] == 'x' and board_array[2][2] == 'x' \
    or board_array[0][2] == 'o' and board_array[1][2] == 'o' and board_array[2][2] == 'o':
        pg.draw.line(windos, azul, )

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    
    # Declaração de variável de posição da seta do mouse
    seta = pg.mouse.get_pos()
    seta_position_x = seta[0]
    seta_position_y = seta[1]

    # Declaração de variável de clique da seta do mouse
    clique = pg.mouse.get_pressed()
    print (clique)

    # Jogo da Velha
    grade_do_tabuleiro(window)
    clique_on_off, clique_last_status, clique_position_x, clique_position_y = clique_logica(clique_on_off, clique_last_status, clique_position_x, clique_position_y)
    draw_selected_cell(window, board_array)
    board_array, X_or_O_turn = board_array_data(board_array, X_or_O_turn, end_game, x, y)

    # Último status do clique
    if clique[0] == 1:
        clique_last_status = 1
    else:
        clique_last_status = 0
    
    pg.display.update()


