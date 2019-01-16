# Move Test
# Marcus Chiu
# A01034056
# 23 11 2018

from unittest import TestCase
from unittest.mock import patch


import gameplay
import game


class TestMethods(TestCase):
    # Note: Mock inputs are there in case the enemy roll function succeeds in spawning an enemy.
    # In which case, the character will flee the encounter and survive.
    def testMoveNorthPass(self):
        char = game.create_character('Matt', 0, 3)
        with patch('builtins.input', return_value='R') as _raw_input:
            gameplay.dir_valid(char, 'N')
            self.assertEqual(char['y-pos'], 2)

    def testMoveNorthFail(self):
        char = game.create_character('Matt', 0, 0)
        with patch('builtins.input', return_value='R') as _raw_input:
            gameplay.dir_valid(char, 'N')
            self.assertEqual(char['y-pos'], 0)

    def testMoveSouthPass(self):
        char = game.create_character('Matt', 0, 0)
        with patch('builtins.input', return_value='R') as _raw_input:
            gameplay.dir_valid(char, 'S')
            self.assertEqual(char['y-pos'], 1)

    def testMoveSouthFail(self):
        char = game.create_character('Matt', 0, 4)
        with patch('builtins.input', return_value='R') as _raw_input:
            gameplay.dir_valid(char, 'S')
            self.assertEqual(char['y-pos'], 4)

    def testMoveEastPass(self):
        char = game.create_character('Matt', 0, 0)
        with patch('builtins.input', return_value='R') as _raw_input:
            gameplay.dir_valid(char, 'E')
            self.assertEqual(char['x-pos'], 1)

    def testMoveEastFail(self):
        char = game.create_character('Matt', 4, 0)
        with patch('builtins.input', return_value='R') as _raw_input:
            gameplay.dir_valid(char, 'E')
            self.assertEqual(char['x-pos'], 4)

    def testMoveWestPass(self):
        char = game.create_character('Matt', 3, 0)
        with patch('builtins.input', return_value='R') as _raw_input:
            gameplay.dir_valid(char, 'W')
            self.assertEqual(char['x-pos'], 2)

    def testMoveWestFail(self):
        char = game.create_character('Matt', 0, 0)
        with patch('builtins.input', return_value='R') as _raw_input:
            gameplay.dir_valid(char, 'W')
            self.assertEqual(char['x-pos'], 0)