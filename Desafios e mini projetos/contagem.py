def contagem():
    print ()
    print ("----------------------------------")
    print ("| Quantos numeros seu texto tem? |")
    print ("----------------------------------")
    print ()

    fechar = False
    total = 0
    palavra = input ("Digite o seu texto: ")

    while (not fechar):
        fechar = (total == len (palavra))
        total += 1

    print()
    print (total - 1)
    print ()
    print ("Deseja contar novamente?")
    print ()
    print ("(1) Sim (2) Não")
    print ()

    escolha = int (input ())

    if (escolha) == 1:
        contagem()

    elif (escolha) == 2:
        print("Obrigado por participar!")
        print ()

    else:
        print ("Selecione uma opção valida")
        print ()

if (__name__ == "__main__"):
    contagem()