class Flights:

    def __init__(self, lCodigo, lDestiancion, num_pasajeros : int):
        self.lCodio = lCodigo
        self.lDestiancion = lDestiancion
        self.num_pasajeros =  num_pasajeros
    
    def get_num_pasajeros(self)-> int:
        return self.num_pasajeros

    def add_vuelo (self):

        return True
        pass
    
    def existen_Destinos(self) -> bool:
        if len(self.lDestiancion) <= 0:
            return False # no existen destinos
        else:
            return False
    def existen_Vuelos(self) -> bool:
        if len(self.lCodio) <= 0:
            return False # no existen vuelos
        else:
            return True
    
    def get_destinos(self):
        return self.lDestiancion
    
    def get_vuelos(self):
        return self.lCodio
