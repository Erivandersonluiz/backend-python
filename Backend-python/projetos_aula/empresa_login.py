# TODO: Verifique as regras do e-mail:
"""Deve conter o caractere "@" e um domínio """
"""como gmail.com ou outlook.com """
"""Não pode começar ou terminar com "@" """
"""Não pode conter espaços """

# entrada do usuario
email = input().strip()

# programa para valida os email
def validar_email(email):
    # verificar se falta o "@" ou se tem espaço no e-mail
    if "@" not in email or " " in email:
        return "E-mail inválido"
    # verificarfica se começa ou termina com o "@"
    if email.startswith("@") or email.endswith("@"): # os metodos SWITH está na documentação oficial do python.
        return "E-mail inválido"
    # verificar o nome e dominio
    partes = email.split("@") # o split é uma string vazia com um separador especificado retorna.
    if len(partes) != 2:
        return "E-mail inválido"
    
    dominio = partes

    dominio_valido = ["gmail.com", "outlook.com"]

    if dominio not in dominio_valido:
        return "E-mail válido"

    return "E-mail válido"


# saida do usuario
print(validar_email(email))