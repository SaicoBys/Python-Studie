# ========================================
# Flujo de Control en Python
# ========================================

"""
## 📌 Descripción
El flujo de control en Python permite ejecutar diferentes bloques de código según condiciones específicas.
Se divide en las siguientes estructuras:

1. **Condicionales (`if`, `elif`, `else`)**: Ejecutan código dependiendo de una condición.
2. **Operadores Lógicos (`and`, `or`, `not`)**: Permiten combinar condiciones en expresiones condicionales.
3. **Estructuras de decisión `match-case`**: Alternativa a `if-elif-else` (Python 3.10+).
4. **Control de flujo en bucles (`break`, `continue`, `else`)**: Manejan la ejecución dentro de los bucles.
"""

# ========================================
# 1. Condicionales (if, elif, else)
# ========================================

"""
Las sentencias `if`, `elif` y `else` permiten ejecutar código basado en condiciones.

📌 **Sintaxis básica:**
if condición:
    # Código a ejecutar si la condición es verdadera
elif otra_condición:
    # Código si la primera condición es falsa y esta es verdadera
else:
    # Código si ninguna condición anterior se cumple
"""

# Ejemplo interactivo con entrada del usuario
edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Eres mayor de edad.")
elif edad >= 13:
    print("Eres un adolescente.")
else:
    print("Eres un niño.")

# ========================================
# 2. Operadores Lógicos en Condiciones
# ========================================

"""
Los operadores lógicos (`and`, `or`, `not`) permiten evaluar múltiples condiciones:
- `and`: Devuelve `True` si ambas condiciones son verdaderas.
- `or`: Devuelve `True` si al menos una condición es verdadera.
- `not`: Invierte el resultado de una condición.
"""

# Ejemplo con operadores lógicos
ingresos = 5000
credito_bueno = True

if ingresos > 3000 and credito_bueno:
    print("Aprobado para el préstamo.")
else:
    print("No cumples con los requisitos.")

# ========================================
# 3. Uso de match-case (Python 3.10+)
# ========================================

"""
`match-case` es una alternativa más clara al `if-elif-else` cuando se tienen múltiples casos.

📌 **Sintaxis:**
match variable:
    case valor1:
        # Código a ejecutar
    case valor2:
        # Otro bloque de código
    case _:
        # Caso por defecto (similar a else)
"""

# Ejemplo con match-case
opcion = int(input("Seleccione una opción (1, 2 o 3): "))

match opcion:
    case 1:
        print("Seleccionaste la opción 1.")
    case 2:
        print("Seleccionaste la opción 2.")
    case _:
        print("Opción no válida.")  # `case _:` actúa como `else` en `if-elif-else`.

# ========================================
# 4. Control de Flujo en Bucles
# ========================================

"""
Se pueden utilizar `break`, `continue` y `else` dentro de bucles para modificar el flujo de ejecución:
- `break`: Detiene completamente el bucle.
- `continue`: Salta a la siguiente iteración sin ejecutar el resto del código en la actual.
- `else`: Se ejecuta solo si el bucle termina sin interrupciones por `break`.
"""

# Ejemplo con break y continue
for numero in range(1, 6):
    if numero == 3:
        continue  # Salta el número 3
    print(numero)

# Ejemplo con else en for-loop
for i in range(5):
    print(i)
else:
    print("Bucle terminado sin interrupciones.")

# Ejemplo con else en while-loop
contador = 0
while contador < 3:
    print(f"Intento {contador + 1}")
    contador += 1
else:
    print("El bucle terminó sin interrupciones.")

# ========================================
# Resumen
# ========================================

"""
## 📌 Resumen
- `if-elif-else` se usa para decisiones condicionales.
- Los operadores `and`, `or`, `not` permiten evaluar múltiples condiciones.
- `match-case` es útil para evaluar múltiples casos de una variable (Python 3.10+).
- `break` y `continue` modifican el comportamiento de los bucles.
- `else` en bucles se ejecuta solo si el bucle no se interrumpe con `break`.
"""

# ========================================
# Ejercicios de Práctica
# ========================================

"""
## 🧠 Ejercicios de práctica para if / elif / else

1️⃣ Clasifica una temperatura:
   - Si es mayor o igual a 30°C, imprime "Hace calor".
   - Si está entre 20°C y 29°C, imprime "Está templado".
   - Si es menor de 20°C, imprime "Hace frío".

2️⃣ Clasifica un número ingresado por el usuario:
   - Imprime "Positivo" si el número es mayor a 0.
   - Imprime "Negativo" si es menor a 0.
   - Imprime "Cero" si es igual a 0.

3️⃣ Evalúa una nota del 0 al 100:
   - "Excelente" si es 90 o más.
   - "Bien" si está entre 70 y 89.
   - "Suficiente" si está entre 60 y 69.
   - "Insuficiente" si es menor de 60.

4️⃣ Pregunta al usuario si tiene membresía (sí/no) y cuánto gastó:
   - Si tiene membresía y gastó más de 100, imprime "Descuento aplicado".
   - Si tiene membresía pero gastó 100 o menos, imprime "Compra mínima no alcanzada".
   - Si no tiene membresía, imprime "No aplica descuento".

5️⃣ Selección de fruta:
   - Pide al usuario que escriba una fruta (manzana, banana, naranja).
   - Usa `match-case` para imprimir un mensaje distinto por fruta.
   - Si no es ninguna de esas, imprime "Fruta no reconocida".

6️⃣ Validación con `not`:
   - Declara una variable `llueve = False`.
   - Usa `not` para imprimir "Puedes salir sin paraguas" si no está lloviendo.

✅ Prueba a resolver cada uno con lo aprendido sobre condicionales.
"""

# --------------------------------------------------
# 1️⃣ Clasifica una temperatura
# --------------------------------------------------

def temp(c):
    if c >= 30:
        return "Hace calor."
    elif c >= 20:
        return "Está templado."
    else:
        return "Hace frío."

# --------------------------------------------------
# 2️⃣ Clasifica un número como positivo, negativo o cero
# --------------------------------------------------

def nums(num):
    if num > 0:
        return f"El numero {num} es positivo."
    elif num < 0 :
        return f"El numero {num} es negativo."
    else:
        return f"El numero {num} es cero."

# --------------------------------------------------
# 3️⃣ Evalúa una nota de 0 a 100
# --------------------------------------------------

def grades(grade):
    if grade >= 90:
        return f"La nota es de {grade}, lo cual es 'excelente'."
    elif grade >= 70:
        return f"La nota es de {grade}, lo cual es 'bien'."
    elif grade >= 60:
        return f"La nota es de {grade}, lo cual es 'suficiente'."
    else:
        return f"La nota es de {grade}, lo cual es 'insuficiente'."

# --------------------------------------------------
# 4️⃣ Verifica membresía y gasto
# --------------------------------------------------

membresia = True
check = 120

if membresia == True and check > 100:
    print("Descuento aplicado")
elif membresia == True and check <= 100:
    print("Compra minima no alcanzada")
else:
    print("No aplica descuento")

# --------------------------------------------------
# 5️⃣ Usa `match-case` para seleccionar una fruta
# --------------------------------------------------

fruta = input("Seleccione una fruta: Manzana, Pera o Sandia: ")

match fruta:
    case 1:
        print("Comeras Manzana")
    case 2:
        print("Comeras Pera")
    case _:
        print("Comeras Sandia")


# --------------------------------------------------
# 6️⃣ Usa `not` para validar una condición
# --------------------------------------------------

llueve = False
if not llueve:
    print("Puedes salir sin paraguas.")

# ========================================
# Fin del Documento
# ========================================