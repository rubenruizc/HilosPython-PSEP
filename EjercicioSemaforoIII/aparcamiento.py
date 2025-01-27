from threading import Semaphore,Thread
import random
import time

class Aparcamiento(Thread):

    semaforo = Semaphore(5)

    def __init__(self,nombre):
        Thread.__init__(self)
        self.nombre = nombre

    def run(self):
        # Simulamos el acceso a las cajas de un supermercado
        print("🚗 Vehículo",self.nombre,"entrando al garaje")
        Aparcamiento.semaforo.acquire()

         # Cada cliente es atendido en un tiempo distinto
        
        print("🚗 Vehículo",self.nombre,"está aparcando")
        time.sleep(random.randint(1,10))
        
        Aparcamiento.semaforo.release()
        print("🚗 Vehículo",self.nombre,"saliendo del garaje",".Espacios disponibles", Aparcamiento.semaforo._value)

       
        