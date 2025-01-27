from condition import Lista

if __name__ == "__main__":
    # Crear y ejecutar 10 hilos
    hilos = []
    for i in range(10):
        hilo = Lista(nombre=f"Hilo-{i+1}")
        hilos.append(hilo)
        hilo.start()

    # Esperar a que todos los hilos terminen
    for hilo in hilos:
        hilo.join()

    print("Todos los hilos han terminado.")
