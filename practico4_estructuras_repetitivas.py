
# Práctico 4 - Estructuras Repetitivas

# 1) Números del 0 al 100
for i in range(101):
    print(i)

# 2) Contar dígitos
numero = int(input("Ingrese un número entero: "))
print("Cantidad de dígitos:", len(str(abs(numero))))

# 3) Suma entre dos números (excluyendo extremos)
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
inicio = min(a, b) + 1
fin = max(a, b)
suma = 0
for i in range(inicio, fin):
    suma += i
print("La suma es:", suma)

# 4) Suma hasta ingresar 0
suma = 0
while True:
    numero = int(input("Ingrese un número (0 para salir): "))
    if numero == 0:
        break
    suma += numero
print("Suma total:", suma)

# 5) Juego de adivinanza
import random
numero_secreto = random.randint(0, 9)
intentos = 0
adivinado = False
while not adivinado:
    intento = int(input("Adivina el número (0-9): "))
    intentos += 1
    if intento == numero_secreto:
        adivinado = True
print("¡Correcto! Lo adivinaste en", intentos, "intentos.")

# 6) Números pares del 100 al 0
for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)

# 7) Sumar hasta un número positivo
n = int(input("Ingrese un número positivo: "))
suma = 0
for i in range(n + 1):
    suma += i
print("La suma es:", suma)

# 8) Contar pares, impares, positivos y negativos
pares = impares = positivos = negativos = 0
cantidad = 100
for _ in range(cantidad):
    num = int(input("Ingrese un número: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
print("Pares:", pares)
print("Impares:", impares)
print("Positivos:", positivos)
print("Negativos:", negativos)

# 9) Calcular la media de 100 números
suma = 0
cantidad = 100
for _ in range(cantidad):
    num = int(input("Ingrese un número: "))
    suma += num
media = suma / cantidad
print("La media es:", media)

# 10) Invertir número
numero = input("Ingrese un número: ")
invertido = numero[::-1]
print("Número invertido:", invertido)
