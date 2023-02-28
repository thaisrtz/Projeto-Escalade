def jogar():
    print("*****************************")
    print ("Bem vindo ao jogo de forca")
    print("*****************************")

    secret_word = "banana"
    right_letters = ["_", "_", "_", "_", "_", "_"]

    defeat = False
    victory = False

    print(right_letters)
    while(not defeat and not victory):

        trial = input("Digite uma letra: ")
        trial = trial.strip( )

        index = 0
        for letter in secret_word:
            if(trial.upper()==letter.upper()):
               right_letters[index] = letter
            index = index + 1

        print(right_letters)

    print("Fim do jogo!")

if(__name__ == "__main__"):
    jogar()