from panaderia import Panaderia,Comprador

if __name__ == "__main__":
    p = Panaderia()

    for i in range (10):
        c = Comprador(i,p)
        c.start()