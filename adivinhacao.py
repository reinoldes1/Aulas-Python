import random


print ("------------------------------------")
print ("| Bem vindo ao jogo de adivinhação |")
print ("------------------------------------")

numero_secreto = round (random.randrange (1, 101))
tentativas = 8

print (numero_secreto)

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
        print ("Você acertou!")
        break

    else:
        if (chute_maior):
            print ("Você errou! Tente algo mais baixo")
        elif (chute_menor):
            print ("Você errou! Tente algo mais alto")

print ("------------------")
print ("| Fim do jogo!!! |")
print ("------------------")