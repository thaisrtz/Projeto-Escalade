print("**********************************")
print ("Bem vindo ao jogo de adivinhação")
print("**********************************")

numero_secreto = 7
tentativas = 3

for rodada in range (1, tentativas +1):
    print ("Rodada {} de {}". format (rodada, tentativas))
    chute_str = input ("Digite um numero: ")
    chute =  int(chute_str)

    print ("Você digitou o numero ", chute)

    if (chute < 1):
        print ("Você precisa digitar um número entre 1 e 100!")

    if (chute > 100):
        print ("Você precisa digitar um número entre 1 e 100!")

    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print ("Você acertou!")
        break

    else:
        ("Você errou!")
        if (maior):
            print ("O seu chute foi maior do que o número secreto.")

        elif (menor):
            print("O seu chute foi menor do que o número secreto.")

print ("Fim do jogo!")
