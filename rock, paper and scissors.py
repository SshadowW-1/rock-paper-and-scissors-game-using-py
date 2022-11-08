# Building Rock, Paper and Scissor Game

import random
name = input("Input your name player : ")
print(f"Welcome ,{name.title()} to the game.")


def game():
    user_input = input("Enter your choice. (R) For Rock, (P) For Paper and (S) For scissor :  ")
    computer_input = random.choice(['r', 'p', 's'])
    if user_input == computer_input:
        return "It's tie"

    if win(user_input, computer_input):
        return "You Won "

    return "You lost"


def win(player, opponent):
    if player == "r" and opponent == "s" or player == "p" and opponent == "r" or player == "s" and opponent == "p":
        return True


def play_again():
    while True:
        play = input("Do you want to play again ?(y/n): ")
        if play == "y":
            print(game())
        else:
            print("You have exited the game.")
            break


print(game())
play_again()
