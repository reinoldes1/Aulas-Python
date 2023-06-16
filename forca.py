import jogos
import random

def jogar():

    print_opening()

    palavra_secreta = load_palavra_secreta()

    letras_certas = initialize_letras_acertadas(palavra_secreta)
    
    
    enforcado = False
    acertou = False
    tentativas = 0

    while (not enforcado and not acertou):
        
        chute = input ("Escolha uma letra: ")
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_certas [index] = letra
                index += 1
    
        else:
            tentativas += 1
            print("Você errou! faltam {} tentativas" .format (6 - tentativas))

        enforcado = tentativas == 6
        acertou = "_" not in letras_certas

        print (letras_certas)
        if (acertou):
            print ("-----------------------------------")
            print ("| Parabens você acertou a palavra |")
            print ("-----------------------------------")
        
        elif (enforcado):
            print ("------------------------")
            print ("| Que pena você perdeu |")
            print ("------------------------")



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