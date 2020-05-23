

import unittest
from src.PaymentData import PaymentData


class TestBank(unittest.TestCase):

    def test_precio_cero(self):

        importe = 0
        datosPago = PaymentData(importe=importe)

        assert datosPago.get_importe() == 0  # coste de viaje 0
        print("Test_Viaje_Precio_Cero ok")


    def test_precio_viaje_esperado(self) -> None:

        importe = 0
        num_pasajeros = 3
        datosPago = PaymentData("VISA", "Paco", "123", 123, importe)

        lPrecios = [30, 30, 30]
        for precioDestino in lPrecios:
            datosPago.add_importe(precioDestino * num_pasajeros)
        importeEsperado = sum(lPrecios) * num_pasajeros

        assert datosPago.get_importe() == importeEsperado
        print("Test_precio_viaje_esperado ok")

    def test_precio_viaje_esperado_nuevos_destinos(self) -> None:
        importe = 0
        num_pasajeros = 3
        datosPago = PaymentData("VISA", "Paco", "123", 123, importe)

        lPrecios = [30, 30, 30]
        # se sumna el coste de cada destino en funcion del numero de pasajeos
        for precioDestino in lPrecios:
            datosPago.add_importe(precioDestino * num_pasajeros)

        # se suman 2 nuevos destinos
        datosPago.add_importe(30 * num_pasajeros)
        datosPago.add_importe(30 * num_pasajeros)

        lPrecios.append(30)
        lPrecios.append(30)

        importeEsperado = sum(lPrecios) * num_pasajeros

        assert datosPago.get_importe() == importeEsperado
        print("Test_precio_viaje_esperado_nuevos_destinos ok")

if __name__ == '__main__':
    unittest.main(exit=False)
