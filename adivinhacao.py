print ("------------------------------------")
print ("| Bem vindo ao jogo de adivinhação |")
print ("------------------------------------")

numero_secreto = 20

chute_str = input("Digite o seu número: ")

print ("Você digitou " , chute_str)

chute = int (chute_str)

acertou     = chute == numero_secreto
chute_maior = chute > numero_secreto
chute_menor = chute < numero_secreto

if (acertou):
    print ("Você acertou!")

else:
    if (chute_maior):
        print ("Você errou! Tente algo mais baixo")
    elif (chute_menor):
        print ("Você errou! Tente algo mais alto")

print ("------------------")
print ("| Fim do jogo!!! |")
print ("------------------")