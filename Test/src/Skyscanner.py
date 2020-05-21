from src.User import User
from src.Flights import Flights



class Skyscanner():
    
    
    def __init__(self, user: User, lVuelos: Flights):
        self.user = user
        self.lVuelos = lVuelos

        pass
    def get_num_pasajeros(self) -> int:
        return self.lVuelos.get_num_pasajeros()
    
    def existen_Destinos(self) -> bool:
        return self.lVuelos.existen_Destinos()
    
    def existen_Vuelos(self) -> bool:
        return self.lVuelos.existen_Vuelos()
    
    def confirm_reserve(self, user: User, flights: Flights) -> bool:
        return True
    
    def get_destinos(self):
        return self.lVuelos.get_destinos()

    def get_vuelos(self):
        return self.lVuelos.get_vuelos()