# Práctico 5: Listas
# Erika Godoy

# Objetivo:
# Desarrollar la comprensión y la capacidad de manipular listas en Python mediante la aplicación de conceptos fundamentales
# como la indexación, la modificación de elementos, el uso de métodos integrados y el manejo de listas anidadas.

# Resultados de aprendizaje:
# 1. Reconocer y aplicar correctamente la indexación y el slicing para acceder a elementos individuales o subconjuntos dentro de una lista.
# 2. Utilizar los métodos básicos de listas para crear, modificar y gestionar estructuras de datos simples.
# 3. Modificar listas mediante la actualización de valores y el manejo de listas anidadas, comprendiendo cómo acceder a datos en estructuras más complejas.

# Actividades

# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.
multiplos_de_cuatro = list(range(4, 101, 4))
print(multiplos_de_cuatro)

# 2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo.
mis_elementos = ["pantera", "korn", "deftones", "alice in chains", "opeth"]
print(mis_elementos[-2])

# 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla.
lista_vacia = []
lista_vacia.append("black metal")
lista_vacia.append("power metal")
lista_vacia.append("doom metal")
print(lista_vacia)

# 4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente.
# Imprimir la lista resultante por pantalla.
animales = ["perro", "gato", "conejo", "pez"]
animales[1:3] = ["loro", "oso"]
print(animales)

# 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
# Se define una lista llamada números con sus respectivos valores, se encuentra el valor maximo con max(numeros),
# la función max() devuelve el valor máximo de la lista que es este caso es 22 y lo elimina con remove() y devuelve la lista sin este valor.

numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))  # Elimina el máximo de la lista
print(numeros)

# 6) Crear una lista con números del 10 al 30 (incluido), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.
numeros = list(range(10, 31, 5))
print(numeros[:2])

# 7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera.
autos = ["sedan", "polo", "suran", "gol"]
autos[1:2] = ["renault", "toyota"]
print(autos)

# 8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente.
# Imprimir la lista resultante por pantalla.
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print(dobles)

# 9) Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes:
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# a) Agregar "jugo" a la lista del tercer cliente usando append.
compras[2].append("jugo")

# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
compras[1][1] = "tallarines"

# c) Eliminar "pan" de la lista del primer cliente.
compras[0].remove("pan")

# d) Imprimir la lista resultante por pantalla
print(compras)

# 10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
lista_anidada = [15, True], [25.5, 57.9, 30.6], False]
print(lista_anidada)
