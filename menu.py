import sys
from time import sleep

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
