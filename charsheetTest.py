# Char Sheet Test
# Marcus Chiu
# A01034056
# 08 11 2018

from unittest import TestCase
import game


class TestMethods(TestCase):
    char = game.create_character("Olivia", 0, 0)
    assert len(char['name']) == 6

    def testInitHealth(self):
        char = game.create_character("Jane", 0, 0)
        self.assertTrue(char['hp'] == 10)

    def testInitXPos(self):
        char = game.create_character("Chris", 0, 0)
        self.assertTrue(char['x-pos'] == 0)

    def testInitYPos(self):
        char = game.create_character("Sean", 0, 0)
        self.assertTrue(char['y-pos'] == 0)

    def testPresent(self):
        char = game.create_character("Dan", 0, 0)
        self.assertTrue(char['present'] is False)
