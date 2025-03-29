# ========================================
# Uso de While Loops en Python
# ========================================

"""
## 📌 Descripción
El bucle `while` en Python ejecuta un bloque de código repetidamente mientras una condición sea verdadera.

📌 **Características principales:**
- Se usa cuando no sabemos de antemano cuántas veces se repetirá el bucle.
- Es importante modificar la condición dentro del bucle para evitar bucles infinitos.
- Se puede combinar con `break`, `continue` y `else` para controlar el flujo de ejecución.
"""

# ========================================
# Ejemplo básico de while
# ========================================

counter = 5
while counter > 0:
    print(f"Contador: {counter}")
    counter -= 1  # Disminuye el contador en cada iteración

# ========================================
# Uso de else en while
# ========================================

"""
El `else` en un bucle `while` se ejecuta solo si el bucle termina sin interrupciones (`break`).
"""

contador = 0
while contador < 3:
    print(f"Intento {contador + 1}")
    contador += 1
else:
    print("El bucle terminó sin interrupciones.")

# ========================================
# Uso de while True con break
# ========================================

"""
Un `while True` crea un bucle infinito que solo termina cuando se usa `break`.
Es útil cuando no sabemos cuántas iteraciones se necesitarán.
"""

while True:
    entrada = input("Escribe 'salir' para finalizar: ")
    if entrada.lower() == "salir":
        print("Saliendo del bucle...")
        break

# ========================================
# Uso de input() en while
# ========================================

"""
Podemos usar `while` para solicitar entrada del usuario hasta que se ingrese un valor específico.
"""
user_input = ""
while user_input.lower() != "salir":
    user_input = input("Escribe 'salir' para terminar: ")

# ========================================
# Validación de entrada con while
# ========================================

"""
Podemos usar `while` para asegurarnos de que el usuario ingrese datos correctos.
"""

edad = input("Ingresa tu edad (número entre 1 y 100): ")

while not edad.isdigit() or not (1 <= int(edad) <= 100):
    print("Entrada no válida. Debes ingresar un número entre 1 y 100.")
    edad = input("Ingresa tu edad nuevamente: ")

print(f"Edad válida ingresada: {edad}")

# ========================================
# Uso de `break` y `continue`
# ========================================

"""
- `break`: Termina el bucle inmediatamente.
- `continue`: Salta el resto del código en la iteración actual y pasa a la siguiente.
"""

# Ejemplo de 'break'
x = 0
while x < 10:
    if x == 5:
        break  # Detiene el bucle cuando x es 5
    print(x)
    x += 1
# Salida: 0, 1, 2, 3, 4

# Ejemplo de 'continue'
y = 0
while y < 5:
    y += 1
    if y == 3:
        continue  # Omite la impresión del número 3
    print(y)
# Salida: 1, 2, 4, 5

# ========================================
# Resumen
# ========================================

"""
## 📌 Resumen
- `while` ejecuta un bloque de código mientras la condición sea verdadera.
- Se debe modificar la condición dentro del bucle para evitar bucles infinitos.
- `else` en `while` se ejecuta solo si no se interrumpe con `break`.
- `while True` se usa para bucles infinitos hasta que ocurra una condición de salida.
- `break` permite salir del bucle antes de que termine.
- `continue` omite el resto del código en una iteración y pasa a la siguiente.
"""

# ========================================
# Ejercicios de Práctica
# ========================================

"""
## 🧠 Ejercicios de práctica para While Loops

Practica lo aprendido sobre bucles `while`, `break`, `continue`, `else`, validación de entrada y ciclos infinitos controlados.

Escribe tu solución en los espacios indicados.
"""

# --------------------------------------------------
# 1️⃣ Imprime los números del 1 al 5 usando while
# --------------------------------------------------

contador = 1

while contador <= 5:
    print(f"Contador: {contador}")
    contador += 1

# --------------------------------------------------
# 2️⃣ Usa while para contar hacia atrás desde 10 hasta 1
# --------------------------------------------------

counter = 10

while counter >= 1:
    print(f"Contador regresivo: {counter}")
    counter -= 1

# --------------------------------------------------
# 3️⃣ Pide al usuario una contraseña hasta que escriba "secreto123"
# --------------------------------------------------

user = input("Ingresa una clave: ")
password = "secreto123"

while user.lower() != password:
    user = input("Escribe de nuevo la clave: ")
print("Clave correcta")

# --------------------------------------------------
# 4️⃣ Usa while con `continue` para omitir el número 3 al contar hasta 5
# --------------------------------------------------

y = 0
while y < 5:
    y += 1
    if y == 3:
        continue
    print(y)

# --------------------------------------------------
# 5️⃣ Usa while con `break` para detener al llegar a 7
# --------------------------------------------------

i = 0
while i < 10:
    i += 1
    if i == 7:
        break
    print(i)

# --------------------------------------------------
# 6️⃣ Crea un bucle while que se ejecute solo si el usuario escribe "sí"
# --------------------------------------------------

user_input = ""
while user_input.lower() != "si":
    user_input = input("Escribe 'si' para salir: ")


# --------------------------------------------------
# 7️⃣ Validación: Pide un número entre 1 y 10 hasta que el usuario lo ingrese correctamente
# --------------------------------------------------

num = input("Ingresa un numero entre 1 y 10: ")

while not num.isdigit() or not (1 <= int(num) <= 10):
    print("Entrada no valida. Debes ingresar un numero entre 1 y 10")
    num = input("Ingresa un numero nuevamente: ")
print(f"Numero valido ingresado {num}")

# ========================================
# Fin del Documento
# ========================================