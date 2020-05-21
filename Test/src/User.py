from src.PaymentData import PaymentData
class User:
    
    def __init__(self, nombre, apellidos, DNI, datosPago: PaymentData):
        """ Declaracon de Usuario, este contiene los datos necesarios para gestionar la reserva."""
        self.nombre = nombre
        self.apellidos = apellidos
        self.DNI = DNI
        self.datosPago = datosPago
    
    def get_coste_viaje(self) -> float:
        return  self.datosPago.get_coste_viaje()
    
    


  