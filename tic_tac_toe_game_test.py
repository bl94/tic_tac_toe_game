import unittest
from tic_tac_toe_game import main,win_check

class TestTicTacToeGame(unittest.TestCase):
    def test_tic_toe_tac_game(self):
        self.assertEqual(main(),2)

if __name__=='__main__':
    unittest.main()