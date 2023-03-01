import random

def jogar():

    print_opening_message()
    secret_word = secret_word_generator()
    right_letters = secret_right_letters(secret_word)
    print(right_letters)

    defeat = False
    victory = False
    wrong_guess = 0

    while (not defeat and not victory):

        guess = receiving_guess()

        if(guess in secret_word):
            right_guess_marker(guess, right_letters, secret_word)

        else:
            wrong_guess += 1
            print ("Você errou! Restam {} tentativas.".format(6-wrong_guess))

        defeat = wrong_guess == 6
        victory = "_" not in right_letters
        print(right_letters)

    if (victory):
        print_victory_message()
    if (defeat):
        print_defeat_message()

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

def receiving_guess():
    guess = input("Digite uma letra: ")
    guess = guess.strip().upper()
    return guess

def right_guess_marker(guess, right_letters, secret_word):
    index = 0
    for letter in secret_word:
        if (guess == letter):
            right_letters[index] = letter
        index += 1

def print_victory_message():
    print("Você ganhou!")

def print_defeat_message():
    print("Você perdeu!")
    print("A palavra secreta era: ", secret_word)

if (__name__ == "__main__"):
    jogar()