import unittest
from FarmGame import Farm
from FarmGame import FarmStock
from FarmGame import Planting
from FarmGame import Player
import WoWgame

# import unnecessary_math


class TestUM(unittest.TestCase):
    def setUp(self):
        pass

    def testFarmshop(self):
        # FarmStock.Wheat.buyWheatAmount(2)
        self.assertEqual((Player.Player.money - 30 ) ,  (Player.Player.money  - FarmStock.Wheat.buyPrice * 2))



        # else:
        #     unittest.FunctionTestCase.fail(self)


    # def test_strings_a_3(self):
    #     self.assertEqual(multiply('a', 3), 'aaa')


if __name__ == '__main__':
    unittest.main()