# ========================================
# Función rental_car_cost para Costo de Alquiler de Coches
# ========================================

# Descripción:
"""
Esta función calcula el costo total de alquilar un coche basado en el número de días de alquiler.
Incluye descuentos según la duración del alquiler.
"""

# Versión inicial
def rental_car_cost(d):
    base_cost = 40 * d  # Costo base calculado por día
    if d >= 7:
        base_cost -= 50  # Descuento de $50 si se alquila por 7 días o más
    elif d >= 3:
        base_cost -= 20  # Descuento de $20 si se alquila por 3 días o más
    return base_cost  # Retornamos el costo total con descuentos aplicados

# Refactorización usando comprensión de condiciones
def rental_car_cost_refactored(d):
    base_cost = 40 * d  # Costo base calculado por día
    discount = 50 if d >= 7 else 20 if d >= 3 else 0  # Operador ternario para determinar el descuento
    return base_cost - discount  # Aplicamos el descuento directamente al retornar el valor

# Ejemplo de uso:
days = 5
print(rental_car_cost(days))  # Uso de la función inicial
print(rental_car_cost_refactored(days))  # Uso de la función refactorizada

# ========================================
# Fin del Documento
# ========================================