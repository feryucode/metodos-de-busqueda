def busqueda_binaria(catalogo, codigo_buscado):
    inicio = 0
    fin = len(catalogo) - 1
    comparaciones = 0

    while inicio <= fin:
        medio = (inicio + fin) // 2
        comparaciones += 1
        codigo_actual = catalogo[medio]["codigo"]

        if codigo_actual == codigo_buscado:
            return medio, catalogo[medio], comparaciones
        elif codigo_buscado < codigo_actual:
            fin = medio - 1
        else:
            inicio = medio + 1

    return -1, None, comparaciones


def ejecutar_binaria():
    catalogo = [
        {"codigo": 1005, "nombre": "Mouse inalámbrico", "precio": 320},
        {"codigo": 1012, "nombre": "Teclado mecánico", "precio": 950},
        {"codigo": 1018, "nombre": "Memoria USB 64GB", "precio": 180},
        {"codigo": 1024, "nombre": "Audífonos Bluetooth", "precio": 640},
        {"codigo": 1031, "nombre": "SSD NVMe 1TB", "precio": 1450},
        {"codigo": 1040, "nombre": "Monitor 24 pulgadas", "precio": 2890},
        {"codigo": 1047, "nombre": "Hub USB-C 6 en 1", "precio": 410},
        {"codigo": 1055, "nombre": "Webcam Full HD", "precio": 580},
        {"codigo": 1063, "nombre": "Fuente de poder 650W", "precio": 1320},
        {"codigo": 1079, "nombre": "Gabinete ATX", "precio": 1150},
    ]

    print("\n--- BÚSQUEDA BINARIA: CATÁLOGO DE ELECTRÓNICA ---")
    print("Códigos disponibles (ordenados):")
    print(", ".join(str(p["codigo"]) for p in catalogo))

    try:
        codigo = int(input("\nIngresa el código del producto a buscar: "))
    except ValueError:
        print("\nEntrada inválida: debes escribir un número de código.")
        return

    pos, producto, comparaciones = busqueda_binaria(catalogo, codigo)

    if producto:
        print(f"\nProducto encontrado en el índice {pos} (comparaciones: {comparaciones}):")
        print(f"  Código: {producto['codigo']} | Nombre: {producto['nombre']} | Precio: ${producto['precio']}")
    else:
        print(f"\nEl código {codigo} no existe en el catálogo (comparaciones: {comparaciones}).")


if __name__ == "__main__":
    ejecutar_binaria()