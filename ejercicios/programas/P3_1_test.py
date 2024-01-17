import unittest
from P3_1 import nuevoTablero
  
class TestP1(unittest.TestCase):
    tableroVacio = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    def test_nuevo_tablero(self):
        self.assertEqual(nuevoTablero(), self.tableroVacio)

if __name__ == '__main__':
    unittest.main()