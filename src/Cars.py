import Coche
class Cars:

    def __init__(self):
        self.list_coches = []
        self.precio_total = 0 

    def get_precio_total(self):
        return self.precio_total
    def añadir_coche(self, Coche):
        self.list_coches.append(Coche)
        self.precio_total = self.precio_total + Coche.precio
    def eliminar_coche(self,Coche):
        condi = False
        if Coche in self.list_coches:
            self.list_coches.remove(Coche)
            condi = True
            self.precio_total =0
            for i in range(len(self.list_coches)):
                self.precio_total = self.precio_total + self.list_coches[i].get_precio()

        return condi
