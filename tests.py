import unittest

from chess import bishop, knight, queen, rook


class ChessTest(unittest.TestCase):

    def test_queen(self):
        result = queen(4)
        self.assertEqual(2, result)

    def test_rook(self):

        result = rook(3)
        self.assertEqual(6, result)

    def test_bishop(self):
        result = bishop(3)
        self.assertEqual(26, result)        
        result = bishop(2)
        self.assertEqual(4, result)

    def test_knight(self):
        result = knight(2)
        self.assertEqual(16, result)


if __name__ == '__main__':
    unittest.main()
