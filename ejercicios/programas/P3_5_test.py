import unittest
from P3_5 import comprobarGanador
  
class TestP5(unittest.TestCase):
    tableroVacio = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    tableroX = [["X", "O", "O"], ["X", "X", " "], ["X", " ", "O"]]
    tableroO = [["O", "X", "O"], ["X", "O", " "], ["O", " ", "X"]]
    tableroEmpate = [["O", "O", "X"], ["X", "X", "O"], ["O", "X", "X"]]
    tableroSigue = [["X", "O", "O"], [" ", "X", " "], [" ", " ", " "]]

    def test_sigue(self):
        self.assertTrue(comprobarGanador(self.tableroSigue))

    def test_gana_X(self):
        self.assertEqual(comprobarGanador(self.tableroX), "X")

    def test_gana_O(self):
        self.assertEqual(comprobarGanador(self.tableroO), "O")

    def test_empate(self):
        self.assertFalse(comprobarGanador(self.tableroEmpate))

    def test_vacio(self):
        self.assertTrue(comprobarGanador(self.tableroVacio))

    def test_todas_las_victorias(self):
        tablero = list(self.tableroVacio)

        # Filas
        tablero[0] = ["X", "X", "X"]
        self.assertEqual(comprobarGanador(tablero), "X")

        tablero[0] = [" ", " ", " "]
        tablero[1] = ["X", "X", "X"]
        self.assertEqual(comprobarGanador(tablero), "X")

        tablero[1] = [" ", " ", " "]
        tablero[2] = ["X", "X", "X"]
        self.assertEqual(comprobarGanador(tablero), "X")

        # Columnas
        tablero = list(self.tableroVacio)
        tablero[0][0] = "X"
        tablero[1][0] = "X"
        tablero[2][0] = "X"
        self.assertEqual(comprobarGanador(tablero), "X")

        tablero = list(self.tableroVacio)
        tablero[0][1] = "X"
        tablero[1][1] = "X"
        tablero[2][1] = "X"
        self.assertEqual(comprobarGanador(tablero), "X")

        tablero = list(self.tableroVacio)
        tablero[0][2] = "X"
        tablero[1][2] = "X"
        tablero[2][2] = "X"
        self.assertEqual(comprobarGanador(tablero), "X")

        # Diagonales
        tablero = list(self.tableroVacio)
        tablero[0][0] = "X"
        tablero[1][1] = "X"
        tablero[2][2] = "X"
        self.assertEqual(comprobarGanador(tablero), "X")

        tablero = list(self.tableroVacio)
        tablero[0][2] = "X"
        tablero[1][1] = "X"
        tablero[2][0] = "X"
        self.assertEqual(comprobarGanador(tablero), "X")



if __name__ == '__main__':
    unittest.main()