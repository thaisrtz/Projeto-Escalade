import random

print("**********************************")
print ("Bem vindo ao jogo de adivinhação")
print("**********************************")

numero_secreto = random.randrange(0,101)
tentativas = 0
pontos = 100

print ("Níveis de dificuldade:")
print ("(1) Fácil (2) Médio (3) Difícil")

nivel = int(input("Escolha o nível: "))

if (nivel==1):
    tentativas = 8

elif (nivel==2):
    tentativas = 6

elif (nivel==3):
    tentativas = 4

else:
    print ("Escolha um nivel de 1 a 3")

for rodada in range (1, tentativas +1):
    print ("Rodada {} de {}". format (rodada, tentativas))
    chute_str = input ("Digite um numero de 1 a 100: ")
    chute =  int(chute_str)

    if (chute < 1 or chute > 100):
        print ("Você precisa digitar um número entre 1 e 100!")
        continue

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

        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

print ("Fim do jogo!")
print ("O número secreto era ", numero_secreto)
if (acertou):
    print ("Você fez {} pontos!". format (pontos))
else:
    print ("Você não fez nenhum ponto.")
