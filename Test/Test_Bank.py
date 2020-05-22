from unittest.mock import patch
from src.Bank import Bank
from src.User import User
from src.PaymentData import PaymentData



def Test_pago():

    #datos usuario
    nombre ="Armando"
    apellidos = "Guerrra Segura"
    DNI = '88499756B'

    #datos pago
    numTarjeta = 5581238443939998
    tipo_visa = PaymentData.tipo_VISA
    cvv = 117  # codigo seguridad tarjeta
    importe = 0

    bank = Bank()

    usuario = User(nombre, apellidos, DNI)

    datosPago = PaymentData(tipo_visa, nombre, numTarjeta, cvv,  importe)

    assert bank.do_payment(usuario, datosPago) == True
    print("Test_pagament ok")

def Test_metodo_pago():

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

def Test_pago_incorrecto():
    """
    # datos usuario
    nombre = "Armando"
    apellidos = "Guerrra Segura"
    DNI = '88499756B'

    # datos pago
    numTarjeta = 5581238443939998
    tipo_visa = PaymentData.tipo_VISA
    cvv = 117  # codigo seguridad tarjeta
    importe = 0

    bank = Bank()

    usuario = User(nombre, apellidos, DNI)

    datosPago = PaymentData(tipo_visa, nombre, numTarjeta, cvv, importe)
    """
    with patch('src.Bank') as mock_Bank:
        mock_Bank.do_payment.return_value = False

    assert mock_Bank.do_payment() == False
    print("Test_pago_incorrecto ok")

Test_pago()
Test_metodo_pago()
Test_pago_incorrecto()