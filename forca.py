import jogos


def jogar():

    print ("------------------------------")
    print ("| Bem vindo ao jogo de forca |")
    print ("------------------------------")

    palavra_secreta = "biblioteca"
    letras_certas = ["_ , _ , _ , _ , _ , _ , _ , _ , _ , _"]
    
    
    enforcado = False
    acertou = False

    while (not enforcado and not acertou):
        
        chute = input ("Escolha uma letra: ")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                letras_certas [index] = letra
            index = index + 1

        print (letras_certas)


    print ("------------------")
    print ("| Fim do jogo!!! |")
    print ("------------------")
    
    #Seleção de jogar novamente ou retornar a escolha
    print ("Deseja jogar de novo ou escolher outro jogo?")
    print ("(1) Jogar novamente (2) Voltar a seleção de jogos")

    escolha = int (input ())

    if (escolha == 1):
        jogar()
    elif (escolha == 2):
        jogos.select_game()
    else:
        print ("Selecione uma opção valida")

if (__name__ == "__main__"):
    jogar()