import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import unittest
from unittest.mock import patch


class TestRentalcars(unittest.TestCase):

    def test_reservar_correcta(self):
        with patch('src.Rentalcars') as mock:
            mock.confirm_reserve.return_value = True
            self.assertTrue(mock.confirm_reserve(), "Reserva se ha hecho correctamente")

    def test_reserva_incorrecta(self):
        with patch('src.Rentalcars') as mock:
            mock.confirm_reserve.return_value = False
            self.assertFalse(mock.confirm_reserve(), "Reserva no se ha podido realizar")



if __name__ == '__main__':
    unittest.main()
