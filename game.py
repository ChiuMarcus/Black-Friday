# Black Friday Game
# Marcus Chiu
# A01034056
# 08 11 2018

# This file contains functions not directly related to gameplay: The main game function, the file save and load functons
# and the character creation module.


import json
import time
import sys
import gameplay

# These are constants representing the dimension of the dungeon.
map_w = 5
map_h = 5


def delay_print(s):
    """A helper function that prints the input string s at a slower rate
    PARAM: string s
    PRECONDITIONS: Input must be a string
    POSTCONDITION: string is printed out with a 50ms delay between each word."""
    for word in s:
        sys.stdout.write(word)
        sys.stdout.flush()
        time.sleep(0.05)
    print("\n")


def game_map(char, row, col):
    """Displays a map and character position within the map.
    PARAM: char, row, column
    PRECONDITION: char is well formed
    POSTCONDITION: Displays a map of size row x col, with the char's position shown in the map"""
    for i in range(0, row):
        for j in range(0, col):
            if i == 0 and j == 0:
                if char['present']:
                    print("[E]", end="")
                elif i == char['y-pos'] and j == char['x-pos']:
                    print("[P]", end="")
                else:
                    print("[.]", end="")
            elif i == char['y-pos'] and j == char['x-pos']:
                print("[P]", end="")
            else:
                print("[.]", end="")
        print('\n')
    return


def save_char(char):
    """Saves the character state to a json file.
    PARAM: Dictionary
    PRECONDITION: Character dictionary is well-formed.
    POSTCONDITION: A json file with the character name as its title, and the character information stored inside."""
    save_file = char['name'] + '.json'
    with open(save_file, 'w') as fp:
        json.dump(char, fp)
    return


def create_character(name, xpos, ypos):
    """Creates and returns a basic Character profile.
    PARAM: Character String
    PRECONDITION: String must contain at least one letter.
    POSTCONDITION: Returns a dictionary containing the character's name, the character's starting HP and the starting
    position within the dungeon."""
    if len(name) <= 0:
        print("Error: Please enter a valid name")
        return
    else:
        character = {'name': name, 'hp': 10, 'x-pos': xpos, 'y-pos': ypos, 'present': False}
        return character


def intro_text():
    """Prints the introductory exposition
    PARAM: None
    PRECONDITION: None
    POSTCONDITION: None"""
    print("\n ==========")  # Plays the introduction if they have not played before.
    delay_print("November 23rd 2018. Black Friday")
    delay_print(
        "Standing before the sealed dorway of the Mall, You shiver as a gust of cold autumn air hits your face.")
    delay_print(
        "Once again, you glance at the time on your phone: 5:59am. You've been standing here for almost two "
        "hours now.")
    delay_print("Still, losing a few hours of sleep is a small price to pay in order to achieve your goal:")
    delay_print(
        "The latest Nintendo Switch Game everyone's been hyped about. Today is the first day it's available in "
        "stores and you think it would make the perfect Christmas gift.")
    delay_print(
        "And it seems everyone else seems to agree, because the crowd here is ridiculously large. You think "
        "it's almost twice the size of last year's Black Friday sale.")
    delay_print(
        "The clock strikes six. A metallic rattle echoes and you snap to attentjon as the metal shutters rise "
        "up and the doors are opened.")
    delay_print("Like a living wave, the shoppers burst into the mall, intent on getting their gifts at any cost.")
    delay_print("Your mission is clear: Find the game store, buy the game and get out of here alive.")
    delay_print("Good luck, shopper. May the odds be in your favor.")
    print("==========\n")


def game_init():
    """Asks the player if they have already made a character, and either loads an existing character from the json
    file, or creates a new character and save file.
    PARAM: None
    PRECONDITIONS: None
    POSTCONDITION: Returns a well-formed character dictionary."""
    f_exists = True
    while f_exists:
        load_game = input("Have you played this game before? (y/n)")  # Asks user if they have an existing save file
        if load_game == "y" or load_game == "Y":
            file_name = input("Please enter your character's name: ") + ".json"
            try:
                with open(file_name, 'r') as charfile:  # Finds the corresponding save file and opens it.
                    character = json.load(charfile)
                    delay_print("Your mission is clear: Find the game store, buy the game and get out of here alive.\n")
                    return character
            except IOError:
                print("Error: The file does not seem to exist\n")

        # Reminds the player of their objective upon loading the game.
        elif load_game == 'N' or load_game == 'n':
            charname = input("Please enter a name for your character: ")
            character = create_character(charname, 0, 0)  # Creates a new character profile.
            save_char(character)  # Saves the new character in case they die before saving or quitting.
            intro_text()  # Prints the introduction text if you are a new player.
            # No need to read the introduction again if you have played before.
            return character
        else:
            print("I didn't understand that, please try again.\n")


def game():
    """The main function that calls on other functions to start the game. Will keep the user in a while loop until
    the player character wins or is knocked out.
    PARAM: None
    PRECONDITIONS: None
    POSTCONDITION: None"""
    delay_print("\n Welcome to: ")
    print("      ____  __    ___   ________ __    __________  ________  _____  __")
    print("     / __ )/ /   /   | / ____/ //_/   / ____/ __ \/  _/ __ \/   \ \/ /")
    print("    / __  / /   / /| |/ /   / ,<     / /_  / /_/ // // / / / /| |\  /")
    print("   / /_/ / /___/ ___ / /___/ /| |   / __/ / _, _// // /_/ / ___ |/ /")
    print("  /_____/_____/_/  |_\____/_/ |_|  /_/   /_/ |_/___/_____/_/  |_/_/")
    print("                                                                   ")
# Ascii art made using the generator: http://patorjk.com/software/taag/
    global game
    character = game_init() # Initializes the game setting by either loading a character or creating  a new
    # character and printing the introductory text.
    game = True
    while game:
        if character['x-pos'] == map_w - 1 and character['y-pos'] == map_h - 1 and character['present'] is False:
            character['present'] = True
            delay_print("With a cry of triumph, you walk out of the store, prize in hand. Now comes the last leg of "
                        "your quest: ")
            delay_print("Make it back to the exit alive. (press M to view the exit on the map)")
        elif character['x-pos'] == 0 and character['y-pos'] == 0 and character['present']:
            game = False
            print("\n==== VICTORY! ====")
            delay_print("You stagger out of the mall exhausted and ruffled, but triumphant.")
            delay_print("You survived the Black Friday horde, and managed to buy your present as well!")
            delay_print("Your victory high is broken by the sound of your alarm, prompting you to sprint frantically "
                        "to your car: Class starts in 30 minutes, and you can't afford to be late!")
        else:
            print("Type M to view the map. If you wish to stop playing, type Q. If you want to save your game, "
                  "type save")
            command = input("What do you want to do?")
            if command == "M" or command == 'm':
                game_map(character, map_w, map_h)
            elif command == "Q" or command == 'q':
                save_char(character)
                game = False
            elif command == 'save':
                save_char(character)
                print("Progress has been saved.")
            else:
                gameplay.move(character, command)
    return


def main():
    game()


if __name__ == "__main__":
    main()
    print("\n")

