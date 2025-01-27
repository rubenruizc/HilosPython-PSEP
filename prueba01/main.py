from ejemplo import MiHilo

if __name__ == "__main__":

    print("Soy el hilo principal")

    for i in range (10):
        t = MiHilo(i)
        t.start()

