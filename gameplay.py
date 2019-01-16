# Gameplay
# Marcus Chiu
# A01034056
# 23 11 2018

# This module contains the functions directly related to gameplay, such as movement and combat.


import random

# These are constants representing the dimension of the dungeon.
map_w = 5
map_h = 5


def roll_die(sides):
    """
    Returns a number representing the total value obtained from rolling a die with a defined number of sides.
    PARAM: integer
    PRECONDITION: side_num must be a positive integer
    POSTCONDITION: Returns an integer between side_num and side_num * roll_num
    """
    total = random.randint(1, sides)
    return total


def move(char, direction):
    """Moves the character around the dungeon.
    PARAM: A dictionary, a string
    PRECONDITION: Character must be valid, direction must be either N, S, E or W.
    POSTCONDITION: The character's position will either move one position in the specified direction, or prints an
        error message if invaid.
        RETURN: None
        """
    north = ['north', 'North', 'n', 'N']
    south = ['south', 'South', 's', 'S']
    east = ['east', 'East', 'e', 'E']
    west = ['west', 'West', 'w', 'W']
    if direction in north:
        dir_valid(char, 'N')
    elif direction in south:
        dir_valid(char, 'S')

    elif direction in east:
        dir_valid(char, 'E')
    elif direction in west:
        dir_valid(char, 'W')
    else:
        print("That is not a valid direction")
    return


def dir_valid(char, point):
    """
    Checks if the direction you move to is valid, and move you if it is.
    PARAMETER: char
    PRECONDITION: point must be N, S, E or W.
    POSTCONDITION: Player character either moves one space in the indicated direction, or is informed that they
    cannot move that way.
    RETURN: None
    """
    if point == 'S' and (char['y-pos'] + 1) < map_h:
        char['y-pos'] += 1
        enemy_roll(char)
    elif point == 'E' and (char['x-pos'] + 1) < map_w:
        char['x-pos'] += 1
        enemy_roll(char)
    elif point == 'N' and (char['y-pos'] - 1) >= 0:
        char['y-pos'] -= 1
        enemy_roll(char)
    elif point == 'W' and (char['x-pos'] - 1) >= 0:
        char['x-pos'] -= 1
        enemy_roll(char)
    else:
        print("You cannot go that way")
    return


def enemy_roll(char):
    """Rolls a 10-sided die, and either creates a monster to fight if the value rolled is 1 (i.e. a monster has spawned),
    or heals the player for 1 hp if the character is under full health.
    PARAM: None
    PRECONDITION: None
    POSTCONDITION: Creates a monster and initiates combat or heals the player for 1 hp if they are under
    full health.
    RETURN: None
    """
    if roll_die(10) == 1:
        enemy = {'name': 'Black Friday Shopper', 'hp': 10}
        combat_round(char, enemy)
    else:
        if char['hp'] < 10:
            char['hp'] += 1
    return


def damage_calc(char):
    """Calculates the damage done to a char2 by an char1, damage is calculated by a dice roll.
   PARAM: attack_class, the attacker's class, and char2, a character sheets
   PRECONDITION: Both inputs are well-formed.
   POSTCONDITION: Reduces the HP by the rolled value.
   RETURN: None"""

    damage = roll_die(6)
    char['hp'] -= damage
    print(char['name'] + " is struck for ", damage, "damage.")
    return


def is_dead(char):
    """Determines if a character is dead
       PARAM: a dictionary representing a character or monster
       PRECONDITION: Input is a well formed character class
       POSTCONDITION: returns 1 if the character's hp is 0 or lower, and 0 otherwise
       RETURN: integer"""
    if char['hp'] <= 0:
        print(char['name'] + " is knocked out!")
        return 1
    else:
        return 0


def combat_round(char1, char2):
    """Simulates a single round of combat
    PARAM: char1 and char2, character sheets
    PRECONDITION: Inputs are both character sheets created by generate_charsheet
    POSTCONDITION: Prints message if one character dies
    RETURN: None"""
    global game
    print("What will you do?")
    choice = input("Type F to fight or R to flee")
    if choice == "F" or choice == "f":
        damage_calc(char2)
        if is_dead(char2) == 1:
            return
        print(char2['name'] + "'s remaining HP: ", char2['hp'], "/10")
        print("It's " + char2['name'] + "'s turn!")
        damage_calc(char1)
        if is_dead(char1) == 1:
            print("GAME OVER")
            game = False
            return
        print(char1['name'] + "'s remaining HP: ", char1['hp'], "/10")
        print("On to the next round!")
        return combat_round(char1, char2)
    elif choice == "R" or choice == '"r':
        if roll_die(10) == 1:
            print(char2['name'] + " launched a sneak attack on " + char1['name'] + "!")
            char1['hp'] -= roll_die(4)
            print(char1['name'] + "'s remaining HP: ", char1['hp'], "/10")
        if is_dead(char1) == 1:
            print("GAME OVER")
            game = False
            return
        else:
            print(char1['name'] + " ran away!")
            return
    else:
        print("That is not a valid command.")
        combat_round(char1, char2)