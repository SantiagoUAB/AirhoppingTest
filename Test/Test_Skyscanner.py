import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import unittest
from unittest.mock import patch

from src.Skyscanner import Skyscanner



class TestSkyscanner(unittest.TestCase):

    def test_reserva_correcta(self):

        with patch('src.Skyscanner') as mock:
            mock.confirm_reserve.return_value = True
            self.assertTrue(mock.confirm_reserve())

    def test_conrimrar_reserva_error(self):
        with patch('src.Skyscanner') as mock_get:
            mock_get.confirm_reserve.return_value = False
        assert mock_get.confirm_reserve() == False
        print("Test_conrimrar_reserva_error")

if __name__ == '__main__':
    unittest.main()
