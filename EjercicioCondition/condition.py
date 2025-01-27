
import random
from threading import Thread, Condition
import time


class Lista (Thread):
    lista = [False, False, False, False, False]
    cond = Condition()

    def __init__(self,nombre):
        Thread.__init__(self)
        self.nombre = nombre

    def run(self):
        num = random.randint(0,4)

        Lista.cond.acquire()

        while Lista.lista[num] == True:
            print("El hilo",self.nombre,"esta esperando la posicion",num)
            Lista.cond.wait()

        Lista.lista[num] = True

        Lista.cond.release()

        print("El hilo",self.nombre,"esta usando el objeto",num)

        time.sleep(random.randint(1,10))

        print("El hilo",self.nombre,"libera el objeto",num)

        Lista.cond.acquire()

        Lista.lista[num] = False

        Lista.cond.notifyAll()

        Lista.cond.release()