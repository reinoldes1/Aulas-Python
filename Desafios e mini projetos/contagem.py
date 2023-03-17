def contagem():
    print ("-------------------------------------")
    print ("| Quantos caracteres seu texto tem? |")
    print ("-------------------------------------")

    fechar = False
    total = 0
    palavra = input ("Digite o seu texto: ")

    while (not fechar):
        fechar = (total == len (palavra))
        total += 1

    print (total - 1)
    print ("Deseja contar novamente?")
    print ("(1) Sim (2) Não")

    escolha = int (input ())

    if (escolha) == 1:
        contagem()

    elif (escolha) == 2:
        print("Obrigado por participar!")

    else:
        print ("Selecione uma opção valida")

if (__name__ == "__main__"):
    contagem()