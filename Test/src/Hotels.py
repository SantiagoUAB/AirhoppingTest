import os
import os.path

class Hotels:

    def __init__(self, codigo, nombre, nReservas, nHabitaciones, nDias_reserva):
        self.codigo = codigo
        self.nombre = nombre
        self.nReservas = nReservas
        self.nHabitaciones = nHabitaciones
        self.nDias_reserva = nDias_reserva
        pass

    def rm(self, filename):
        """Dummy function to remove a file.

        Args:
            filename (str): path to the file.
        """    
        if os.path.isfile(filename):
            os.remove(filename)
    
    @staticmethod
    def get_always_true():
        """Dummy function to return always true

        Returns:
            [bool]: Return true.
        """        
        return True