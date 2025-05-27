# Gestión de Stock - Programación I

# Listas paralelas
nombres = []
cantidades = []

# Función para mostrar el menú
def mostrar_menu():
    print("\n🛒 MENÚ DE OPCIONES")
    print("1. Agregar producto")
    print("2. Ver productos agotados")
    print("3. Actualizar stock")
    print("4. Ver todos los productos")
    print("5. Salir")

# Bucle principal
salir = False
while not salir:
    mostrar_menu()
    opcion = input("Selecciona una opción (1-5): ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del producto: ")
        while True:
            try:
                cantidad = int(input("Ingrese la cantidad en stock: "))
                break
            except ValueError:
                print("⚠️ Error: ingrese un número entero para la cantidad.")
        nombres.append(nombre)
        cantidades.append(cantidad)
        print("✅ Producto agregado con éxito.")

    elif opcion == "2":
        print("\n📦 Productos agotados:")
        agotados = False
        for i in range(len(nombres)):
            if cantidades[i] == 0:
                print(f"- {nombres[i]}")
                agotados = True
        if not agotados:
            print("No hay productos agotados.")

    elif opcion == "3":
        producto = input("Ingrese el nombre del producto a actualizar: ")
        if producto in nombres:
            index = nombres.index(producto)
            while True:
                try:
                    nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
                    break
                except ValueError:
                    print("⚠️ Error: ingrese un número entero.")
            cantidades[index] = nueva_cantidad
            print("🔄 Stock actualizado correctamente.")
        else:
            print("❌ Producto no encontrado.")

    elif opcion == "4":
        print("\n📋 Listado de productos:")
        if len(nombres) == 0:
            print("No hay productos cargados.")
        else:
            for i in range(len(nombres)):
                print(f"- {nombres[i]}: {cantidades[i]} unidades")

    elif opcion == "5":
        print("👋 Gracias por usar el sistema de gestión de stock.")
        salir = True

    else:
        print("⚠️ Opción inválida. Intente nuevamente.")
