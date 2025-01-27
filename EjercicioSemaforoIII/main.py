from aparcamiento import Aparcamiento

if __name__ == "__main__":
    for i in range(1,10):
        hilo = Aparcamiento(i)
        hilo.start()