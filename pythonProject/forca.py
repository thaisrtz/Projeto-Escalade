def jogar():
    print("*****************************")
    print("Bem vindo ao jogo de forca")
    print("*****************************")

    secret_word = "maca".upper()
    right_letters = []

    defeat = False
    victory = False
    wrong_guess = 0

    for letter in secret_word:
        right_letters.append("_")

    print(right_letters)
    while (not defeat and not victory):

        guess = input("Digite uma letra: ")
        guess = guess.strip().upper()

        if(guess in secret_word):
            index = 0
            for letter in secret_word:
                if (guess == letter):
                    right_letters[index] = letter
                index += 1

        else:
            wrong_guess += 1
            print ("Você errou! Restam {} tentativas.".format(6-wrong_guess))

        defeat = wrong_guess == 6
        victory = "_" not in right_letters
        print(right_letters)

    print("Fim do jogo!")
    if (victory):
          print("Você ganhou!")
    if (defeat):
          print ("Você perdeu!")


if (__name__ == "__main__"):
    jogar()
