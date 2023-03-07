import forca
import adivinhacao

def select_game():

    print ("-----------------------")
    print ("| Escolha o seu jogo! |")
    print ("-----------------------")

    print ("(1) Forca (2) Adivinhação")

    jogo = int (input ("Qual jogo? "))

    if (jogo == 1):
        print ("Você escolheu Forca")
        forca.jogar()
    elif (jogo == 2):
        print ("Você escolheu Adivinhação")
        adivinhacao.jogar()

if(__name__ == "__main__"):
    select_game()