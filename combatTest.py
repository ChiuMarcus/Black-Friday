# Combat functions test
# Marcus Chiu
# A01034056
# 08 11 2018

from unittest import TestCase
from unittest.mock import patch

import gameplay
import game


class TestMethods(TestCase):

    def testDamagePlayer(self):
        char = game.create_character('Matt', 0, 0)
        enemy = {'name': 'Shopper', 'hp': 10}
        with patch('builtins.input', return_value='F') as _raw_input:
            gameplay.combat_round(char, enemy)
            self.assertLess(char['hp'], 10)

    def testDamageEnemy(self):
        char = game.create_character('Matt', 0, 0)
        enemy = {'name': 'Shopper', 'hp': 10}
        with patch('builtins.input', return_value='F') as _raw_input:
            gameplay.combat_round(char, enemy)
            self.assertLess(enemy['hp'], 10)

    def testCharDeath(self):
        char = game.create_character('Matt', 0, 0)
        char['hp'] = 0;
        self.assertEquals(gameplay.is_dead(char), 1)

    def testEnemyDeath(self):
        enemy = {'name': 'Shopper', 'hp': 0}
        self.assertEquals(gameplay.is_dead(enemy), 1)

    def testFight(self):
        char = game.create_character('Matt', 0, 0)
        enemy = {'name': 'Shopper', 'hp': 10}
        with patch('builtins.input', return_value='F') as _raw_input:
            gameplay.combat_round(char, enemy)
            self.assertTrue(char['hp'] < 10)

    def testFlee(self):
        char = game.create_character('Matt', 0, 0)
        enemy = {'name': 'Shopper', 'hp': 10}
        with patch('builtins.input', return_value='R') as _raw_input:
            gameplay.combat_round(char, enemy)
            self.assertGreaterEqual(char['hp'], 6)

