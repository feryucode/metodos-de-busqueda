from busqueda_secuencial import ejecutar_secuencial
from busqueda_binaria import ejecutar_binaria
from busqueda_hash import ejecutar_hash


def mostrar_menu():
    while True:
        print("\n=========================================")
        print("       MENÚ DE MÉTODOS DE BÚSQUEDA       ")
        print("=========================================")
        print("1. Búsqueda Secuencial (Pedidos de cafetería)")
        print("2. Búsqueda Binaria (Catálogo de electrónica)")
        print("3. Búsqueda Hash (Consulta de alumnos)")
        print("4. Salir")
        print("=========================================")

        opcion = input("Elige una opción (1-4): ").strip()

        if opcion == "1":
            ejecutar_secuencial()
        elif opcion == "2":
            ejecutar_binaria()
        elif opcion == "3":
            ejecutar_hash()
        elif opcion == "4":
            print("\nSaliendo del programa...")
            break
        else:
            print("\nOpción no válida. Intenta con un número del 1 al 4.")


if __name__ == "__main__":
    mostrar_menu()