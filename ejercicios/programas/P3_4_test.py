import unittest
from P3_4 import colocarFicha
  
class TestP4(unittest.TestCase):
    tablero = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    tableroLleno = [["X", "O", "O"], [" ", "X", " "], ["X", " ", "O"]]

    def test_casilla_vacia(self):
        self.assertTrue(colocarFicha(self.tablero, (1, 1), "X"))
        self.assertEqual(self.tablero, [[" ", " ", " "], [" ", "X", " "], [" ", " ", " "]])
        self.assertTrue(colocarFicha(self.tablero, (0, 1), "O"))
        self.assertEqual(self.tablero, [[" ", "O", " "], [" ", "X", " "], [" ", " ", " "]])

    def test_casilla_ocupada(self):
        self.assertFalse(colocarFicha(self.tableroLleno, (1, 1), "X"))
        self.assertEqual(self.tableroLleno, [["X", "O", "O"], [" ", "X", " "], ["X", " ", "O"]])
        self.assertFalse(colocarFicha(self.tableroLleno, (1, 1), "O"))
        self.assertEqual(self.tableroLleno, [["X", "O", "O"], [" ", "X", " "], ["X", " ", "O"]])

if __name__ == '__main__':
    unittest.main()