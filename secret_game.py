import os
import random
import sys
from time import sleep
#Secret Game

def start():
    print("""
     ____      ____      __                                       _             _   __               ______                                _       ______                             _ 
    |_  _|    |_  _|    [  |                                     / |_          / |_[  |            .' ____ \                              / |_   .' ___  |                           | |
      \ \  /\  / /.---.  | |  .---.   .--.   _ .--..--.  .---.  `| |-' .--.   `| |-'| |--.  .---.  | (___ \_| .---.  .---.  _ .--.  .---.`| |-' / .'   \_|  ,--.   _ .--..--.  .---. | |
       \ \/  \/ // /__\\\ | | / /'`\]/ .'`\ \[ `.-. .-. |/ /__\\  | | / .'`\ \  | |  | .-. |/ /__\\  _.____`. / /__\\/ /'`\][ `/'`\]/ /__\\| |   | |   ____ `'_\ : [ `.-. .-. |/ /__\\| |
        \  /\  / | \__., | | | \__. | \__. | | | | | | || \__.,  | |,| \__. |  | |, | | | || \__., | \____) || \__.,| \__.  | |    | \__.,| |,  \ `.___]  |// | |, | | | | | || \__.,|_|
         \/  \/   '.__.'[___]'.___.' '.__.' [___||__||__]'.__.'  \__/ '.__.'   \__/[___]|__]'.__.'  \______.' '.__.''.___.'[___]    '.__.'\__/   `._____.' \'-;__/[___||__||__]'.__.'(_)
    """)

def end():
    bye = "Thanks for playing with me, you're a good friend!"
    for char in bye:
        sys.stdout.write(char)
        sleep(0.1)
    print()
    print("""
    ,---.            . .                ,--,--'.           .                          .                    /\\")
    |  -'  ,-. ,-. ,-| |-. . . ,-.      `- |   |-. ,-. ,-. | , ,-.   ,'' ,-. ,-.  ,-. |  ,-. . . . ,-. ,-. )( ")
    |  ,-' | | | | | | | | | | |-'       , |   | | ,-| | | |<  `-.   |- | | |     | | |  ,-| | | | | | | | \/ ")
    `---|  `-' `-' `-^ ^-' `-| `-' :;    `-'   ' ' `-^ ' ' ' ` `-'   |  `-' '     |-' `' `-^ `-| ' ' ' `-| :; ")
     ,-.|                   /|                                       '            |           /|        ,|    ")
     `-+'                  `-'                                                    '          `-'        `'    ")
    """)

def confirm(question):
    while True:
        answer = input(question + " (y/n)")
        answer = answer.lower()
        if "y" in answer:
            return True
        elif "n" in answer:
            return False

def get_puzzle(name):
    music = "I like music " + str(name) + ", so the category will be musical instruments."
    for char in music:
        sys.stdout.write(char)
        sleep(0.1)
    print()
    words = ["xylophone", "marimba", "trumpet", "flute", "clarinet", "baritone", "snare", "bass", "tenors", "saxophone", "mellophone", "tuba"]
    randnum = random.randint(0, len(words) - 1)
    puzzle = words[randnum]
    return puzzle

def get_strikes():
    strikes = 0
    limit = 6
    strikesleft = limit - strikes
    return strikesleft
    
def get_solved(puzzle, guesses):
    solved = ""

    for letter in puzzle:
        if letter in guesses:
            solved += letter
        else:
            solved += "-"

    return solved

def get_name():
        tell = ("Since we're friends now, you should tell me your name.")
        for char in tell:
            sys.stdout.write(char)
            sleep(0.2)
        print()
        
        name = input()
        return name
 
def get_guess(guesses, name):
        letter = input("Guess a letter, " + str(name) + ": ")
        
        if len(letter) > 1:
            one = ("please guess only one letter " + str(name) + ".")
            for char in one:
                sys.stdout.write(char)
                sleep(0.1)
            print()
        elif letter == '' or letter == ' ':
            letter = ("You need to enter a letter, " + str(name) + ".")
            for char in letter:
                sys.stdout.write(char)
                sleep(0.1)
            print()
        elif letter not in "abcdefghijklmnopqrstuvwxyz":
            letter2 = ("You must enter a letter " + str(name) + ".")
            for char in letter2:
                sys.stdout.write(char)
                sleep(0.1)
            print()
        elif letter in guesses:
            repeat = ("You have already entered that letter " + str(name) + ".")
            for char in repeat:
                sys.stdout.write(char)
                sleep(0.1)
            print()
        else:
            return letter
        
def display_board(solved, guesses, strikesleft):
    print(solved, [guesses])
    print()
    tries = ("You have " + str(strikesleft) + " tries left.")
    for char in tries:
        sys.stdout.write(char)
        sleep(0.1)
    print()
    print()
    
def show_result(solved, puzzle, name, strikes):
        if solved == puzzle:
            win = ("Hey you did it! I'm proud of you :)")
            for char in win:
                sys.stdout.write(char)
                sleep(0.1)
            print()
        elif strikes >= 6:
            loss =("Oh...sorry. I guess you lost.")
            for char in loss:
                sys.stdout.write(char)
                sleep(0.1)
            print()
            
def play():
    name = get_name()
    puzzle = get_puzzle(name)
    strikesleft = get_strikes()
    guesses = ""
    solved = get_solved(puzzle, guesses)
    display_board(solved, guesses, strikesleft)

    limit = 6
    strikes = 0

    while solved != puzzle:
        letter = get_guess(guesses, name)

        if (len(str(letter)) > 1) or (letter == '' or letter == ' ') or (letter not in "abcdefghijklmnopqrstuvwxyz") or (letter in guesses):
            strikes != strikes + 1
            
        if str(letter) not in puzzle:
            strikesleft = limit - strikes - 1
            strikes += 1
            
        guesses += str(letter)
        solved = get_solved(puzzle, guesses)
        display_board(solved, guesses, strikesleft)

    show_result(solved, puzzle, name, strikes)

def main():    
    start()

    playing = True

    while playing:
        play()
        playing = confirm("Would you like to play again?")

    end()

if __name__ == "__main__":
    main()
