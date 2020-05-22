class PaymentData:

    tipo_VISA = 'VISA'
    tipo_Mastercard = 'Mastercard'
    def __init__(self, tipo_tarjeta : str, nombre_titular : str, num_tarjeta : str, codigo_seguridad : int, importe : float):
        self.tipo_tarjeta = tipo_tarjeta
        self.nombre_titular = nombre_titular
        self.num_tarjeta  = num_tarjeta
        self.codigo_seguridad = codigo_seguridad
        self.importe = importe

    def get_tipo_pago(self):
        return self.tipo_tarjeta

    def get_importe(self) -> float:
        return self.importe
    def eliminar_importe_destino(self, importe) -> None:
        self.importe = self.importe - importe
    def add_coste_destino(self, importe : float) -> None:

        self.importe = self.importe + importe