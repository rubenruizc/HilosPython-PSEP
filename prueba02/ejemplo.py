import random
from threading import Thread,Lock

class BloqueaLista(Thread):
    lista = [False,False,False,False,False]
    bloqueo = Lock()

    def __init__(self,nombre):
        Thread.__init__(self,name=nombre)

    def run(self):
        print("Hilo",self.name,"ejecutandose")

        # Genero posición aleatoria de la lista a tomar
        pos  = random.randint(0,4)
        print("Hilo",self.name,"quiere tomar la posicion",pos)

        # Antes de acceder a la lista, bloqueo la ejecución
        BloqueaLista.bloqueo.acquire()

        if not BloqueaLista.lista[pos]:
            print("Hilo",self.name,"tomando la posicion",pos)
            BloqueaLista.lista[pos] = True
         
        # Desbloqueo la ejecución
        BloqueaLista.bloqueo.release()