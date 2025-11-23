def crear_sala(filas, columnas):
    return [["L" for _ in range(columnas)] for _ in range(filas)]

def mostrar_sala(sala):
    print("\nEstado de la sala:")
    for fila in sala:
        print(" ".join(fila))
    print()

def reservar_asiento(sala):
    fila = int(input("Fila a reservar: ")) - 1
    columna = int(input("Columna a reservar: ")) - 1
    if fila < 0 or fila >= len(sala) or columna < 0 or columna >= len(sala[0]):
        print("Asiento inválido.\n")
        return
    if sala[fila][columna] == "X":
        print("El asiento ya está ocupado.\n")
    else:
        sala[fila][columna] = "X"
        print("Asiento reservado.\n")

def liberar_asiento(sala):
    fila = int(input("Fila a liberar: ")) - 1
    columna = int(input("Columna a liberar: ")) - 1
    if fila < 0 or fila >= len(sala) or columna < 0 or columna >= len(sala[0]):
        print("Asiento inválido.\n")
        return
    if sala[fila][columna] == "L":
        print("El asiento ya está libre.\n")
    else:
        sala[fila][columna] = "L"
        print("Asiento liberado.\n")

def contar_asientos(sala):
    libres = sum(fila.count("L") for fila in sala)
    ocupados = sum(fila.count("X") for fila in sala)
    print(f"Asientos libres: {libres}")
    print(f"Asientos ocupados: {ocupados}\n")

def menu():
    filas = int(input("Número de filas: "))
    columnas = int(input("Número de columnas: "))
    sala = crear_sala(filas, columnas)
    
    while True:
        print("Menú:")
        print("1. Mostrar sala")
        print("2. Reservar asiento")
        print("3. Liberar asiento")
        print("4. Contar asientos")
        print("5. Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            mostrar_sala(sala)
        elif opcion == "2":
            reservar_asiento(sala)
        elif opcion == "3":
            liberar_asiento(sala)
        elif opcion == "4":
            contar_asientos(sala)
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.\n")

if __name__ == "__main__":
    menu()
