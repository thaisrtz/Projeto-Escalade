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
            hangman_drawing(wrong_guess)

        defeat = wrong_guess == 6
        victory = "_" not in right_letters
        print(right_letters)

    if (victory):
        print_victory_message()
    else:
        print_defeat_message(secret_word)

    input("Enter para sair")

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

def hangman_drawing(wrong_guess):
    print("  _______     ")
    print(" |/      |    ")

    if(wrong_guess == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(wrong_guess == 2):
        print(" |      (_)   ")
        print(" |       |    ")
        print(" |       |    ")
        print(" |            ")

    if(wrong_guess == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |       |    ")
        print(" |            ")

    if(wrong_guess == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(wrong_guess == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (wrong_guess == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")
    print(" |            ")
    print("_|___         ")
    print()
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
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def print_defeat_message(secret_word):
    print("A palavra secreta era: ", secret_word)
    print("Puxa, você foi enforcado!")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print(" /                   \      ")
    print(" /                   \    ")
    print(" }  XXXXX     XXXXX  {    ")
    print(" |  XXXXX     XXXXX  |      ")
    print(" |   XXX       XXX   |      ")
    print(" |         A         |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I_I_I_I_I_I_I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

if (__name__ == "__main__"):
    jogar()