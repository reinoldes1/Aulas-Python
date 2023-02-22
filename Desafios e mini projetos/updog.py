print ("---------")
print ("| Updog |")
print ("---------")

resposta = ["whats updog?", "what's updog?", "What's updog?", "Whats updog?"]

tentativas = 8

for rodada in range (1, tentativas + 1):
    chute = input ("You know updog?: ")
     
    if (chute in resposta):
        print ("Good what about u? ( •̀ ω •́ )y")
        break
     
    else:
        print ("No bro, you don't even know what updog means lol (≧∇≦)ﾉ")

if (tentativas >= 8):
    print("I don't want to play whit you anymore >:c")