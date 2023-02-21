print ("---------")
print ("| Updog |")
print ("---------")

resposta_certa = ("whats updog?")

#("Whats updog?") ("What's updog?") ("what's updog?")


while (resposta_certa):

    chute = input ("You know updog?: ")

    acertou = resposta_certa == chute
        
    if (acertou):
        print ("Good what about u?")
        break
    
    else:
        print ("Try again")