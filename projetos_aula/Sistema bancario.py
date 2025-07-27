print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("Seja Bem-vindo ao Banco Devpy!")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

saldo = 0.0
limite_saque = 500.0
numero_saque = 0
limite_saque_diarios = 3
extrato = ""
opcao = -1 

while opcao != 0:
    opcao = int(input("[1] - sacar \n[2] - depositar \n[3] - extrato  \n[4] - saindo " \
    "\nQual das operações o Sr. deseja: "))

    if opcao == 1:
        if saldo >= limite_saque:
         print("Saque realizado com sucesso")

    elif opcao == 2:
        print("Exibindo extrato ...")
   
    elif opcao == 3: 
         print(f"Dinheiro depositado R${saldo}")
         print(f"Dinheiro depositado R${numero_saque}")
         print(f"Dinheiro depositado R${limite_saque_diarios}")
         print(f"Dinheiro depositado R${extrato}")

    elif opcao == 4:
      print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
      print("Obrigado por ser nosso cliente!")
      print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
      break

    else:
      print("Opção invalida tente novamente as operações.")
   










