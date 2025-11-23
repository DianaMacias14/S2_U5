def main():
    estudiantes = int(input("¿Cuántos estudiantes hay? "))
    materias = int(input("¿Cuántas materias hay? "))

    calificaciones = []
    print("\nIngrese las calificaciones de cada estudiante para cada materia (0-100):")

    for i in range(estudiantes):
        fila = []
        for j in range(materias):
            nota = float(input(f"Estudiante {i+1}, materia {j+1}: "))
            while nota < 0 or nota > 100:
                print("Calificación inválida. Debe estar entre 0 y 100.")
                nota = float(input(f"Estudiante {i+1}, materia {j+1}: "))
            fila.append(nota)
        calificaciones.append(fila)

    # Imprimir la matriz de calificaciones de forma tabulada
    print("\nMatriz de calificaciones:")
    for i, fila in enumerate(calificaciones):
        print(f"Estudiante {i+1}:\t" + "\t".join(f"{nota:.2f}" for nota in fila))

    # Promedio por estudiante
    print("\nPromedio por estudiante:")
    for i in range(estudiantes):
        promedio = sum(calificaciones[i]) / materias
        print(f"Estudiante {i+1}: {promedio:.2f}")

    # Promedio por materia
    print("\nPromedio por materia:")
    for j in range(materias):
        suma_materia = sum(calificaciones[i][j] for i in range(estudiantes))
        promedio = suma_materia / estudiantes
        print(f"Materia {j+1}: {promedio:.2f}")

    # Calificación más alta y más baja
    todas_notas = [nota for fila in calificaciones for nota in fila]
    max_nota = max(todas_notas)
    min_nota = min(todas_notas)
    print(f"\nCalificación más alta: {max_nota:.2f}")
    print(f"Calificación más baja: {min_nota:.2f}")

if __name__ == "__main__":
    main()
