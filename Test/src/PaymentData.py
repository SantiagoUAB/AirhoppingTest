class PaymentData:

    def __init__(self, tipo_tarjeta : str, nombre_titular : str, num_tarjeta : str, codigo_seguridad : int, importe : float):
        self.tipo_tarjeta = tipo_tarjeta
        self.nombre_titular = nombre_titular
        self.num_tarjeta  = num_tarjeta
        self.codigo_seguridad = codigo_seguridad
        self.importe = importe
    
    def get_coste_viaje(self) -> float:
        return self.importe
