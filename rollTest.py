# Roll Test
# Marcus Chiu
# A01034056
# 08 11 2018

from unittest import TestCase

import gameplay


class TestMethods(TestCase):
    def test_rangeMin(self):
        self.assertGreaterEqual(gameplay.roll_die(6), 1)

    def test_rangeMax(self):
        self.assertLessEqual(gameplay.roll_die(6), 6)


