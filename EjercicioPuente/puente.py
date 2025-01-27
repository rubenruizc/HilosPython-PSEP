import time
import random
from threading import *

class PasoPuente (Thread):

    semaforoNorte = Semaphore(1)

    semaforoSur = Semaphore(1)

    def __init__(self,nombre,direccion):
        Thread.__init__(self)
        self.nombre = nombre
        self.direccion = direccion

    def run (self):

        if self.direccion == 0:
            PasoPuente.semaforoNorte.acquire()
            PasoPuente.semaforoSur.acquire()

            print (f"{self.nombre} cruzando el puente en dirección Norte")
            time.sleep(random.randint(2,3))
            print(f"{self.nombre} ha cruzado el puente en direccion Norte")

            PasoPuente.semaforoNorte.release()
            PasoPuente.semaforoSur.release()

        else:
            PasoPuente.semaforoSur.acquire()
            PasoPuente.semaforoNorte.acquire()

            print (f"{self.nombre} cruzando el puente en direccion Sur")
            time.sleep(random.randint(2,3))
            print(f"{self.nombre} ha cruzado el puente en direccion Sur")

            PasoPuente.semaforoSur.release()
            PasoPuente.semaforoNorte.release()