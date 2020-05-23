import unittest
from src.Hotel import Hotel
from src.Hotels import Hotels
from src.User import User

class TestHotels(unittest.TestCase):
    def setUp(self) -> None:


        self.hotel = Hotel(1234,'Royal Palace',5,2,7,50)
        self.hotels = Hotels()


        self.hotels.añadir_hotel(self.hotel)

    def test_viaje_añadir_alojamiento(self):


        self.assertEqual(50,self.hotels.getpreciototal())

    def test_viaje_eliminar_alojamiento(self):

        hotel = Hotel(4321,'Port Aventura Hotel', 5,2,4,100)
        hotel2 = Hotel(4321, 'Port Aventura Hotel', 5, 2, 4, 200)

        self.hotels.añadir_hotel(hotel)
        self.hotels.añadir_hotel(hotel2)

        self.hotels.eliminar_hotel(hotel)
        self.hotels.eliminar_hotel(hotel2)

        self.assertEqual(50,self.hotels.getpreciototal())