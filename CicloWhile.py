print("Ejemplo 1: Contador de repeticiones en el gimnasio")
print("Hola, voy a hacer 5 series de lagartijas")
serie = 1
while serie <= 5:
    print("Completando serie número:", serie)
    serie += 1
print("¡Entrenamiento terminado!")

print("\n" + "-"*40 + "\n")

print("Ejemplo 2: Validación de calificación")
calificacion = float(input("Introduce tu calificación (entre 0 y 10): "))
while calificacion < 0 or calificacion > 10:
    print("Error: La calificación no es válida.")
    calificacion = float(input("Por favor, escribe una calificación entre 0 y 10: "))
print("Calificación guardada:", calificacion)

print("\n" + "-"*40 + "\n")

print("Ejemplo 3: Cuenta regresiva para despegue")
print("Iniciando cuenta regresiva desde 10:")
segundos = 10
while segundos >= 1:
    print(segundos, end="... ")
    segundos -= 1
print("¡Despegue!")

print("\n" + "-"*40 + "\n")

print("Ejemplo 4: Crecimiento de bacterias (duplicación)")
print("Empezamos con 2 bacterias y se duplican cada hora hasta pasar de 500")
bacterias = 2
while bacterias <= 500:
    print("Bacterias actuales:", bacterias)
    bacterias = bacterias * 2
print("El ciclo se detuvo porque superó las 500 bacterias (llegó a", bacterias, ")")

print("\n" + "-"*40 + "\n")

print("Ejemplo 5: Llenado de un garrafón de agua")
print("El garrafón tiene capacidad de 20 litros y le echamos de 4 en 4 litros")
litros = 0
while litros < 20:
    litros += 4
    print("Llevamos", litros, "litros en el garrafón")
print("¡Garrafón lleno con 20 litros!")
