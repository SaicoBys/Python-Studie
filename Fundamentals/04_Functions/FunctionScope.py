# ========================================
# Funciones en Python - Ámbito de Variables
# ========================================

"""
## Descripción
El ámbito de una variable determina en qué partes del código puede ser utilizada.
En Python, existen los siguientes tipos de ámbito:

1. **Ámbito Local**: Variables definidas dentro de una función, solo accesibles dentro de ella.
2. **Ámbito Global**: Variables definidas fuera de funciones, accesibles en todo el programa.
3. **Palabra Clave `global`**: Permite modificar variables globales dentro de una función.
4. **Palabra Clave `nonlocal`**: Permite modificar variables en un ámbito intermedio dentro de funciones anidadas.
"""

# ========================================
# 1. Ámbito Local
# ========================================

"""
Las variables creadas dentro de una función solo existen dentro de ella.
Intentar acceder a ellas fuera de la función generará un error.
"""

def funcion_local():
    x = 10  # Variable local
    print(f"Valor de x dentro de la función: {x}")

funcion_local()

# ❌ Intento de acceder a una variable local fuera de su función (provocará un error)
# print(x)  # Esto generaría un NameError porque x solo existe dentro de la función

# ========================================
# 2. Ámbito Global
# ========================================

"""
Las variables globales se definen fuera de cualquier función y pueden ser accedidas desde cualquier parte del código.
"""

y = 20  # Variable global

def funcion_global():
    print(f"Valor de y dentro de la función: {y}")

funcion_global()
print(f"Valor de y fuera de la función: {y}")

"""
⚠ **Advertencia sobre Variables Globales**:
El uso excesivo de variables globales puede hacer que el código sea más difícil de depurar y mantener.
Siempre que sea posible, es mejor usar variables locales dentro de funciones.
"""

# ========================================
# 3. Uso de `global` para modificar variables globales dentro de funciones
# ========================================

"""
Si intentamos modificar una variable global dentro de una función sin declararla como `global`, Python la tratará como una variable local.
"""

contador = 0  # Variable global

def incrementar_contador():
    global contador  # Declaramos que vamos a modificar la variable global
    contador += 1
    print(f"Contador dentro de la función: {contador}")

incrementar_contador()
print(f"Contador fuera de la función: {contador}")

"""
⚠ **Advertencia sobre `global`**:
El uso de `global` puede generar efectos secundarios no deseados si varias funciones modifican la misma variable global.
Es recomendable evitarlo en programas grandes para mejorar la modularidad.
"""

# ========================================
# 4. Uso de `nonlocal` para modificar variables en funciones anidadas
# ========================================

"""
`nonlocal` permite modificar variables en un ámbito intermedio dentro de una función anidada.
"""

def funcion_externa():
    mensaje = "Hola"
    
    def funcion_interna():
        nonlocal mensaje  # Modifica la variable en el ámbito intermedio
        mensaje = "Hola, modificado"
        print(f"Mensaje dentro de la función interna: {mensaje}")
    
    funcion_interna()
    print(f"Mensaje dentro de la función externa: {mensaje}")

funcion_externa()

"""
📌 **¿Cuándo usar `nonlocal`?**
- Útil cuando una función interna necesita modificar una variable definida en la función externa.
- No se puede usar `nonlocal` con variables globales, solo con variables en ámbitos intermedios.
"""

# ========================================
# Resumen
# ========================================

"""
📌 **Resumen del Ámbito de Variables en Python**:
- **Local**: Variables creadas dentro de una función, solo accesibles ahí.
- **Global**: Variables accesibles en todo el código.
- **global**: Permite modificar variables globales dentro de una función, pero su uso debe ser limitado.
- **nonlocal**: Permite modificar variables en un ámbito intermedio en funciones anidadas.

✔ Comprender el ámbito de las variables es clave para evitar errores y escribir código limpio y estructurado.
"""

# ========================================
# Fin del Documento
# ========================================
