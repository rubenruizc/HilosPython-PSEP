from supermercado import Supermercado

if __name__ == "__main__":
    for i in range(4):
        supermercado = Supermercado(i)
        supermercado.start()