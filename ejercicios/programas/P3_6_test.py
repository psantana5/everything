import unittest
from unittest.mock import patch
from io import StringIO
from P3_6 import pedirPosicion
  
class TestP6(unittest.TestCase):

    @patch('P3_6.input', create=True)
    def test_entrada_correcta(self, mocked_input):
        mocked_input.side_effect = ['2 2']
        res = pedirPosicion()
        self.assertEqual(res, (1, 1))

    @patch('P3_6.input', create=True)
    def test_entrada_segunda(self, mocked_input):
        mocked_input.side_effect = ['0 2', '1 2']
        res = pedirPosicion()
        self.assertEqual(res, (0, 1))

    @patch('P3_6.input', create=True)
    def test_entrada_tercera(self, mocked_input):
        mocked_input.side_effect = ['0 2', 'patata 2', '30 2', '2', '3 3']
        res = pedirPosicion()
        self.assertEqual(res, (2, 2))

if __name__ == '__main__':
    unittest.main()