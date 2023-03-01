import random


def jogar():

    print_opening_message()
    secret_word = secret_word_generator()
    right_letters = secret_right_letters(secret_word)

    defeat = False
    victory = False
    wrong_guess = 0

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
        print("A palavra secreta era: ", secret_word)

def print_opening_message():
    print("*****************************")
    print("Bem vindo ao jogo de forca")
    print("*****************************")

def secret_word_generator():
    archive = open("words.txt", "r")
    words = []
    for line in archive:
        line = line.strip()
        words.append(line)

    archive.close()

    num = random.randrange(0, len(words))
    secret_word = words[num].upper()
    return secret_word

def secret_right_letters(word):
    return ["_" for letter in word]

if (__name__ == "__main__"):
    jogar()