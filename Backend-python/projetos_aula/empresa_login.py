# entrada do usuario
email = input().strip()

# programa para valida os email
def validar_email(email):
    # verificar se falta o "@" ou se tem espaço no e-mail
    if "@" not in email or " " in email:
        return "e-mail invalido"
    # verufuca se começa ou termina com o "@"
    if email.start("@") or email.end("@"):
        return "e-mail invalido"
    
    
# TODO: Verifique as regras do e-mail:
"""Deve conter o caractere "@" e um domínio """
"""como gmail.com ou outlook.com."""
"""Não pode começar ou terminar com "@"."""
"""Não pode conter espaços."""

dominio_valido = ["gmail.com", "outlook.com"]
dominio_invalido = [
    ".@gmail.com",
    ".@outlook.com",
    "outlook.com@", 
    "gmailcom@",
    "@ gmail.com",
    "@ outlook.com",
    " gmail.com",
    " outlook.com"
]

# saida do usuario
print(validar_email(email))