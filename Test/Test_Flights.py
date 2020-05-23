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

        self.datosPago = PaymentData("VISA", self.nombres[0], self.numTarjeta, self.cvv, self.costeViaje)

        self.num_pasajeros = 3
        self.num_destinos_eliminar = 2
        self.lDestinacion_vuelos = ["Metropolis", "Dinamarcia", "Suecia"]
        self.lCodigo_vuelos = [741, 852, 963]

        self.lDestinos_eliminar = self.lDestinacion_vuelos[:self.num_destinos_eliminar]
        self.lCodigos_vuelo_eliminar = self.lCodigo_vuelos[:self.num_destinos_eliminar]

    def test_Viaje_Numero_pasajeros(self):
        lVuelos = Flights(num_pasajeros=self.num_pasajeros)

        assert lVuelos.get_num_pasajeros() == self.num_pasajeros  # numero de paajeros esperados

    def test_viaje_sin_destinos(self):

        lVuelos = Flights()
        self.assertFalse(lVuelos.existen_Destinos())

    def test_Viase_Sin_Vuelos(self):

        lVuelos = Flights()

        assert lVuelos.existen_Vuelos() == False
        print("Test_Viase_Sin_Vuelos ok")

    def test_destinos_esperados(self):

        lVuelos = Flights(lDestiancions=self.lDestinacion_vuelos)

        assert lVuelos.get_destinos() == self.lDestinacion_vuelos

    def test_vuelos_esperados(self):

        lVuelos = Flights(lCodigos=self.lCodigo_vuelos)

        assert lVuelos.get_vuelos() == self.lCodigo_vuelos


    def test_viaje_eliminar_destinos(self) -> None:

        lVuelos = Flights(num_pasajeros=self.num_pasajeros)

        for destino in self.lDestinacion_vuelos:
            lVuelos.add_destino(destino)

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






if __name__ == '__main__':
    unittest.main()
