

import unittest
from src.PaymentData import PaymentData
from src.Factura import Factura


class TestFactura(unittest.TestCase):

    @classmethod
    def setUp(self) -> None:

        self.lDestinacion_vuelos = ["Metropolis", "Dinamarcia", "Suecia"]
        self.lPrecios = [30, 30, 30]

        self.lNuevos_destinos = ["Grieta" , "Luxemburgo"]
        self.lNuevos_precios = [30,30]

        self.num_pasajeros = 3



    def test_precio_cero(self):

        factura = Factura()

        self.assertEqual(factura.get_total(), 0)  # coste de viaje 0

    def test_precio_viaje_esperado(self) -> None:

        factura = Factura(num_pasajeros=self.num_pasajeros)

        for destino, precio in zip(self.lDestinacion_vuelos, self.lPrecios):
            factura.add_destino(destino, precio)
        #calcular importe esperado
        importeEsperado = sum(self.lPrecios) * self.num_pasajeros

        assert factura.get_total() == importeEsperado


    def test_precio_viaje_esperado_nuevos_destinos(self) -> None:

        factura = Factura(num_pasajeros=self.num_pasajeros)

        for destino, precio in zip(self.lDestinacion_vuelos, self.lPrecios):
            factura.add_destino(destino, precio)

        for destino, precio in zip(self.lNuevos_destinos, self.lNuevos_precios):
            factura.add_destino(destino, precio)

        importeEsperado = sum(self.lPrecios)* self.num_pasajeros + sum(self.lNuevos_precios )* self.num_pasajeros
        assert factura.get_total() == importeEsperado


    def test_precio_viaje_esperado_eliminar_destinos(self) -> None:  # volveremos

        factura = Factura(num_pasajeros=self.num_pasajeros)

        for destino, precio in zip(self.lDestinacion_vuelos, self.lPrecios):
            factura.add_destino(destino, precio)

        # se elimian 2 destinos
        factura.eliminar_destino("Dinamarcia")
        factura.eliminar_destino("Suecia")

        # se descuetnan 2 destinos en el valor esperado
        lPrecios = [30, 0, 0]
        importeEsperado = sum(lPrecios) * self.num_pasajeros

        assert factura.get_total() == importeEsperado

        print("Test_precio_viaje_esperado_eliminar_destinos")


if __name__ == '__main__':
    unittest.main(exit=False)
