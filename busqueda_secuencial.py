def busqueda_secuencial(pedidos, cliente_buscado):
    comparaciones = 0
    objetivo = cliente_buscado.strip().lower()

    for indice, pedido in enumerate(pedidos):
        comparaciones += 1
        if pedido["cliente"].lower() == objetivo:
            return indice, pedido, comparaciones

    return -1, None, comparaciones


def ejecutar_secuencial():
    pedidos = [
        {"turno": 101, "cliente": "Carlos", "producto": "Americano caliente", "estado": "Entregado"},
        {"turno": 102, "cliente": "Mariana", "producto": "Latte frío", "estado": "Listo"},
        {"turno": 103, "cliente": "Diego", "producto": "Capuchino", "estado": "En preparación"},
        {"turno": 104, "cliente": "Sofía", "producto": "Té matcha", "estado": "En preparación"},
        {"turno": 105, "cliente": "Andrés", "producto": "Frappé moka", "estado": "Pendiente"},
        {"turno": 106, "cliente": "Valeria", "producto": "Chocolate caliente", "estado": "Pendiente"},
        {"turno": 107, "cliente": "Luis", "producto": "Espresso doble", "estado": "Pendiente"},
    ]

    print("\n--- BÚSQUEDA SECUENCIAL: PEDIDOS DE CAFETERÍA ---")
    print("Clientes registrados hoy:")
    print(", ".join(p["cliente"] for p in pedidos))

    nombre = input("\nIngresa el nombre del cliente a buscar: ")
    pos, resultado, comparaciones = busqueda_secuencial(pedidos, nombre)

    if resultado:
        print(f"\nPedido encontrado en la posición {pos} (comparaciones: {comparaciones}):")
        print(f"  Turno: {resultado['turno']} | Cliente: {resultado['cliente']}")
        print(f"  Producto: {resultado['producto']} | Estado: {resultado['estado']}")
    else:
        print(f"\nNo se encontró ningún pedido a nombre de '{nombre}' (comparaciones: {comparaciones}).")


if __name__ == "__main__":
    ejecutar_secuencial()