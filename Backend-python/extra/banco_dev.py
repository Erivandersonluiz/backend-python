import tkinter as tk
from tkinter import messagebox

# Estado inicial
saldo = 0.0
limite_saque = 500.0
numero_saque = 0
limite_saque_diarios = 3
extrato = []

# Funções
def sacar():
    global saldo, numero_saque, extrato
    try:
        valor = float(entry_valor.get())
        if valor > saldo:
            messagebox.showwarning("Erro", "Saldo insuficiente.")
        elif valor > limite_saque:
            messagebox.showwarning("Erro", "O valor passou do limite de saque.")
        elif numero_saque >= limite_saque_diarios:
            messagebox.showwarning("Erro", "Limite de saques diários atingido.")
        else:
            saldo -= valor
            numero_saque += 1
            extrato.append(f"Saque: -R${valor:.2f}")
            messagebox.showinfo("Sucesso", "Saque realizado com sucesso.")
    except ValueError:
        messagebox.showerror("Erro", "Digite um valor válido.")

def depositar():
    global saldo, extrato
    try:
        valor = float(entry_valor.get())
        if valor < 0:
            messagebox.showwarning("Erro", "Valor negativo não é permitido.")
        else:
            saldo += valor
            extrato.append(f"Depósito: R${valor:.2f}")
            messagebox.showinfo("Sucesso", "Depósito realizado com sucesso.")
    except ValueError:
        messagebox.showerror("Erro", "Digite um valor válido.")

def ver_extrato():
    extrato_str = "\n".join(extrato) if extrato else "Nenhuma movimentação realizada."
    extrato_str += f"\n\nSaldo atual: R${saldo:.2f}"
    messagebox.showinfo("Extrato Bancário", extrato_str)

def sair():
    root.destroy()

# Janela principal
root = tk.Tk()
root.title("Banco Devpy")
root.geometry("400x400")
root.resizable(False, False)

# Header azul
header = tk.Frame(root, bg="blue", height=80)
header.pack(fill=tk.X)
titulo = tk.Label(header, text="Seja Bem-vindo ao Banco Devpy!", fg="white", bg="blue", font=("Helvetica", 14, "bold"))
titulo.pack(pady=20)

# Entrada de valor
label_valor = tk.Label(root, text="Valor (R$):")
label_valor.pack(pady=(20, 5))
entry_valor = tk.Entry(root, font=("Helvetica", 12))
entry_valor.pack(pady=5)

# Botões
btn_sacar = tk.Button(root, text="Sacar", command=sacar, width=20, bg="lightgray")
btn_sacar.pack(pady=10)

btn_depositar = tk.Button(root, text="Depositar", command=depositar, width=20, bg="lightgray")
btn_depositar.pack(pady=10)

btn_extrato = tk.Button(root, text="Ver Extrato", command=ver_extrato, width=20, bg="lightgray")
btn_extrato.pack(pady=10)

btn_sair = tk.Button(root, text="Sair", command=sair, width=20, bg="red", fg="white")
btn_sair.pack(pady=20)

# Loop principal
root.mainloop()
