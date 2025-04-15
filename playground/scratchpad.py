# ========================================
# Archivo de Práctica - Python
# ========================================

"""
## 📌 Descripción:
Este archivo contiene ejercicios para practicar estructuras de control, listas, loops y funciones.
Cada sección tiene ejercicios resueltos con explicaciones detalladas.
También incluye pruebas para verificar el correcto funcionamiento de cada solución.
"""

# ========================================
# 📝 Sección 1: While Loops
# ========================================

# Ejercicio 1: Contador descendente
# 🔹 Escribe un while loop que imprima los números del 10 al 1 en orden descendente.
# 🔹 Una vez que llegue a 1, debe imprimir "¡Despegue!".

print("\n🟢 Ejercicio 1: Contador descendente")

counter = 10
while counter > 0:  # Mientras el contador sea mayor a 0
    print(counter)   # Imprime el valor actual del contador
    counter -= 1     # Disminuye el contador en 1 en cada iteración

print("¡Despegue!")  # Cuando el loop termina, imprime "¡Despegue!"

# Prueba: No necesita valores de entrada, se ejecuta directamente.


# ----------------------------------------


# Ejercicio 2: Solicitar número par
# 🔹 Escribe un while loop que pida al usuario un número.
# 🔹 Si el número ingresado NO es par, el programa debe seguir pidiendo otro número.
# 🔹 Cuando el usuario ingrese un número par, el programa debe imprimir "Número válido" y terminar.

print("\n🟢 Ejercicio 2: Solicitar número par")

while True:
    num = int(input("Ingresa un número par: "))  # Pedimos un número
    if num % 2 == 0:  # Si el número es par (residuo 0 al dividir por 2)
        print("Número válido")
        break  # Sale del bucle

    print("Número inválido, intenta de nuevo")

# Prueba: Ejecutar el código e ingresar diferentes números (pares e impares).


# ========================================
# 📝 Sección 2: Listas y Loops
# ========================================

# Ejercicio 3: Contar números positivos en una lista
# 🔹 Escribe un programa que reciba una lista de números y cuente cuántos son positivos.

print("\n🟢 Ejercicio 3: Contar números positivos en una lista")

def positive_nums(numbers):
    counter = 0  # Inicializamos el contador en 0
    for number in numbers:  # Iteramos sobre cada número en la lista
        if number > 0:  # Si el número es mayor que 0
            counter += 1  # Incrementamos el contador
    return counter

# Prueba con diferentes listas
numbers = [3, -1, 5, 0, -8, 10, -2]
print("Números positivos en la lista:", positive_nums(numbers))


# ----------------------------------------


# Ejercicio 4: Reemplazar negativos por cero
# 🔹 Si un número es negativo, reemplázalo por 0.

print("\n🟢 Ejercicio 4: Reemplazar negativos por cero")

def negatives_per_zero(my_list):
    for i in range(len(my_list)):  # Iteramos sobre los índices de la lista
        if my_list[i] < 0:  # Si el número es negativo
            my_list[i] = 0  # Lo reemplazamos por 0
    return my_list

# Prueba:
numbers = [3, -1, 5, 0, -8, 10, -2]
print("Lista modificada:", negatives_per_zero(numbers))


# ========================================
# 📝 Sección 3: Funciones
# ========================================

# Ejercicio 5: Máximo de tres números
# 🔹 Escribe una función max_of_three(a, b, c) que devuelva el mayor de los tres.

print("\n🟢 Ejercicio 5: Máximo de tres números")

def max_of_three(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

# Pruebas con diferentes valores
print(max_of_three(10, 13, 9))   # 13
print(max_of_three(5, 5, 3))     # 5
print(max_of_three(7, 2, 7))     # 7
print(max_of_three(4, 4, 4))     # 4


# ----------------------------------------


# Ejercicio 6: Verificar si un número es primo

print("\n🟢 Ejercicio 6: Verificar si un número es primo")

def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    for i in range(2, int(n**0.5) + 1):  # Optimizamos iterando hasta √n
        if n % i == 0:
            return False
    return True

# Pruebas con diferentes números
print(is_prime(7))  # True
print(is_prime(10)) # False
print(is_prime(23)) # True
print(is_prime(25)) # False


# ========================================
# 📝 Sección 4: Desafíos Extras
# ========================================

# Ejercicio 7: Invertir una lista

print("\n🟢 Ejercicio 7: Invertir una lista")

def invertir_lista(lista):
    inverted_list = []  # Creamos una lista vacía
    for i in range(len(lista) - 1, -1, -1):  # Recorremos la lista en orden inverso
        inverted_list.append(lista[i])  # Agregamos cada elemento a la nueva lista
    return inverted_list

# Prueba con una lista
numbers = [1, 2, 3, 4, 5]
print("Lista invertida:", invertir_lista(numbers))  # [5, 4, 3, 2, 1]


# ----------------------------------------


# Ejercicio 8: Contar vocales en una palabra

print("\n🟢 Ejercicio 8: Contar vocales en una palabra")

def contar_vocales(palabra):
    counter = 0  # Inicializamos el contador en 0
    for letra in palabra:  # Iteramos sobre cada letra de la palabra
        if letra in "aeiouAEIOU":  # Si la letra es una vocal
            counter += 1  # Incrementamos el contador
    return counter

# Pruebas con diferentes palabras
print(contar_vocales("hola"))  # 2
print(contar_vocales("Python"))  # 1
print(contar_vocales("AEIOU"))  # 5
print(contar_vocales("rhythm"))  # 0


# ========================================
# Fin del Archivo de Práctica
# ========================================

