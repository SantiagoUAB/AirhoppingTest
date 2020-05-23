import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import unittest
from src.Flights import Flights
from src.Skyscanner import Skyscanner
from src.User import User
from src.PaymentData import PaymentData



class TestFlights(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.nombres = ["Ana", "Bernardo", "Ramirez"]
        self.apellidos = ["Hurtado Hurtado", "Chaves Chaves", "Mateos"]
        self.DNI = ["08075225V", "02604904Q", "03897631M"]

        self.usuario = User(self.nombres[0], self.apellidos[0], self.DNI[0])

        self.numTarjeta = 5581238443939998
        self.cvv = 117  # codigo seguridad tarjeta
        self.costeViaje = 0



        self.num_pasajeros = 3
        self.num_destinos_eliminar = 2
        self.lDestinacion_vuelos = ["Metropolis", "Dinamarcia", "Suecia"]
        self.lCodigo_vuelos = [741, 852, 963]

        self.lDestinos_eliminar = self.lDestinacion_vuelos[:self.num_destinos_eliminar]
        self.lCodigos_vuelo_eliminar = self.lCodigo_vuelos[:self.num_destinos_eliminar]

        self.lDestinacion_vuelos = ["Metropolis", "Dinamarcia", "Suecia"]
        self.lPrecios = [30, 30, 30]

        self.lNuevos_destinos = ["Grieta", "Luxemburgo"]
        self.lNuevos_precios = [30, 30]



    def test_Viaje_Numero_pasajeros(self):
        lVuelos = Flights(num_pasajeros=self.num_pasajeros)

        assert lVuelos.get_num_pasajeros() == self.num_pasajeros  # numero de paajeros esperados

    def test_viaje_sin_destinos(self):

        lVuelos = Flights()
        self.assertFalse(lVuelos.existen_Destinos())

    def test_viaje_Sin_Vuelos(self):

        lVuelos = Flights()

        assert lVuelos.existen_Vuelos() == False
        print("Test_Viase_Sin_Vuelos ok")

    def test_destinos_esperados(self):

        lVuelos = Flights()

        for destino in self.lDestinacion_vuelos:
            lVuelos.add_destino(destino, 0)

        assert lVuelos.get_destinos() == self.lDestinacion_vuelos

    def test_vuelos_esperados(self):

        lVuelos = Flights(lCodigos=self.lCodigo_vuelos)

        assert lVuelos.get_vuelos() == self.lCodigo_vuelos


    def test_viaje_eliminar_destinos(self) -> None:

        lVuelos = Flights(num_pasajeros=self.num_pasajeros)

        for destino in self.lDestinacion_vuelos:
            lVuelos.add_destino(destino, 0)

        for destinoEliminar in self.lDestinos_eliminar:
            lVuelos.eliminar_destino(destinoEliminar)

        self.assertEqual(lVuelos.get_destinos(), ["Suecia"])

    def test_viaje_eliminar_vuelos(self) -> None:

        lVuelos = Flights(num_pasajeros=self.num_pasajeros)

        for vuelo in self.lCodigo_vuelos:
            lVuelos.add_vuelo(vuelo)

        # eliminar de listado de vuelos

        for vuelo in self.lCodigos_vuelo_eliminar:
            lVuelos.eliminar_vuelo(vuelo)

        self.assertEqual( lVuelos.get_vuelos(), [963])


    def test_destinos_precio_cero(self):

        vuelos = Flights()

        self.assertEqual(vuelos.get_total(), 0)  # coste de viaje 0

    def test_precio_viaje_esperado(self) -> None:

        vuelos = Flights(num_pasajeros=self.num_pasajeros)

        for destino, precio in zip(self.lDestinacion_vuelos, self.lPrecios):
            vuelos.add_destino(destino, precio)
        #calcular importe esperado
        importeEsperado = sum(self.lPrecios) * self.num_pasajeros

        assert vuelos.get_total() == importeEsperado

    def test_precio_viaje_esperado_nuevos_destinos(self) -> None:

        vuelos = Flights(num_pasajeros=self.num_pasajeros)

        for destino, precio in zip(self.lDestinacion_vuelos, self.lPrecios):
            vuelos.add_destino(destino, precio)

        for destino, precio in zip(self.lNuevos_destinos, self.lNuevos_precios):
            vuelos.add_destino(destino, precio)

        importeEsperado = sum(self.lPrecios) * self.num_pasajeros + sum(self.lNuevos_precios) * self.num_pasajeros
        assert vuelos.get_total() == importeEsperado

    def test_precio_viaje_esperado_eliminar_destinos(self) -> None:  # volveremos

        vuelos = Flights(num_pasajeros=self.num_pasajeros)

        for destino, precio in zip(self.lDestinacion_vuelos, self.lPrecios):
            vuelos.add_destino(destino, precio)

        # se elimian 2 destinos
        vuelos.eliminar_destino("Dinamarcia")
        vuelos.eliminar_destino("Suecia")

        # se descuetnan 2 destinos en el valor esperado
        lPrecios = [30, 0, 0]
        importeEsperado = sum(lPrecios) * self.num_pasajeros

        assert vuelos.get_total() == importeEsperado

        print("Test_precio_viaje_esperado_eliminar_destinos")

if __name__ == '__main__':
    unittest.main()
