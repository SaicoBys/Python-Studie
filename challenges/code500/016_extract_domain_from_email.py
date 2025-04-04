# ========================================
"""
📌 CHALLENGE #016: extract_domain_from_email
- Escribe una función que reciba una dirección de correo electrónico y retorne su dominio.
- Utiliza el método split() para separar el correo en la parte que aparece después del "@".

🧠 Ejemplo:
Entrada: "user@example.com"
Salida esperada: "example.com"
"""
# ========================================
entrada = "user@example.com"

def extract_domain_from_email(mail):
    return mail.split("@")[-1]

print(extract_domain_from_email(entrada))