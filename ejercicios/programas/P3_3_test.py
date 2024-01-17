import unittest
from P3_3 import cambiarTurno
  
class TestP3(unittest.TestCase):

    def test_cambiar_turno(self):
        self.assertEqual(cambiarTurno("X"), "O")
        self.assertEqual(cambiarTurno("O"), "X")

if __name__ == '__main__':
    unittest.main()