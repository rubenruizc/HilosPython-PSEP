from threading import Semaphore,Thread
import time
import random

class Cine(Thread):

    semaforo = Semaphore(20)

    def __init__(self,nombre):
        Thread.__init__(self)
        self.nombre = nombre

    def run (self):
    # Simulamos el acceso a las cajas de un supermercado
        print("🚗 Persona",self.nombre,"entrando al cine")
        Cine.semaforo.acquire()

         # Cada cliente es atendido en un tiempo distinto
        
        print("🚗 Persona",self.nombre,"está sentando")
        time.sleep(random.randint(1,10))
        
        Cine.semaforo.release()
        print("🚗 Persona",self.nombre,"saliendo del cine",".Espacios disponibles", Cine.semaforo._value)