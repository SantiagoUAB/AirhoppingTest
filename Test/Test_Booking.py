import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import unittest
from unittest.mock import patch

from src.Booking import Booking

class TestBooking(unittest.TestCase):

    @classmethod
    def setUp(self) -> None:
        self.pathBooking = 'src.Booking'
        self.mensaje_OK = "Reserva se ha hecho correctamente"
        self.mensaje_FAIL = "Reserva no se ha podido realizar"

    def test_reservar_correcta(self):

        with patch(self.pathBooking) as mock:
            mock.confirm_reserve.return_value = True
            self.assertTrue(mock.confirm_reserve(), self.mensaje_OK)

    def test_reserva_incorrecta(self):
        with patch(self.pathBooking) as mock:
            mock.confirm_reserve.return_value = False
            self.assertFalse(mock.confirm_reserve(), self.mensaje_FAIL)


if __name__ == '__main__':
    unittest.main()
