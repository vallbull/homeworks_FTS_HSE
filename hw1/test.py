import unittest

from tic_tac_toe import *


class Test_TicTacToe(unittest.TestCase):

    def test_best_turn(self):
        field1 = [['X', '.', '.'],
                  ['.', 'X', '.'],
                  ['O', 'O', '.']]
        minimax(field1, 'X', 'O', 4, -1, -1, 0)
        assert field1 == [['X', '.', '.'],
                          ['.', 'X', '.'],
                          ['O', 'O', 'O']]
        field1 = [['X', 'X', '.'],
                  ['X', 'O', '.'],
                  ['O', 'O', '.']]
        minimax(field1, 'O', 'X', 3, -1, -1, 0)
        assert field1 == [['X', 'X', 'X'],
                          ['X', 'O', '.'],
                          ['O', 'O', '.']]

    def test_check_win(self):
        field1 = [['X', '.', '.'],
                  ['.', 'X', '.'],
                  ['O', 'O', 'X']]
        assert win_check(field1, 1, 1, 3) == 10
        assert win_check(field1, 1, 1, 3) != 0
        field1 = [['X', '.', '.'],
                  ['.', 'X', '.'],
                  ['O', 'O', 'X']]
        assert win_check(field1, 1, 2, 3) != 0
        assert win_check(field1, 1, 2, 3) != 10
        assert win_check(field1, 1, 2, 3) is None
        assert win_check(field1, 1, 1, 3) == 10

        field1 = [['X', 'O', 'X'],
                  ['O', 'X', 'X'],
                  ['O', 'X', 'O']]
        assert win_check(field1, 1, 2, 0) == 0
        assert win_check(field1, 2, 2, 0) == 0
        assert win_check(field1, 3, 1, 0) == 0
        assert win_check(field1, 2, 1, 0) == 0
        assert win_check(field1, 1, 2, 0) != 10
        assert win_check(field1, 2, 2, 0) != 10
        assert win_check(field1, 3, 1, 0) != 10
        assert win_check(field1, 2, 1, 0) != 10

        field1 = [['.', '.', '.'],
                  ['.', '.', '.'],
                  ['.', '.', '.']]
        assert win_check(field1, 2, 3, 9) is None


if __name__ == "__main__":
    unittest.main()
