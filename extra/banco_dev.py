import tkinter as tk
from tkinter import messagebox

# Iniciar o saldo
saldo = 1000

# Funções do banco
def sacar():
    global saldo
    try:
        valor = float(entrada_valor.get())
        if valor <= saldo:
            saldo_label.config(text=f"Saldo atual: R${saldo - valor:.2f}")
            messagebox.showinfo("Saque", f"Você sacou R${valor:.2f}")
            atualizar_saldo(-valor)
        else:
            messagebox.showwarning("Erro", "Saldo insuficiente.")
    except ValueError:
        messagebox.showerror("Erro", "Digite um valor válido.")

def depositar():
    global saldo
    try:
        valor = float(entrada_valor.get())
        atualizar_saldo(valor)
        messagebox.showinfo("Depósito", f"Você depositou R${valor:.2f}")
    except ValueError:
        messagebox.showerror("Erro", "Digite um valor válido.")

def atualizar_saldo(valor):
    global saldo
    saldo += valor
    saldo_label.config(text=f"Saldo atual: R${saldo:.2f}")
    entrada_valor.delete(0, tk.END)

# Criar janela principal
janela = tk.Tk()
janela.title("Banco Dev")
janela.configure(bg="white")
janela.geometry("350x300")

# Boas-vindas
titulo = tk.Label(janela, text="Bem-vindo ao Banco Dev!", fg="blue", bg="white", font=("Arial", 16, "bold"))
titulo.pack(pady=10)

# Saldo atual
saldo_label = tk.Label(janela, text=f"Saldo atual: R${saldo:.2f}", fg="blue", bg="white", font=("Arial", 12))
saldo_label.pack(pady=5)

# Entrada de valor
entrada_valor = tk.Entry(janela, width=20, font=("Arial", 12))
entrada_valor.pack(pady=10)

# Botões
botao_depositar = tk.Button(janela, text="Depositar", bg="blue", fg="white", font=("Arial", 12), command=depositar)
botao_depositar.pack(pady=5)

botao_sacar = tk.Button(janela, text="Sacar", bg="blue", fg="white", font=("Arial", 12), command=sacar)
botao_sacar.pack(pady=5)

# Mensagem de rodapé
rodape = tk.Label(janela, text="Obrigado por ser nosso cliente!", fg="blue", bg="white", font=("Arial", 10))
rodape.pack(side="bottom", pady=10)

# Iniciar interface
janela.mainloop()
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=

"""
 versão atualizada. 
"""
import tkinter as tk
from tkinter import messagebox

# =====================
# DADOS INICIAIS
# =====================
senha_correta = "1234"
saldo = 1000
historico = []

# =====================
# FUNÇÕES
# =====================
def verificar_login():
    if entrada_senha.get() == senha_correta:
        tela_login.destroy()
        abrir_interface_banco()
    else:
        messagebox.showerror("Erro", "Senha incorreta. Tente novamente.")

def sacar():
    global saldo
    try:
        valor = float(entrada_valor.get())
        if valor <= saldo:
            saldo -= valor
            atualizar_saldo()
            historico.append(f"Saque de R${valor:.2f}")
            messagebox.showinfo("Saque", f"Você sacou R${valor:.2f}")
        else:
            messagebox.showwarning("Erro", "Saldo insuficiente.")
    except ValueError:
        messagebox.showerror("Erro", "Digite um valor válido.")

def depositar():
    global saldo
    try:
        valor = float(entrada_valor.get())
        saldo += valor
        atualizar_saldo()
        historico.append(f"Depósito de R${valor:.2f}")
        messagebox.showinfo("Depósito", f"Você depositou R${valor:.2f}")
    except ValueError:
        messagebox.showerror("Erro", "Digite um valor válido.")

def atualizar_saldo():
    saldo_label.config(text=f"Saldo atual: R${saldo:.2f}")
    entrada_valor.delete(0, tk.END)

def mostrar_extrato():
    if historico:
        extrato_texto = "\n".join(historico)
    else:
        extrato_texto = "Nenhuma movimentação registrada."
    messagebox.showinfo("Extrato", extrato_texto)

# =====================
# TELA DE LOGIN
# =====================
tela_login = tk.Tk()
tela_login.title("Login - Banco Dev")
tela_login.configure(bg="white")
tela_login.geometry("300x200")

tk.Label(tela_login, text="Digite sua senha:", bg="white", fg="blue", font=("Arial", 12)).pack(pady=10)
entrada_senha = tk.Entry(tela_login, show="*", width=20, font=("Arial", 12))
entrada_senha.pack(pady=5)

tk.Button(tela_login, text="Entrar", bg="blue", fg="white", font=("Arial", 12), command=verificar_login).pack(pady=20)

# =====================
# TELA PRINCIPAL DO BANCO
# =====================
def abrir_interface_banco():
    janela = tk.Tk()
    janela.title("Banco Dev")
    janela.configure(bg="white")
    janela.geometry("400x350")

    tk.Label(janela, text="Bem-vindo ao Banco Dev!", fg="blue", bg="white", font=("Arial", 16, "bold")).pack(pady=10)

    global saldo_label
    saldo_label = tk.Label(janela, text=f"Saldo atual: R${saldo:.2f}", fg="blue", bg="white", font=("Arial", 12))
    saldo_label.pack(pady=5)

    global entrada_valor
    entrada_valor = tk.Entry(janela, width=20, font=("Arial", 12))
    entrada_valor.pack(pady=10)

    tk.Button(janela, text="Depositar", bg="blue", fg="white", font=("Arial", 12), command=depositar).pack(pady=5)
    tk.Button(janela, text="Sacar", bg="blue", fg="white", font=("Arial", 12), command=sacar).pack(pady=5)
    tk.Button(janela, text="Ver Extrato", bg="blue", fg="white", font=("Arial", 12), command=mostrar_extrato).pack(pady=5)

    tk.Label(janela, text="Obrigado por ser nosso cliente!", fg="blue", bg="white", font=("Arial", 10)).pack(side="bottom", pady=10)

    janela.mainloop()

tela_login.mainloop()


