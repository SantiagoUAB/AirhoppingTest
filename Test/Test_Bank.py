import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import unittest
from unittest.mock import patch
from src.Bank import Bank
from src.User import User
from src.PaymentData import PaymentData


class TestBank(unittest.TestCase):

    def test_pago(self):

        with patch('src.Bank') as mock_Bank:

            mock_Bank.do_payment.return_value = True
            assert mock_Bank.do_payment() == True
            self.assertTrue(mock_Bank.do_payment())

    def test_metodo_pago(self):

        # datos usuario
        nombre = "Armando"

        # datos pago
        numTarjeta = 5581238443939998
        tipo_visa = PaymentData.tipo_VISA
        cvv = 117  # codigo seguridad tarjeta
        importe = 0

        datosPago = PaymentData(tipo_visa, nombre, numTarjeta, cvv, importe)



        assert datosPago.get_tipo_pago() == tipo_visa
        print("Test_metodo_pago ok")

    def test_pago_incorrecto(self):

        with patch('src.Bank') as mock_Bank:
            mock_Bank.do_payment.return_value = False

            assert mock_Bank.do_payment() == False
            print("Test_pago_incorrecto ok")


if __name__ == '__main__':
    unittest.main(exit=False)