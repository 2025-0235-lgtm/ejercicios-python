print ("Hola Chely 😄, Python está funcionando perfectamente en tu Linux!")
# ======================================
#  EJERCICIOS PYTHON - CHELY 
# ======================================

# ===== EJERCICIO 1 =====
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

print("\nEJERCICIO 1:")
print("Las asignaturas del curso son:")
for materia in asignaturas:
    print(materia)


# ===== EJERCICIO 2 =====
print("\nEJERCICIO 2:")
for materia in asignaturas:
    print("Yo estudio", materia)


# ===== EJERCICIO 3 =====
print("\nEJERCICIO 3:")
notas = []
for materia in asignaturas:
    nota = input(f"¿Qué nota has sacado en {materia}? ")
    notas.append(nota)

print("\nResultados:")
for i in range(len(asignaturas)):
    print(f"En {asignaturas[i]} has sacado {notas[i]}")


# ===== EJERCICIO 4 =====
print("\nEJERCICIO 4:")
numeros = []
for i in range(6):
    num = int(input(f"Introduce el número ganador {i+1}: "))
    numeros.append(num)
numeros.sort(reverse=True)
print("Números ganadores ordenados de mayor a menor:", numeros)


# ===== EJERCICIO 5 =====
print("\nEJERCICIO 5:")
numeros = list(range(1, 11))
numeros.reverse()
print("Números del 10 al 1 separados por comas:")
print(", ".join(map(str, numeros)))


# ===== EJERCICIO 6 =====
print("\nEJERCICIO 6:")
aprobadas = []
for materia in asignaturas:
    nota = float(input(f"¿Qué nota sacaste en {materia}? "))
    if nota >= 5:
        aprobadas.append(materia)
print("\nHas aprobado las siguientes asignaturas:")
for materia in aprobadas:
    print(materia)


# ===== EJERCICIO 7 =====
print("\nEJERCICIO 7:")
import string
abecedario = list(string.ascii_lowercase)
resultado = [letra for i, letra in enumerate(abecedario) if (i + 1) % 3 == 0]
print("Letras en posiciones múltiplos de 3:")
print(resultado)


# ===== EJERCICIO 8 =====
print("\nEJERCICIO 8:")
palabra = input("Introduce una palabra: ")
if palabra == palabra[::-1]:
    print("Es un palíndromo ")
else:
    print("No es un palíndromo")


# ===== EJERCICIO 9 =====
print("\nEJERCICIO 9:")
palabra = input("Introduce una palabra: ").lower()
vocales = "aeiou"
for vocal in vocales:
    print(f"{vocal}: {palabra.count(vocal)}")


# ===== EJERCICIO 10 =====
print("\nEJERCICIO 10:")
precios = [50, 75, 46, 22, 80, 65, 8]
print("El precio menor es:", min(precios))
print("El precio mayor es:", max(precios))


# ===== EJERCICIO 11 =====
print("\nEJERCICIO 11:")
v1 = [1, 2, 3]
v2 = [-1, 0, 2]
producto_escalar = sum(v1[i] * v2[i] for i in range(len(v1)))
print("El producto escalar es:", producto_escalar)


# ===== EJERCICIO 12 =====
print("\nEJERCICIO 12:")
import math
muestra = input("Introduce números separados por comas: ")
numeros = [float(x) for x in muestra.split(",")]
media = sum(numeros) / len(numeros)
desviacion = math.sqrt(sum((x - media) ** 2 for x in numeros) / len(numeros))
print("Media:", media)
print("Desviación típica:", desviacion)
