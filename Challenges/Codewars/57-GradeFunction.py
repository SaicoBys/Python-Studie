# ========================================
# Función get_grade para Calificaciones en Python
# ========================================

# Descripción:
"""
La función `get_grade` calcula el promedio de tres calificaciones y devuelve la calificación
correspondiente en formato de letra. Este es un ejemplo de cómo se pueden usar
condicionales para determinar rangos y asociar valores específicos a esos rangos.
"""

# Definición de la función:
"""
La función acepta tres argumentos: s1, s2, y s3, que representan las calificaciones
de un estudiante. Estas son sumadas y divididas por tres para obtener el promedio.
"""

# Código de la función:
def get_grade(s1, s2, s3):
    # Calculamos el promedio de los tres puntajes
    score = (s1 + s2 + s3) / 3
    
    # Condicionales para determinar la letra de la calificación basada en el promedio
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

# Refactorización con diccionario
def get_grade_refactored(s1, s2, s3):
    """
    Versión refactorizada utilizando un diccionario para mapear rangos de puntajes a calificaciones.
    Esto permite una comparación más clara y una menor cantidad de condicionales if/elif.
    """
    score = (s1 + s2 + s3) / 3
    grades = {range(90, 101): 'A', range(80, 90): 'B', range(70, 80): 'C', range(60, 70): 'D'}
    return next((grade for scores, grade in grades.items() if score in scores), 'F')

# Ejemplo de uso:
print(get_grade(85, 90, 92))  # Salida: A
print(get_grade_refactored(85, 90, 92))  # Salida: A

# ========================================
# Fin del Documento
# ========================================