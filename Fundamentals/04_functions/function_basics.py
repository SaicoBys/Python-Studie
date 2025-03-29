# ========================================
# Conceptos Básicos de Funciones en Python
# ========================================

"""
## 📌 Descripción
Las funciones en Python permiten encapsular bloques de código para su reutilización y organización.
Son fundamentales para estructurar programas de manera modular y eficiente.

### 📌 Beneficios de usar funciones:
- **Reutilización del código**: Evita duplicación y facilita mantenimiento.
- **Modularidad**: Se puede dividir el código en partes más manejables.
- **Facilitan la depuración**: Es más fácil probar funciones individuales.
"""

# ========================================
# 1. Definición de una Función
# ========================================

"""
Las funciones se definen usando `def` seguido del nombre de la función y paréntesis.

📌 **Sintaxis**:
def nombre_funcion():
    # Código dentro de la función
"""

# Ejemplo básico de función
def saludar():
    """Imprime un mensaje de bienvenida."""
    print("¡Hola, bienvenido a Python!")  # Imprime el mensaje de saludo

saludar()  # Llamada a la función que ejecuta el saludo

# ========================================
# 2. Parámetros en Funciones
# ========================================

"""
Las funciones pueden aceptar parámetros para recibir valores al ser llamadas.

📌 **Tipos de parámetros:**
1. **Parámetros obligatorios**: Se deben proporcionar al llamar la función.
2. **Parámetros con valores por defecto**: Se usan si no se proporciona un valor.
"""

# Ejemplo de parámetros
def informacion(nombre, edad=18):
    """Muestra información de una persona."""
    print(f"Nombre: {nombre}, Edad: {edad}")  # Imprime el nombre y la edad

informacion("Carlos", 25)  # Parámetros explícitos: nombre y edad
informacion("Ana")  # Usa el valor por defecto de `edad`

# ========================================
# 3. Valores de Retorno
# ========================================

"""
Las funciones pueden devolver valores usando `return`. Esto permite capturar y utilizar los resultados.
"""

# Retorno de un solo valor
def cuadrado(num):
    """Devuelve el cuadrado de un número."""
    return num ** 2  # Calcula el cuadrado del número y lo devuelve

print(cuadrado(4))  # 16, llama a la función y muestra el resultado

# Retorno de múltiples valores
def operaciones(a, b):
    """Devuelve la suma y la resta de dos números."""
    suma = a + b  # Calcula la suma
    resta = a - b  # Calcula la resta
    return suma, resta  # Devuelve ambos resultados

resultado_suma, resultado_resta = operaciones(10, 5)  # Llama a la función y captura los resultados
print(f"Suma: {resultado_suma}, Resta: {resultado_resta}")  # Imprime los resultados

# ========================================
# 4. Parámetros con Valores por Defecto
# ========================================

"""
Podemos asignar valores por defecto a los parámetros. Si no se proporciona un valor al llamar la función,
se usará el valor por defecto.
"""

def presentar(nombre="Usuario", edad=18):
    """Muestra un mensaje con nombre y edad con valores por defecto."""
    print(f"Nombre: {nombre}, Edad: {edad}")  # Imprime el nombre y la edad

presentar("Carlos", 25)  # Llama a la función con parámetros específicos
presentar()  # Usa los valores por defecto

# ========================================
# 5. Argumentos Variables: *args y **kwargs
# ========================================

"""
- `*args` permite pasar múltiples valores como una tupla.
- `**kwargs` permite pasar múltiples pares clave-valor como un diccionario.
"""

# Uso de *args
def sumar_todo(*numeros):
    """Suma todos los números proporcionados."""
    return sum(numeros)  # Suma todos los números en la tupla y devuelve el resultado

print(sumar_todo(1, 2, 3, 4, 5))  # 15, llama a la función y muestra la suma

# Uso de **kwargs
def mostrar_info(**datos):
    """Muestra información proporcionada como clave-valor."""
    for clave, valor in datos.items():  # Itera sobre los pares clave-valor
        print(f"{clave}: {valor}")  # Imprime cada par clave-valor

mostrar_info(nombre="Ana", edad=22, ciudad="Madrid")  # Llama a la función con datos

# ========================================
# Resumen
# ========================================

"""
📌 **Resumen de Funciones en Python**:
- Se usa `def` para definir funciones.
- Las funciones pueden aceptar **parámetros** y devolver valores con `return`.
- `*args` permite pasar múltiples valores como tupla.
- `**kwargs` permite pasar múltiples valores como pares clave-valor.
- Se pueden definir **valores por defecto** en los parámetros de una función.
- Las funciones pueden devolver **uno o múltiples valores**.
"""

# ========================================
# Ejercicios de Práctica
# ========================================

"""
## 🧠 Ejercicios de práctica sobre funciones

1️⃣ Escribe una función llamada `saludo_personalizado(nombre)` que imprima un saludo personalizado usando el nombre proporcionado.

2️⃣ Crea una función `area_rectangulo(base, altura)` que calcule y retorne el área de un rectángulo.

3️⃣ Define una función `multiplicar_lista(*numeros)` que use `*args` para multiplicar todos los números pasados como argumento.

4️⃣ Crea una función `mostrar_perfil(**datos)` que reciba cualquier cantidad de datos (nombre, edad, ciudad, etc.) y los imprima en formato clave: valor.

5️⃣ Crea una función `calculo_salario(base, bonus=0)` que devuelva el salario total sumando base + bonus, siendo bonus un parámetro opcional.

✅ Prueba a resolverlos aplicando lo aprendido en este documento.
"""

# --------------------------------------------------
# 1️⃣ saludo_personalizado(nombre)
# --------------------------------------------------


# --------------------------------------------------
# 2️⃣ area_rectangulo(base, altura)
# --------------------------------------------------


# --------------------------------------------------
# 3️⃣ multiplicar_lista(*numeros)
# --------------------------------------------------


# --------------------------------------------------
# 4️⃣ mostrar_perfil(**datos)
# --------------------------------------------------


# --------------------------------------------------
# 5️⃣ calculo_salario(base, bonus=0)
# --------------------------------------------------


# ========================================
# Fin del Documento
# ========================================
