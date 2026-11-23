TAMANO_TABLA = 11


def funcion_hash(matricula, tamano=TAMANO_TABLA):
    return matricula % tamano


def crear_tabla_hash(alumnos, tamano=TAMANO_TABLA):
    tabla = [[] for _ in range(tamano)]
    for alumno in alumnos:
        indice = funcion_hash(alumno["matricula"], tamano)
        tabla[indice].append(alumno)
    return tabla


def buscar_hash(tabla, matricula):
    indice = funcion_hash(matricula, len(tabla))
    comparaciones = 0

    for alumno in tabla[indice]:
        comparaciones += 1
        if alumno["matricula"] == matricula:
            return indice, alumno, comparaciones

    return indice, None, comparaciones


def ejecutar_hash():
    alumnos = [
        {"matricula": 24080101, "nombre": "Ana López", "carrera": "Ing. en Sistemas"},
        {"matricula": 24080112, "nombre": "Pedro Ramírez", "carrera": "Ing. Industrial"},
        {"matricula": 24080125, "nombre": "Lucía Herrera", "carrera": "Ing. en Sistemas"},
        {"matricula": 24080134, "nombre": "Jorge Castillo", "carrera": "Ing. Mecánica"},
        {"matricula": 24080148, "nombre": "Fernanda Díaz", "carrera": "Ing. Civil"},
        {"matricula": 24080156, "nombre": "Mateo Vargas", "carrera": "Ing. Eléctrica"},
        {"matricula": 24080167, "nombre": "Camila Torres", "carrera": "Ing. en Sistemas"},
        {"matricula": 24080179, "nombre": "Daniel Morales", "carrera": "Ing. Química"},
    ]

    tabla = crear_tabla_hash(alumnos)

    print("\n--- BÚSQUEDA HASH: CONSULTA DE ALUMNOS POR MATRÍCULA ---")
    print("Matrículas registradas:")
    print(", ".join(str(a["matricula"]) for a in alumnos))

    try:
        matricula = int(input("\nIngresa la matrícula a consultar: "))
    except ValueError:
        print("\nEntrada inválida: la matrícula debe ser numérica.")
        return

    indice, alumno, comparaciones = buscar_hash(tabla, matricula)

    if alumno:
        print(f"\nAlumno encontrado en la cubeta [{indice}] (comparaciones dentro de la cubeta: {comparaciones}):")
        print(f"  Matrícula: {alumno['matricula']} | Nombre: {alumno['nombre']} | Carrera: {alumno['carrera']}")
    else:
        print(f"\nNo se encontró la matrícula {matricula} en la cubeta [{indice}] (comparaciones: {comparaciones}).")


if __name__ == "__main__":
    ejecutar_hash()