print("Ejemplo 1: Recorrer una lista simple de números")
for i in [1, 2, 3, 4, 5]:
    print("Número actual en el ciclo:", i)
print("Fin del ejemplo 1\n")

print("Ejemplo 2: Recorrer una lista de elementos (videojuegos)")
for juego in ["Minecraft", "Roblox", "Fortnite", "FIFA"]:
    print("Me gusta jugar:", juego)
print("Fin del ejemplo 2\n")

print("Ejemplo 3: Recorrer los caracteres de una palabra (porras)")
for letra in "EMIR":
    print(f"Dame una {letra}!")
print("¡EMIR!")
print("Fin del ejemplo 3\n")

print("Ejemplo 4: Usando range() para contar con un límite")
for i in range(1, 6):
    print("Contando con range:", i)
print("Fin del ejemplo 4\n")

print("Ejemplo 5: Simular la tirada de dados 3 veces y sumar el total")
import random
print("Comienzo del ejemplo 5")
total = 0
for i in range(3):
    dado = random.randrange(1, 7)
    print(f"Tirada {i + 1}: salió un {dado}")
    total += dado
print(f"¡Suma total acumulada en los 3 dados: {total} puntos!")
print("Fin del ejemplo 5")