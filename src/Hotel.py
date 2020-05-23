class Hotel:
    def __init__(self, codigo =0, nombre="", nReservas=0, nHabitaciones=0, nDias_reserva=0,precio =0):
        self.codigo = codigo
        self.nombre = nombre
        self.nReservas = nReservas
        self.nHabitaciones = nHabitaciones
        self.nDias_reserva = nDias_reserva
        self.precio = precio

    def getprecio(self):
        return self.precio

