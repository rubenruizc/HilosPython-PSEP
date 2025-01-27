from threading import Thread,Lock
import random
import time

class Panaderia(Thread):
    pan = 7
    
    bloqueo = Lock()

    def __init__(self):
        Thread.__init__(self)

    def compraPan(self):
        Panaderia.bloqueo.acquire()
        if Panaderia.pan > 0:
            Panaderia.pan -= 1
            ok = True
        else:
            print("No queda pan")
            ok = False

        Panaderia.bloqueo.release()

        return ok

        
class Comprador(Thread):
    def __init__(self,nombre,panaderia):
        Thread.__init__(self,name=nombre)
        self.nombre = nombre
        self.tiendaHabitual = panaderia

    def run(self):
        print("Soy el comprador",self.nombre,"comprando pan")
        time.sleep(random.randint(1,4))
        if(self.tiendaHabitual.compraPan()):
            print("El comprador",self.nombre,"compro pan")