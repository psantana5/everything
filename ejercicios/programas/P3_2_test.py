import unittest
from unittest.mock import patch
from io import StringIO
from P3_2 import imprimirTablero
  
class TestP2(unittest.TestCase):
    tableroVacio = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    tablero1 = [["X", "O", "X"], [" ", "X", "O"], ["X", "O", "O"]]
    tablero2 = [["X", "O", "X"], [" ", " ", "O"], ["X", "O", "O"]]
    tablero3 = [["X", "O", "X"], ["O", "X", "O"], ["X", "O", "X"]]

    @patch('sys.stdout', new_callable=StringIO)
    def test_imprimir_tablero_vacio(self, mock_stdout):
        imprimirTablero(self.tableroVacio)
        esperado = "-------\n| | | |\n| | | |\n| | | |\n-------\n"
        self.assertEqual(mock_stdout.getvalue(), esperado)

    @patch('sys.stdout', new_callable=StringIO)
    def test_imprimir_tablero_1(self, mock_stdout):
        imprimirTablero(self.tablero1)
        esperado = """-------\n|X|O|X|\n| |X|O|\n|X|O|O|\n-------\n"""
        self.assertEqual(mock_stdout.getvalue(), esperado)
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_imprimir_tablero_2(self, mock_stdout):
        imprimirTablero(self.tablero2)
        esperado = "-------\n|X|O|X|\n| | |O|\n|X|O|O|\n-------\n"
        self.assertEqual(mock_stdout.getvalue(), esperado)

    @patch('sys.stdout', new_callable=StringIO)
    def test_imprimir_tablero_3(self, mock_stdout):
        imprimirTablero(self.tablero3)
        esperado = "-------\n|X|O|X|\n|O|X|O|\n|X|O|X|\n-------\n"
        self.assertEqual(mock_stdout.getvalue(), esperado)

if __name__ == '__main__':
    unittest.main()