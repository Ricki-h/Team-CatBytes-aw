# Bibliotecas
import sys
from time import sleep

# Início do programa
nome = str(input('Por favor, digite um nome de usuário com no máximo 10 caracteres: ')).strip()
sleep(1)
print('CARREGANDO.')
sleep(1)
print('CARREGANDO..')
sleep(1)
print('CARREGANDO...')
sleep(1)

# Condições de medição do comprimento do nome de usuário do jogador
letras = len(nome)
if letras >=1 and letras <= 10:
    print('Seu nome está de acordo com as normas!')
    sleep(1)
    next = str(input('Por favor, prossiga em frente com o programa ao digitar "NEXT": ')).strip()
    next.lower()
    if next.strip() == 'next':
        sleep(3)
  
    # E se o usuário errar o "next"?
    else:
        sleep(1)
        print(f'O nome da função não é esse, jogador {nome}! Õ_Ô')
        sleep(1)
        print('Tente de novo!')
        next = str(input('Por favor, prossiga em frente com o programa ao digitar "NEXT": ')).strip()
        next.lower()
    # E se ele errar mais de uma vez?
        if next.strip() != 'next':
            sleep(1)
            print('Poxa, você errou de novo?')
            sleep(1)
            print('Vamos reiniciar para facilitar para você!')
            sleep(1)
            sys.exit()

# Condição para o jogador que não escrever (o nome de usuário) da forma esperada
else:
    print(f'Seu nome ultrapassa os caracteres, jogador {nome}.')
    sleep(1)
    print('Reinicie o programa e tente novamente, por favor!')
    sleep(1)
    sys.exit()

# Início propriamente dito do Menu
print(f'Bem-vindo, jogador(a) {nome}!')
sleep(1)
print('Esse sistema que você está acessando em específico é o de um simples jogo: o Jogo da Velha!')
sleep(1)
print('Ele é bem simples, caso você não conheça. Quem fizer uma linha reta com o mesmo símbolo primeiro...')
sleep(1)
print('Ganha! =D')
sleep(1)

def exibir_menu():
    print("Menu:")
    sleep(1)
    print("1. Home")
    sleep(1)
    print("2. Jogar")
    sleep(1)
    print("3. História")
    sleep(1)
    print("4. Sair")
    sleep(1)

def home():
    # Lógica para adicionar uma nova tarefa
    print("Menu:")
    sleep(1)
    print("1. Home")
    sleep(1)
    print("2. Jogar")
    sleep(1)
    print("3. História")
    sleep(1)
    print("4. Sair")
    sleep

def jogar():
    # Lógica para exibir as tarefas existentes
    print ('JOGO')

def historia():
    print('Por ser um jogo muito antigo, o Jogo da Velha não tem realmente uma explicação concreta e única para a sua origem,\njá que as partidas mais antigas da brincadeira datam de séculos passados, desde o século 14, com uma imensidade\nde registros no Egito, na China, na América pré-colombiana e no Império Romano.Porém, na teoria mais aceita, acredita-se\nque a expansão do jogo à Europa o fez explodir de verdade: na Inglaterra, quando as mulheres mais velhas já não tinham\nmais capacidade visual de bordar graças às limitações da idade, era sugerido esse jogo para que elas tivessem outro\nhobby/passatempo; por esse motivo, no Brasil, é conhecido atualmente como Jogo da Velha.')

def saida():
    print('Saindo.')
    sleep(1)
    print('Saindo..')
    sleep(1)
    print('Saindo...')
    sleep(1)
    sys.exit()

def main():
    while True:
        exibir_menu()
            
        escolha = input("Digite o que você deseja: ")
            
        if escolha == "1":
            home()
        elif escolha == "2":
            jogar()
        elif escolha == "3":
            historia()
        elif escolha == "4":
            saida()
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
