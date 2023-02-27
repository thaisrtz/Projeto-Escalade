def jogar():
    print("*****************************")
    print ("Bem vindo ao jogo de forca")
    print("*****************************")

    secret_word = "banana"

    defeat = False
    victory = False

    while(not defeat and not victory):

        trial = input("Digite uma letra: ")

        index = 0
        for letter in secret_word:
            if(trial==letter):
                print("Encontrei a letra {} na posição {}".format(trial,index))
            index = index + 1

        print("jogando...")

    print("Fim do jogo!")

if(__name__ == "__main__"):
    jogar()