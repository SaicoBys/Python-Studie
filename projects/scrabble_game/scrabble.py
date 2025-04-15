# ========================================
# 🧩 Sección 5: Preparación para Proyecto Scrabble
# ========================================

"""
Esta sección te ayudará a dominar los conceptos necesarios para resolver el proyecto de Scrabble de manera independiente.
Incluye ejercicios sobre: diccionarios con zip(), funciones, bucles anidados y manipulación de datos.
"""

# 🔹 Parte 1: Crear diccionario de puntos con zip() y dict()

print("\n🟢 Scrabble - Parte 1: Diccionario de puntos")

letters = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", 
    "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", 
    "U", "V", "W", "X", "Y", "Z"
]

points = [
    1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 
    5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 
    1, 4, 4, 8, 4, 10
]

# Creamos el diccionario
letter_to_points = dict(zip(letters, points))  # Unimos la lista y la convertimos en diccionario
letter_to_points[" "] = 0  # Añadimos la ficha en blanco

print(letter_to_points)

# 🔹 Parte 2: Función para puntuar una palabra

print("\n🟢 Scrabble - Parte 2: Función score_word()")

def score_word(word):
    point_total = 0
    for letter in word:  # Iteramos sobre cada letra, para guardarla en la variable letter
        point_total += letter_to_points.get(letter.upper(), 0)  # Verificamos si la variable se encuentra
    return point_total

# Pruebas
print("Puntos de BROWNIE:", score_word("BROWNIE"))
print("Puntos de HELLO:", score_word("HELLO"))
print("Puntos de PYTHON:", score_word("PYTHON"))

# 🔹 Parte 3: Diccionario de jugadores y palabras

print("\n🟢 Scrabble - Parte 3: Diccionario player_to_words")

player_to_words = {
    "player1": ["BLUE", "TENNIS", "EXIT"],
    "wordNerd": ["EARTH", "EYES", "MACHINE"],
    "Lexi Con": ["ERASER", "BELLY", "HUSKY"],
    "Prof Reader": ["ZAP", "COMA", "PERIOD"]
}

# Acceder y modificar
print("Palabras de Lexi Con:", player_to_words["Lexi Con"])
player_to_words["player1"].append("SUN")
print("Palabras nuevas de player1:", player_to_words["player1"])

# 🔹 Parte 4: Calcular puntuaciones totales por jugador

print("\n🟢 Scrabble - Parte 4: Diccionario player_to_points")

player_to_points = {}

for player, words in player_to_words.items():
    player_points = 0
    for word in words:
        player_points += score_word(word)
    player_to_points[player] = player_points

print("Puntajes totales por jugador:", player_to_points)

# 🔹 Parte 5: Agregar nuevas palabras jugadas

print("\n🟢 Scrabble - Parte 5: Agregando palabras nuevas play_word")

def play_word(player, word):
    """Agrega una palabra nueva a un jugador específico."""
    if player in player_to_words:
        player_to_words[player].append(word)
    else:
        player_to_words[player] = [word]

    # Actualiza los puntos del jugador
    player_to_points[player] = sum(score_word(w) for w in player_to_words[player])

# Prueba de la función
play_word("player1", "CODE")
print("Palabras actualizadas de player1:", player_to_words["player1"])
print("Nuevo puntaje de player1:", player_to_points["player1"])
