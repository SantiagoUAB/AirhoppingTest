import os
import os.path

from src.Hotel import Hotel

class Hotels:

    def __init__(self):
        self.listahoteles = []
        self.precio_total = 0

    def getpreciototal(self):
        return self.precio_total

    def añadir_hotel(self, Hotel):

        self.listahoteles.append(Hotel)
        self.precio_total = self.precio_total + Hotel.getprecio()

    def eliminar_hotel(self, Hotel):

        self.listahoteles.remove(Hotel)
        self.precio_total = 0
        for i in range(len(self.listahoteles)):
            self.precio_total = self.precio_total + self.listahoteles[i].getprecio()
