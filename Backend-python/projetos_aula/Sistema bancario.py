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
    opcao = int(input("[1] - sacar \n[2] - depositar \n[3] - extrato  \n[0] - saindo " \
    "\nQual das operações o Sr. deseja: "))

    

    if opcao == 1:
      valor = float(input(f"Qual o valor que o senhor deseja saca: R$ "))

      if valor <= 0: # foi adicioando esse codigo para trata o erro de valor negativo 
        print("valor invalido.")

      if valor > saldo:
        print("Saldo insuficiente.")

      elif valor > limite_saque:
        print("O valor passou do seu limite.")

      elif numero_saque >= limite_saque_diarios:
        print("O senhor já chegou no limite do saque diario.")

      else:
        saldo -= valor
        numero_saque += 1
        extrato += f"saque:R${valor:.2f}\n"
        print("Saque realizado com sucesso.")
   

    elif opcao == 2:
      valor = input("Quanto o senhor deseja deposita:R$ ")

      valor = float(valor)  # foi adicioando esse codigo para trata o erro

      if valor <= 0:
          print("valor não permitido para deposita")
      
      else:
          saldo += valor
          extrato += f"deposito: R${valor:.2f}\n"
          print("deposito realizado com sucesso.")

   
    elif opcao == 3: 
         print("=-=-=-=-=-=-=-=-==-=-=")
         print("EXTRATO BANCARIO")
         print("=-=-=-=-=-=-=-=-==-=-=")
    
         if extrato == "":
            saldo == extrato
            print(f"saldo da conta R${saldo}")

         else:
            print(extrato)
            print(f"saldo da conta: R${saldo:.2f}\n") 

    elif opcao == 0:
      print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
      print("Obrigado por ser nosso cliente!")
      print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
      break

    else:
      print("Opção invalida tente novamente as operações.")
   










