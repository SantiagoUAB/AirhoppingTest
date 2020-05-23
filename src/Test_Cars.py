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
        self.nombres = ['Ana', 'Bernardo', 'Ramirez']
        self.apellidos = ['Hurtado Hurtado', 'Chaves Chaves', 'Mateos']
        self.DNI = ['08075225V', '02604904Q', '03897631M']
        self.coches = Coche()
        self.coches.crear_coche(1234,'Mercedes','Avenida hola', 2,50)
        self.car = Cars()
        self.car.añadir_coche(self.coches)
    def test_viaje_añadir_vehiculo_precio(self):
        self.coches.crear_coche(1225,'Citroen','Calle Eureka', 5,25)
        self.car.añadir_coche(self.coches)
        self.assertEqual(self.car.get_precio_total(),75)

    def Test_vije_eliminar_vehiculo_precio(self):
        self.coches.crear_coche(1225,'Citroen','Calle Eureka',5,25)
        self.car.añadir_coche(self.coches)
        self.assertEqual(2,len(self.car.list_coches))
        self.car.eliminar_coche(self.coches)
        self.assertEqual(50,self.car.get_precio_total())
if __name__ == '__main__':
    unittest.main(exit=False)