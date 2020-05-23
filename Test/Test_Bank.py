from unittest.mock import patch
from src.Bank import Bank
from src.User import User
from src.PaymentData import PaymentData



def test_pago():


    with patch('src.Bank') as mock_Bank:

        mock_Bank.do_payment.return_value = True
        assert mock_Bank.do_payment() == True
        print("Test_pago_incorrecto ok")



def test_metodo_pago():

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

def test_pago_incorrecto():

    with patch('src.Bank') as mock_Bank:
        mock_Bank.do_payment.return_value = False

        assert mock_Bank.do_payment() == False
        print("Test_pago_incorrecto ok")

test_pago()
test_metodo_pago()
test_pago_incorrecto()