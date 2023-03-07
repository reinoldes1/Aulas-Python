import jogos


def jogar():

    print ("------------------------------")
    print ("| Bem vindo ao jogo de forca |")
    print ("------------------------------")

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