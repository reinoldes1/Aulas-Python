import jogos
import random

def jogar():
    
    print_opening()
    

    numero_secreto = round (random.randrange (1, 101))
    tentativas = 0
    pontos = 1000

    nivel = int (input ())

    if (nivel == 1):
        tentativas = 15
    elif (nivel == 2):
        tentativas = 8
    else:
        tentativas = 5

    for rodada in range (1, tentativas + 1):
        print ("Tentativa {} de {}". format (rodada , tentativas))
        chute_str = input("Digite um número de 1 a 100: ")
        print ("Você digitou " , chute_str)
        chute = int (chute_str)

        if (chute < 1 or chute > 100):
            print ("Digite um numero de 1 a 100")
            continue

        acertou     = chute == numero_secreto
        chute_maior = chute > numero_secreto
        chute_menor = chute < numero_secreto

        if (acertou):
            print ("Você acertou e fez {} pontos!" .format (pontos))
            break

        else:
            if (chute_maior):
                print ("Você errou! Tente algo mais baixo")
            elif (chute_menor):
                print ("Você errou! Tente algo mais alto")
                    
            pontos_perdidos = abs (numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    #Mostrar o numero secreto 
    if (numero_secreto != chute ):
        print ("O seu número era: " , (numero_secreto))

    print_ending()

    player_selection()

    escolha = int (input ())

    if (escolha == 1):
        jogar()
    elif (escolha == 2):
        jogos.select_game()
    elif (escolha == 3):
        print ("Obrigado por jogar!")
    else:
        print ("Selecione uma opção valida")

def print_opening():
    print ("------------------------------------")
    print ("| Bem vindo ao jogo de adivinhação |")
    print ("------------------------------------")

    print ("Selecione a dificuldade:")
    print ("(1) Fácil (2) Médio (3) Difícil")

def print_ending():
    print ("------------------")
    print ("| Fim do jogo!!! |")
    print ("------------------")

    #Seleção de jogar novamente

    print ("Deseja jogar de novo ou escolher outro jogo?")
    print ("(1) Jogar novamente (2) Voltar a seleção de jogos (3) Sair")

def player_selection():
    escolha = int (input ())

    if (escolha == 1):
        jogar()
    elif (escolha == 2):
        jogos.select_game()
    elif (escolha == 3):
        print ("Obrigado por jogar!")
    else:
        print ("Selecione uma opção valida")

#Rodar script direto

if (__name__ == "__main__"):
    jogar()
