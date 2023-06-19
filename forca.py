import jogos
import random

def jogar():

    print_opening()

    palavra_secreta = load_palavra_secreta()

    letras_certas = initialize_letras_acertadas(palavra_secreta)

    print (letras_certas)
    
    
    enforcado = False
    acertou = False
    tentativas = 0

    while (not enforcado and not acertou):
        
        chute = ask_chute()

        if (chute in palavra_secreta):
            print_right_answer(chute, letras_certas, palavra_secreta)

    
        else:
            tentativas += 1
            enforcando(tentativas)

        enforcado = tentativas == 7
        acertou = "_" not in letras_certas

        print (letras_certas)
        if (acertou):
            print_win()
        
        elif (enforcado):
            print_lose(palavra_secreta)

    print_ending()
    
    #Seleção de jogar novamente
    
    player_selection()

def print_opening():
    print ("------------------------------")
    print ("| Bem vindo ao jogo de forca |")
    print ("------------------------------")

def load_palavra_secreta():
    arquivo = open("C:/Users/reinoldes/Desktop/Alura/Aula Python/Aulas-Python/frutas.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)


    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def initialize_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def ask_chute():
    chute = input ("Escolha uma letra: ")
    chute = chute.strip().upper()
    return(chute)

def print_right_answer(chute, letras_certas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_certas [index] = letra
        index += 1

def enforcando(tentativas):
    print("  _______     ")
    print(" |/      |    ")

    if(tentativas == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(tentativas == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (tentativas == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print() 

def print_win():
    print ("-----------------------------------")
    print ("| Parabens você acertou a palavra |")
    print ("-----------------------------------")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def print_lose(palavra_secreta):
    print ("------------------------")
    print ("| Que pena você perdeu |")
    print ("------------------------") 
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")   

def print_ending():
    print ("------------------")
    print ("| Fim do jogo!!! |")
    print ("------------------")
    
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

if (__name__ == "__main__"):
    jogar()