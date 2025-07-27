
print("Óla, mundo!")

nome = input(f"Digite seu nome: ")
print("Seu nome é",nome)

idade = int(input(f" Diga sua idade: "))
print("Minha idade é",idade)

            #operadores aritméticos

""" a difinição indica a seguint ordem como
a correta: 
º Parênteses
º Exponentes
º Multiplicação e Divisão
º Adição e Subtração
º Igualdade
"""
# x = 10-5*2

"""
print (10 -5 * 2 )
resultado 0

print((10 - 5 ) * 2) 
resultado 10

print(10 ** 2 * 2)
# resultado 200

print (10 ** (2 * 2))
# resultado 10000

print(10 / 2 * 4)
# resultado 20.0
""" 

p = 20
r = 10
print (p + r )
print (p - r )
print (p / r )
print (p // r )


                # indentação 

print("=-=-=")
print("Bem vindo ao banco Dev!")
print("=-=-=")

saldo = 1000
print(f"saldo atual é: R${saldo}")

def sacar(valor):
    global saldo
    if saldo >= valor:
        saldo -= valor
        print(f"valor sacado: R${valor}")
    else:
        print("saldo insuficiente")

def depositar(valor):
    global saldo
    saldo += valor
    print(f"Valor depositado: R${valor}")

depositar_valor = float(input("deposite o valor: "))
depositar(depositar_valor)

sacar(500)

print(f"Saldo atual é de: R${saldo}")

print("=-=-=")
print("Obrigado por ser nosso cliente!")
print("=-=-=")

# programa de caixa eletrônico 
print("Bem-vindo ao caixa eletrônico!")
def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("valor sacado!")
        print("retire o seu dinheiro na boca do caixa.")
    
    print("obrigado por ser nosso cliente, tenha um bom dia!")

def depositar(valor):
    saldo = 500

    saldo += valor
sacar(1000)


                # estrutura condicionais

# programa de caixa eletronico 1
saldo = 2000
saque = float(input("Informe o valor do saque:"))

if saldo >= saque:
    print("Realizando saque!")

else:
    print("saldo insuficiente!")

# proograma de caixa eletrônico 2
print("Bem-vindo ao caixa eletrônico!")
print("Informe a opção desejada: ")
print("1- sacar")
print("2- extrato")
print("4- sair")

opcao = int(input("Informe uma opção: "))

valor = 500

if opcao == 1: 
    valor = float(input("Informe a quantia para o saque: "))

elif opcao == 2:
    print("Exibindo extrato...")   

else:
    print("Opção inválida, tente novamente!")

# programa de caixa eletrônico 3 

conta_facil = True
conta_salario = False
"""
#conta_facil = False
#conta_salario = True
#conta_facil = False
#conta_salario = False
"""

saldo = 2000
saque = 100
chaque_especial = 400

if conta_facil:
    if saldo >= saque:
        print("Saque realizado com sucesso")
    elif saque < (saldo + chaque_especial):
        print("Saque realizado com cheque especial")

elif conta_salario:
    if saldo >= saque:
        print("Saque CS realizado com sucesso")
    else:
        print("Saldo insuficiente, saque não realizado!")   
else:
    print("Conta não identificada, entre em contato com seu gerente!")


# programa de tira cnh 
maior_idade = 18
idoso = 60
idade_especial = 15 # adicionei essa linha

idade = int(input("Informe sua idade: "))

if idade >= maior_idade:
    print("Você pode tirar a CNH!")

elif idade == idade_especial:
    print("Você pode fazer aulas teóricas para a CNH, mas não pode tirar a CNH ainda!")

elif idade == idoso:
    print("Você pode tirar a CNH, mas com restrições devido à sua idade avançada!")

else:
    print("Você não pode tirar a CNH, ainda é menor de idade!") 


# estrutura ternaria, prorama de caixa eletrônico 4
saldo = 2000
saque = 1000

status = "Sucesso" if saldo >= saque else "Saldo insuficiente"
print(f"{status} ao realizar o saque!")


                # Estrutura de repetição    

# exemplo sem repetição 
a = int(input("informe um numero inteiro:"))
print(a)

if a == 2 :
    a += 1
print(a) 

# exemplo com for
texto = input("informe um texto: ")
vogais = "aeiou"

for letra in texto:
    if letra.upper() in vogais:
        print(letra, end="")
else:
    print()

# exemplo função range 

#range(stop) _> range object
list(range(4))
[0, 1, 2, 3]

#Utilizando range com for built-in  
for numero in range(0, 51 ,5):
    print(numero, end="") #o end deixa tudo na mesma linha


# exemplo com while, ate que a condição seja atendida
print("Bem-vindo ao caixa eletrônico!")
opcao = -1
while opcao != 0:
    opcao = int(input("[1]- sacar \n[2]- extrato \n[0]-saindo \n: "))

    if opcao == 1:
        print("Sacando ...")
    elif opcao == 2:
        print("Exibindo extrato ...")
print("Saindo ...")

# exemplo com while 2, usando o else
print("Bem-vindo ao caixa eletrônico!")
opcao = -1
while opcao != 0:
    opcao = int(input("[1]- sacar \n[2]- extrato \n[0]-saindo \n: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo extrato ...")
    else:
        print("obrigado por usar nosso sistema bancário, tenha um bom dia!")

    
# exemplo com while 4, usando break
print("Bem-vindo ao caixa eletrônico!")
opcao = -1    
while opcao !=0:
    opcao = int(input("infome um nunero: "))

    if opcao == 10:
        break

    print(opcao) 


# exemplo com while 5, usando break e True
while True:
    numero = int(input("informe um numero: "))
        
    if numero == 10:
        break
        
    print(numero)   


                    # classe string

# exemplo de string
nome = "vando"

print(nome.upper())
print(nome.lower())
print(nome.title())

# exemplo de string 2 eliminando espaços
texto = "   vando voce estuda python   "    
print(texto + ".")  # adiciona ponto final
print(texto.strip() + ".")  # remove espaços no início e no final
print(texto.lstrip() + ".")  # remove espaços no início
print(texto.rstrip() + ".")  # remove espaços no final

# exemplo de string 3, junções e centralização
curso = "Python"
print(curso.center(20, "*"))  # centraliza com asteriscos
print(curso.ljust(20, "*"))  # alinha à esquerda com asteriscos
print(curso.rjust(20, "*"))  # alinha à direita com asteriscos      
print(curso.center(20, "#"))  # centraliza com resteg
print(".".join(curso))  # junta os caracteres com ponto caractere especiais #@!%$
print(" ".join(curso))  # junta os caracteres com espaço


# exemplo de string 4, menu sem caracteres especiais
menu = "Eltec"
print(menu.center(14)) # centraliza o menu, mais sem o caractere especial
print(menu.ljust(14))  # alinha à esquerda
print(menu.rjust(14))  # alinha à direita       

for letra in menu:
    print(letra, end="-")  # imprime cada letra com traço entre elas 
print()  # pula linha após o loop   


#Interpolação com variaveis

""" Old style % """
nome = "Vando"
idade = 30     
profissao = "Programador"
linguagem = "Python"

print("Meu nome é %s, tenho %d anos, sou %s e " \
"programo em %s." % (nome, idade, profissao, linguagem))

""" New style {} """        
print("Meu nome é {}, tenho {} anos, sou {} e " \
"programo em {}.".format(nome, idade, profissao, linguagem))    

""" F-strings """
print(f"Meu nome é {nome}, tenho {idade} anos, sou {profissao} e  \
programo em {linguagem}.") 

# exemplo de string 5, de strings com f-strings
PI = 3.14159
print(f"Valor de PI: {PI:.2f}")  # formata PI com 2 casas decimais 2f
print(f"Valor de PI: {PI:5.2f}")  # formata PI com 2 casas decimais 2f e largura total de 5 caracteres

# exemplo de string 6, de strings com fateamento 
nome = "Vanderson"
idade = 30     
profissao = "Programador"
linguagem = "Python"

dados = {nome, idade} # fomra de ultiliza a lista com string

print("nome: %s idade: %s" % (nome, idade))# nao é mas ultilizado dessa forma 
print("nome: {} idade: {}".format(nome, idade))  # ultilizando o format
print(f"nome: {nome} idade: {idade}")  # ultilizando o f-string
print("nome: {nome} idade: {idade}".format(dados))#  ultiliza a lista com string

# exemplo de string 7, de strings com f-strings e fateamento    
nome = "Vanderson luiz"
print(nome[0])  # primeiro caractere 
print(nome[0:4])  # fatia do nome
print(nome[9:])
print(nome[12:])
print(nome[10:10])
print(nome[:])

# strings triplas ou de multiplaslinhas 

nome = "camila"

mensagem = f"""
Olá meu nome é {nome}, 
Eu estou aprendendo Python
"""
print(mensagem)

mensagem = f'''
    Olá meu nome é {nome}, 
Eu estou aprendendo Python
        E para conseguir uma vaga.
'''
print(mensagem)


"""
Operação de depósito
Deve ser possivel depositar valores positivos para 
minha conta bancaria. A v1 do projeto trabalha apenas
com 1 usuario, dessa forma não precisamos nos preocupar
em identificar qual é o número da agencia e conta bancaria .
Todos os depositos devem ser armazenados em uma variavel 
e exibidos na operação de extrato.
"""


"""
Operação de saque
O sistema deve permitir realizar 3 saques diarios com limite
maximo de R$ 500,00 por saque. Caso o usuario nao tenha saldo
em conta, o sistema deve exibir uma mensagem informando que 
não será possivel sacar o dinheiro por falta de
saldo. Todos os saques devem ser armazenados em 
uma variavel e exibidos na operação de extrato.
  limitie maximo = 1500,00

"""

"""
Opelração de extrato
Essa operação deve listar todos os depositos e saques
realizados na conta. no fim da listagem deve ser 
exibido o saldo atual da conta.

os valores deve ser exibidos utilizando o formato 
R$ xxx,xx
exemplo: 
1500.45 = R$ 1.500,45
"""

"""Projeto sistema bancario"""
menu = """
bem vindo ao sistema bancário!
[1] - depositar
[2] - sacar
[3] - extrato
[4] - sair  

=>"""
saldo = 0 
limite = 500
extrato = ""
numero_saque = 0
limite_saque = 3

while True:
    opcao = input()
    if opcao == 1:
        print("depositar")
    
    elif opcao == 2:
        print("sacar")
    
    elif opcao == 3:
        print("extrato")

    elif opcao == 4:
        break
    
    else:
        print("opção invalida, por favor selecione novamente a operação desejada.")
    

    