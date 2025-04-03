# ========================================
"""
📌 DESAFÍO #013: Sumar los positivos e invertir la lista
- Dada una lista de números, suma únicamente los números positivos y devuelve la lista invertida.

🧠 Ejemplo:
Entrada: [1, -2, 3, 4, -5]
Salida esperada:
- Suma de positivos: 8   (1 + 3 + 4)
- Lista invertida: [-5, 4, 3, -2, 1]
"""
# ========================================

enter = [1, -2, 3, 4, -5]

def sum_positives_reverse_list(lst):
    reversed_list = []
    nums = 0
    for index in range(len(lst) -1, -1, -1):
        reversed_list.append(lst[index])
        if lst[index] > 0:
            nums += lst[index]
    
    message = "The total is: {nums} and the order is: {reversed_list}".format(reversed_list=reversed_list, nums=nums)
    return message


print(sum_positives_reverse_list(enter))

