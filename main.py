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
    else:
        print ('Tenho quase certeza que não é bem assim...')
        sleep(1)
        print ('Tente novamente por favor!')
        sleep(1)
        next = str(input('Por favor digite "NEXT" para seguir em frente: '))
        
        
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
print ('Sim sim, o típico jogo da velha, você escolhe com qual símbolo vai ficar e quem fizer uma diagonal, com três símbolos iguais, primeiro...')
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
    import teste
    teste.jogar_velha
menu = input('Digite o que você deseja: ')
#Condição do Menu Sair
if menu == 'sair':
    quit()
