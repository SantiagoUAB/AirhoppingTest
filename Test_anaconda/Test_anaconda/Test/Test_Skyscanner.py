


from src.User import User 
from ..src.Flights import Flights
from ..src.Skyscanner import Skyscanner 
from ..src.PaymentData import PaymentData



#from ..src.User import User
#from ..src.Flights import Flights
#from ..src.Skyscanner import Skyscanner



nombres = ["Ana", "Bernardo", "Ramirez"]
apellidos = ["Hurtado Hurtado" ,  "Chaves Chaves" , "Mateos" ]
DNI = ["08075225V", "02604904Q" , "03897631M"]

numTarjeta = 5581238443939998
cvv = 117 # codigo seguridad tarjeta
costeViaje = 0

datosPago = PaymentData("VISA", nombres[0], numTarjeta, cvv, costeViaje)


#user2 = User(nombres[1], apellidos[1], DNI[1] )
#user3 = User(nombres[2], apellidos[2], DNI[2] )

lDestinacion_vuelos = ["Metropolis", "Dinamarcia", "Suecia"]
lCodigo_vuelos = [741, 852 , 963]
num_pasajeros = 3




def Test_Viaje_Numero_pasajeros():
    user1 = User(nombres[0], apellidos[0], DNI[0] , datosPago )

    lVuelos = Flights(lCodigo_vuelos, lDestinacion_vuelos, 3)
    objSkyScanner =  Skyscanner(user1, lVuelos)
    num_pasajerosTest = objSkyScanner.get_num_pasajeros()

    assert num_pasajerosTest  == 3 # numero de paajeros esperados
    print("Test_Viaje_Numero_pasajeros ok")

def Test_Viase_Sin_Destinos():
    user1 = User(nombres[0], apellidos[0], DNI[0] , datosPago )

    lDestinacion_vuelos = []
    lVuelos = Flights(lCodigo_vuelos, lDestinacion_vuelos, 3)
    
    infoReserva =  Skyscanner(user1, lVuelos)

    assert infoReserva.existen_Destinos() == False
    print("Test_Viase_Sin_Destinos ok")

def Test_Viase_Sin_Vuelos():
    user1 = User(nombres[0], apellidos[0], DNI[0] , datosPago )
    lCodigo_vuelos = []

    lVuelos = Flights(lCodigo_vuelos, lDestinacion_vuelos, 3)
    
    infoReserva =  Skyscanner(user1, lVuelos)

    assert infoReserva.existen_Vuelos() == False
    print("Test_Viase_Sin_Vuelos ok")

def Test_Viaje_Precio_Cero():

    datosPago = PaymentData("VISA", nombres[0], numTarjeta, cvv, costeViaje)
    user1 = User(nombres[0], apellidos[0], DNI[0] , datosPago )

    assert user1.datosPago.get_coste_viaje() == 0 # coste de viaje 0
    print("Test_Viaje_Precio_Cero ok")

def Test_destinos_vuelos_esperados():

    lDestinacion_vuelos = ["Metropolis", "Dinamarcia", "Suecia"]
    lCodigo_vuelos = [741, 852 , 963]
    num_pasajeros = 3

    lVuelos = Flights(lCodigo=lCodigo_vuelos, lDestiancion=lDestinacion_vuelos, num_pasajeros=num_pasajeros)
    lVuelos

    assert lVuelos.get_vuelos == lDestinacion_vuelos
    
    
    print("Test_destinos_vuelos_esperados ok ")

def Test_Viaje_Precio_Esperado():
    datosPago = PaymentData("VISA", nombres[0], numTarjeta, cvv, costeViaje)
    user1 = User(nombres[0], apellidos[0], DNI[0] , datosPago )
    lCodigo_vuelos = [741, 852 , 963]

    assert user1.datosPago.get_coste_viaje() == 0 # coste de viaje 0
    print("Test_Viaje_Precio_Cero ok")






Test_Viaje_Numero_pasajeros()
Test_Viase_Sin_Destinos()
Test_Viase_Sin_Vuelos()
Test_Viaje_Precio_Cero()
Test_destinos_vuelos_esperados()

Test_Viaje_Precio_Esperado()

print("ok")