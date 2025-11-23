def agregar_canciones(nombres, artistas, duraciones, popularidades):
    n = int(input("¿Cuántas canciones desea agregar? "))
    for _ in range(n):
        nombre = input("Nombre de la canción: ")
        artista = input("Artista: ")
        duracion = float(input("Duración en minutos: "))
        popularidad = int(input("Popularidad (1-100): "))
        nombres.append(nombre)
        artistas.append(artista)
        duraciones.append(duracion)
        popularidades.append(popularidad)
    print(f"{n} canciones agregadas.\n")

def ver_reportes(nombres, duraciones, popularidades):
    if not nombres:
        print("No hay canciones en la playlist.\n")
        return
    total_canciones = len(nombres)
    duracion_total = sum(duraciones)
    indice_mas_popular = popularidades.index(max(popularidades))
    indice_menos_popular = popularidades.index(min(popularidades))
    promedio_popularidad = sum(popularidades) / total_canciones
    print(f"Número total de canciones: {total_canciones}")
    print(f"Duración total de la playlist: {duracion_total:.2f} minutos")
    print(f"Canción más popular: {nombres[indice_mas_popular]} (Popularidad: {popularidades[indice_mas_popular]})")
    print(f"Canción menos popular: {nombres[indice_menos_popular]} (Popularidad: {popularidades[indice_menos_popular]})")
    print(f"Promedio de popularidad: {promedio_popularidad:.2f}\n")

def buscar_canciones(nombres, artistas, popularidades):
    if not nombres:
        print("No hay canciones en la playlist para buscar.\n")
        return
    print("Buscar canciones por:")
    print("1. Artista")
    print("2. Rango de popularidad")
    opcion = input("Seleccione opción (1-2): ")
    if opcion == "1":
        artista_buscar = input("Nombre del artista a buscar: ").lower()
        encontrados = [nombres[i] for i, art in enumerate(artistas) if art.lower() == artista_buscar]
        if encontrados:
            print("Canciones encontradas:")
            for c in encontrados:
                print(f"- {c}")
        else:
            print("No se encontraron canciones de ese artista.")
    elif opcion == "2":
        min_pop = int(input("Popularidad mínima: "))
        max_pop = int(input("Popularidad máxima: "))
        encontrados = [nombres[i] for i, pop in enumerate(popularidades) if min_pop <= pop <= max_pop]
        if encontrados:
            print("Canciones encontradas:")
            for c in encontrados:
                print(f"- {c}")
        else:
            print("No se encontraron canciones en ese rango de popularidad.")
    else:
        print("Opción inválida.")
    print()

def playlist_recomendada(nombres, artistas, duraciones, popularidades):
    if not nombres:
        print("No hay canciones en la playlist.\n")
        return
    promedio = sum(popularidades) / len(popularidades)
    recomendadas = [(nombres[i], artistas[i], duraciones[i], popularidades[i])
                    for i in range(len(nombres)) if popularidades[i] > promedio]
    if not recomendadas:
        print("No hay canciones con popularidad superior al promedio.\n")
        return
    print(f"Playlist recomendada (popularidad > {promedio:.2f}):")
    for nombre, artista, duracion, pop in recomendadas:
        print(f"- {nombre} de {artista} ({duracion} min, Popularidad: {pop})")
    print()

def menu():
    nombres = []
    artistas = []
    duraciones = []
    popularidades = []
    while True:
        print("Menu:")
        print("1. Agregar canciones")
        print("2. Ver reportes")
        print("3. Buscar canciones")
        print("4. Playlist recomendada")
        print("5. Salir")
        opcion = input("Seleccione una opción (1-5): ")
        if opcion == "1":
            agregar_canciones(nombres, artistas, duraciones, popularidades)
        elif opcion == "2":
            ver_reportes(nombres, duraciones, popularidades)
        elif opcion == "3":
            buscar_canciones(nombres, artistas, popularidades)
        elif opcion == "4":
            playlist_recomendada(nombres, artistas, duraciones, popularidades)
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.\n")

if __name__ == "__main__":
    menu()