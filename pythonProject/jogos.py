import forca
import adivinhacao

print ("*******************")
print ("****** Jogos ******")
print ("*******************")

print ("(1) Forca (2) Adivinhação")

jogo = int(input("Escolha um jogo: "))

if (jogo == 1):
    print ("Jogando forca")
    forca.jogar()

elif (jogo == 2):
    print ("Jogando adivinhação")
    adivinhacao.jogar()