# ========================================
# === 029: crear_diccionario_personas ===
# ========================================
print("Desafío 029")

"""
📌 CHALLENGE #029: crear_diccionario_personas
- Crea un diccionario con las siguientes personas: "Juan": 28, "Ana": 22, "Luis": 35.
- Luego, agrega una nueva persona: "Marta": 30.

🧠 Ejemplo:
Entrada: {}
Salida esperada: {"Juan": 28, "Ana": 22, "Luis": 35, "Marta": 30}
"""

personas = {
    "Jacob": 28,
    "Ana": 22,
    "Luis": 35,
    "Marta": 30
}

personas["Marta"] = 31
print(personas)

# ========================================
# === 030: acceder_valores_diccionario ===
# ========================================
print("Desafío 030")

"""
📌 CHALLENGE #030: acceder_valores_diccionario
- Imprime la edad de "Luis" usando el diccionario creado.

🧠 Ejemplo:
Entrada: {"Juan": 28, "Ana": 22, "Luis": 35}
Salida esperada: 35
"""

print(personas.get("Luis", "No value"))


# ========================================
# === 031: actualizar_valores_diccionario ===
# ========================================
print("Desafío 031")

"""
📌 CHALLENGE #031: actualizar_valores_diccionario
- Cambia la edad de "Ana" a 23.

🧠 Ejemplo:
Entrada: {"Juan": 28, "Ana": 22, "Luis": 35}
Salida esperada: {"Juan": 28, "Ana": 23, "Luis": 35}
"""

personas["Ana"] = 23
print(personas["Ana"])

# ========================================
# === 032: verificar_clave_diccionario ===
# ========================================
print("Desafío 032")

"""
📌 CHALLENGE #032: verificar_clave_diccionario
- Escribe un programa que verifique si "Carlos" está en el diccionario.

🧠 Ejemplo:
Entrada: {"Juan": 28, "Ana": 22, "Luis": 35}
Salida esperada: False
"""

print("Carlos" in personas)

# ========================================
# === 033: contar_letras_string ===
# ========================================
print("Desafío 033")

"""
📌 CHALLENGE #033: contar_letras_string
- Contar cuántas veces aparece cada letra en un string.
- Ejemplo de string: "banana".
- Resultado esperado: {'b': 1, 'a': 3, 'n': 2}.

🧠 Ejemplo:
Entrada: "banana"
Salida esperada: {'b': 1, 'a': 3, 'n': 2}
"""

cadena = "Banana"

def contar_letras_string(cadena):
    contador = {}

    for letra in cadena:
        if letra in contador:
            contador[letra] += 1
        else:
            contador[letra] = 1
    
    return contador

print(contar_letras_string(cadena))

# ========================================
# === 034: crear_diccionario_desde_listas ===
# ========================================
print("Desafío 034")

"""
📌 CHALLENGE #034: crear_diccionario_desde_listas
- Usando estas listas: nombres = ["Alice", "Bob", "Charlie"] y edades = [25, 30, 35].
- Une ambas listas en un diccionario.

🧠 Ejemplo:
Entrada: (["Alice", "Bob", "Charlie"], [25, 30, 35])
Salida esperada: {"Alice": 25, "Bob": 30, "Charlie": 35}
"""

def crear_diccionario_desde_listas(lst1, lst2):
    diccionario = {}
    for k, v in zip(lst1, lst2):
        diccionario[k] = v
    return diccionario

nombres = ["Alice", "Bob", "Charlie"]
edades = [25, 30, 35]
print(crear_diccionario_desde_listas(nombres, edades))

# ========================================
# === 035: filtrar_elementos_pares ===
# ========================================
print("Desafío 035")

"""
📌 CHALLENGE #035: filtrar_elementos_pares
- Usa el diccionario del ejercicio 29 y devuelve un nuevo diccionario solo con las personas que tienen edad par.

🧠 Ejemplo:
Entrada: {"Juan": 28, "Ana": 22, "Luis": 35, "Marta": 30}
Salida esperada: {"Juan": 28, "Ana": 22, "Marta": 30}
"""
# Tu código aquí


# ========================================
# === 036: contar_elementos_repetidos ===
# ========================================
print("Desafío 036")

"""
📌 CHALLENGE #036: contar_elementos_repetidos
- Dada la lista: colores = ["rojo", "azul", "rojo", "verde", "azul", "rojo"].
- Devuelve un diccionario con la cantidad de veces que aparece cada color.

🧠 Ejemplo:
Entrada: ["rojo", "azul", "rojo", "verde", "azul", "rojo"]
Salida esperada: {"rojo": 3, "azul": 2, "verde": 1}
"""
# Tu código aquí


# ========================================
# === 037: claves_mayores_a_30 ===
# ========================================
print("Desafío 037")

"""
📌 CHALLENGE #037: claves_mayores_a_30
- Crear una función que devuelva las claves de un diccionario que tengan valores mayores a 30.
- Usa el diccionario del ejercicio 29 como base.

🧠 Ejemplo:
Entrada: {"Juan": 28, "Ana": 22, "Luis": 35, "Marta": 30}
Salida esperada: ["Luis"]
"""
# Tu código aquí


# ========================================
# === 038: diccionario_letras_vocales ===
# ========================================
print("Desafío 038")

"""
📌 CHALLENGE #038: diccionario_letras_vocales
- Crear un diccionario donde cada letra del string sea una clave y su valor sea True si es vocal, False si no.
- Ejemplo con el string: "python".
- Resultado: {'p': False, 'y': False, 't': False, 'h': False, 'o': True, 'n': False}.

🧠 Ejemplo:
Entrada: "python"
Salida esperada: {'p': False, 'y': False, 't': False, 'h': False, 'o': True, 'n': False}
"""
# Tu código aquí