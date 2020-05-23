import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import unittest
from unittest.mock import patch


from src.User import User
from src.Cars import Cars
from src.Coche import Coche
from src.Rentalcars import Rentalcars
from src.PaymentData import PaymentData

class TestCars(unittest.TestCase):
    @classmethod
    def setUp(self) -> None:

        self.coche = Coche(1225, 'Citroen', 'Calle Eureka', 5, 25)

        self.cars = Cars()
        self.cars.añadir_coche(self.coche)

    def test_viaje_añadir_vehiculo_precio(self):

        self.assertEqual(self.cars.get_precio_total(), 25)

    def test_vije_eliminar_vehiculo_precio(self):

        coche1 = Coche(1225, 'Citroen', 'Calle Eureka', 5, 50)
        coche2 = Coche(1225, 'Citroen 2', 'Calle Eureka 3 ', 5, 50)

        self.cars.añadir_coche(coche1)
        self.cars.añadir_coche(coche2)

        self.cars.eliminar_coche(coche1)
        self.cars.eliminar_coche(coche2)

        self.assertEqual(25, self.cars.get_precio_total())

if __name__ == '__main__':
    unittest.main(exit=False)