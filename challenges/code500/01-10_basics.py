# ========================================
# 001: Contar números pares
# ========================================
print("Desafío 001")

even_count = 0
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in num_list:            # Recorro la lista de números uno por uno.
    if num % 2 == 0:            # Verifico si el número es divisible entre 2 (par).
        even_count += 1         # Incremento el contador si el número es par.

print(f"Total of even numbers: {even_count}")



# ========================================
# 002: Invertir un string
# ========================================
print("Desafío 002")

word = "python"  # Asignamos el string "python" a la variable `word`

# Recorremos el string desde el último carácter hacia el primero
for char in range(len(word) - 1, -1, -1):  
    # `range(len(word) - 1, -1, -1)` es el rango de índices para recorrer el string desde el final.
    # El primer -1 indica el inicio en el último índice del string (len(word) - 1)
    # El segundo -1 indica el final del rango, que es antes de llegar a `-1` (esto permite incluir el primer carácter, que tiene índice 0)
    # El tercer -1 es el paso, indicando que estamos recorriendo los índices de atrás hacia adelante (en orden inverso).

    print(word[char])  # Imprime cada carácter en orden inverso. La variable `char` contiene el índice de cada carácter a imprimir.


# ========================================
# 003: Sumar los positivos
# ========================================
print("Desafío 003")

result = 0
lst = [2, -3, -4, 5, -6, 5]

for num in lst:         # Recorro cada número en la lista para verificar si es positivo
    if num < 0:         # Si el número es negativo, lo omito con continue
        continue
    else:
        result += num   # Si el número es positivo, lo sumo a result
print(result)



# ========================================
# 004: Verificar si es palíndromo
# ========================================
print("Desafío 004")

def is_palindrome(input_word):
    reversed_word = ""
    for index in range(len(input_word) - 1, -1, -1):
        reversed_word += input_word[index]

    if reversed_word.lower() == input_word.lower():
        return True
    return False

print(is_palindrome("Radar"))



# ========================================
# 005: Máximo de tres números
# ========================================
print("Desafío 005")

def max_of_three(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
    
print(max_of_three(12, 13, 15))



# ========================================
# 006: Ordenar una lista
# ========================================
print("Desafío 006")

def order_list(lst):
    lst.sort()
    return lst


numbers_list = [12, 5, 9, 2]
print(order_list(numbers_list))



# ========================================
# 007: Contar vocales en un string
# ========================================
print("Desafío 007")

def counting_vowels(word):
    vowels = "aeiou"
    counter = 0
    for index in word:
        if index in vowels:
            counter += 1
    return counter
        

print(counting_vowels("Nicole"))



# ========================================
# 008: Encontrar el menor número
# ========================================
print("Desafío 008")

unsorted_list = [12, 5, 9, 2]

def find_smallest(nums):
    minor = nums[0]
    for num in nums:
        if num < minor:
            minor = num
    return minor

print(find_smallest(unsorted_list))



# ========================================
# 009: Invertir una lista
# ========================================
print("Desafío 009")

nums = [2, 3, 5, 2, 6, 3, 5]

def reverse_list(lst):
    new_list = []
    for index in range(len(lst) -1, -1, -1):
        new_list.append(lst[index])
    return new_list
    
print(reverse_list(nums))



# ========================================
# 010: Buscar palabra en un texto
# ========================================
print("Desafío 010")

def find_word(word, txt):
    if word in txt:
        return True
    return False

print(find_word("Jacob", "Hola, Jacob"))
