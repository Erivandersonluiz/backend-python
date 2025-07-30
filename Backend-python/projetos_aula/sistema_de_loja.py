# Dicionário com os valores de desconto
descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

# Entrada do usuário
preco = float(input().strip())
cupom = input().strip()

# TODO: Aplique o desconto se o cupom for válido:
if cupom in descontos:
    preco_final = preco * (1 - descontos[cupom]) # esse final do codigo é para calcular os desconto 100 *(1 - 0.10)
else:
    preco_final = preco  # Caso o cupom seja inválido, não há desconto

# Saida do programa 
print(f"{preco_final:.2f}")
