# ========================================
# Uso de Diccionarios en Python
# ========================================

"""
## 📌 Descripción

Un diccionario en Python es una estructura de datos que almacena información en **pares clave-valor**.
Cada **clave** es única e inmutable (por ejemplo: cadenas, números, tuplas) y se utiliza para acceder a su **valor**, que puede ser de cualquier tipo. Es importante destacar que los diccionarios son colecciones **no ordenadas** de pares clave-valor. Además, los diccionarios son **mutables**, lo que permite agregar, modificar o eliminar sus elementos después de su creación.

📌 **Sintaxis Básica:**
    mi_diccionario = {
        'clave1': valor1,
        'clave2': valor2,
        ...
    }
Los valores pueden ser de cualquier tipo, pero las claves deben ser inmutables.
"""

# ========================================
# Ejemplo Básico de Diccionario
# ========================================

# Creación de un diccionario con datos de una persona
persona = {
    "nombre": "Jacob",
    "edad": 28,
    "ciudad": "Santiago"
}

print(persona["nombre"])  # Accede e imprime el valor asociado a la clave "nombre"

# Acceso y escritura de datos en diccionarios:
# Para acceder a un valor, se utiliza su clave. Si se desea cambiar el valor de una clave existente, se puede sobrescribir asignando un nuevo valor a la misma clave.

# ========================================
# Agregar, Modificar y Eliminar Elementos
# ========================================

"""
1️⃣ Agregar Elementos:  
   Para insertar un nuevo par clave-valor, simplemente se asigna el valor a la nueva clave:
       persona["profesion"] = "Desarrollador"

2️⃣ Modificar Elementos:  
   Para cambiar el valor de una clave existente:
       persona["edad"] = 29

3️⃣ Eliminar Elementos:  
   Se puede eliminar un elemento usando la instrucción 'del':
       del persona["ciudad"]
"""

# Agregar nueva clave
persona["profesion"] = "Desarrollador"

# Modificar valor existente
persona["edad"] = 29

# Eliminar una clave
del persona["ciudad"]

print(persona)  # Muestra el diccionario actualizado

# ========================================
# Combinación de Diccionarios
# ========================================

"""
Puedes combinar dos diccionarios utilizando el método .update(), que actualiza el diccionario existente con los pares clave-valor de otro diccionario.
"""

# Ejemplo de combinación de diccionarios
nuevos_datos = {
    "pais": "Chile",
    "telefono": "123456789"
}
persona.update(nuevos_datos)  # Combina nuevos_datos en el diccionario persona
print(persona)

# ========================================
# Iterar sobre Diccionarios
# ========================================

"""
Puedes recorrer un diccionario de diferentes maneras:

- **Claves:** Con .keys()
- **Valores:** Con .values()
- **Pares (clave, valor):** Con .items()
"""

# Iteración sobre las claves
for clave in persona.keys():
    print(f"Clave: {clave}")

# Iteración sobre los valores
for valor in persona.values():
    print(f"Valor: {valor}")

# Iteración sobre pares clave-valor
for clave, valor in persona.items():
    print(f"{clave}: {valor}")

# ========================================
# Comprobación de la Existencia de una Clave
# ========================================

"""
Antes de acceder a un valor, es recomendable verificar si la clave existe para evitar errores.
"""

if "nombre" in persona:
    print("La clave 'nombre' existe y su valor es:", persona["nombre"])

# ========================================
# Métodos Útiles en Diccionarios
# ========================================

"""
- .get(clave, valor_por_defecto): Retorna el valor asociado a 'clave'. Si la clave no existe, devuelve 'valor_por_defecto'.
- .pop(clave): Elimina la clave del diccionario y retorna su valor.
- .clear(): Elimina todos los elementos del diccionario.
"""

print(persona.get("nombre", "Desconocido"))
print(persona.get("altura", "No especificada"))  # Ejemplo de uso de get con valor por defecto

# ========================================
# Ejemplo del Método .pop()
# ========================================

"""
El método .pop() elimina un par clave-valor del diccionario y devuelve el valor eliminado.
"""

telefono_eliminado = persona.pop("telefono", "No existe")  # Elimina el teléfono y devuelve su valor
print("Teléfono eliminado:", telefono_eliminado)
print(persona)

# ========================================
# Diccionarios Anidados
# ========================================

"""
Los diccionarios anidados permiten tener un diccionario dentro de otro para representar datos más complejos.
"""

estudiantes = {
    "Juan": {"edad": 20, "carrera": "Ingeniería"},
    "Ana": {"edad": 22, "carrera": "Medicina"}
}

print(estudiantes["Ana"]["carrera"])  # Accede al valor anidado de 'carrera' de Ana

# ========================================
# Ejercicios de Práctica
# ========================================

"""
Resuelve los siguientes ejercicios para practicar:

1️⃣ Crear un diccionario con los datos de una persona:  
   Define un diccionario con las claves: 'nombre', 'edad' y 'país'.
   
       persona = {
           "nombre": "Nicole",
           "edad": 24,
           "país": "México"
       }

2️⃣ Agregar la clave 'profesión':  
   Añade la clave con el valor que prefieras.
   
       persona["profesión"] = "Bailarina"

3️⃣ Modificar el valor de 'edad':
   
       persona["edad"] = 25

4️⃣ Verificar la existencia de la clave 'nombre' e imprimirla:
   
       if "nombre" in persona:
           print(persona["nombre"])

5️⃣ Eliminar la clave 'país' y mostrar el diccionario resultante:
   
       del persona["país"]
       print(persona)

6️⃣ Crear un diccionario de estudiantes anidados:  
   Usa nombres como claves y otro diccionario como valor (con 'edad' y 'carrera').
   
       estudiantes = {
           "Carlos": {"edad": 21, "carrera": "Arquitectura"},
           "Laura": {"edad": 23, "carrera": "Biología"}
       }

7️⃣ Acceder al valor 'carrera' del estudiante 'Laura':
   
       print(estudiantes["Laura"]["carrera"])
"""

# ========================================
# Resumen
# ========================================

"""
🔑 Conceptos Clave:

- Diccionarios: Estructuras de datos que almacenan pares clave-valor.
- Claves: Únicas e inmutables.
- Valores: Pueden ser de cualquier tipo y pueden modificarse.
- Operaciones: Se pueden agregar, modificar, eliminar y verificar elementos de manera sencilla.
- Iteración: Existen métodos para recorrer claves, valores o ambos.
- Métodos Útiles: .get(), .pop(), y .clear() facilitan el manejo de los diccionarios.
- Diccionarios Anidados: Permiten representar datos complejos mediante estructuras jerárquicas.
"""

# ========================================
# Fin de Apuntes
# ========================================
