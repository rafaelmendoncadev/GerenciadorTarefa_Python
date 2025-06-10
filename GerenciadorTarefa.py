# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import messagebox
from principal import abrir_formulario_principal, centralizar_janela  # Importa a função do outro arquivo
import usuario  # Importa o módulo de acesso ao banco

# Função para autenticar usuário
def autenticar():
    nome = entry_usuario.get()
    senha = entry_senha.get()
    usuario_autenticado = usuario.autenticar_usuario(nome, senha)
    if usuario_autenticado:
        abrir_formulario_principal(janela_login)  # Passa a janela de login
    else:
        messagebox.showerror("Erro de Login", "Usuário ou senha inválidos.")

# Tela de Login
janela_login = tk.Tk()
janela_login.title("Login - Gerenciador de Tarefas")
centralizar_janela(janela_login, 350, 400)
janela_login.configure(bg="#f5f6fa")
janela_login.resizable(False, False)

frame = tk.Frame(janela_login, bg="#ffffff", bd=2, relief="groove")
frame.place(relx=0.5, rely=0.5, anchor="center", width=300, height=320)

label_titulo = tk.Label(frame, text="Login", font=("Segoe UI", 18, "bold"), bg="#ffffff", fg="#273c75")
label_titulo.pack(pady=(30, 20))

label_usuario = tk.Label(frame, text="Usuário", font=("Segoe UI", 10), bg="#ffffff", anchor="w")
label_usuario.pack(fill="x", padx=30)
entry_usuario = tk.Entry(frame, font=("Segoe UI", 10), bg="#f1f2f6", relief="flat")
entry_usuario.pack(fill="x", padx=30, pady=(0, 15))

label_senha = tk.Label(frame, text="Senha", font=("Segoe UI", 10), bg="#ffffff", anchor="w")
label_senha.pack(fill="x", padx=30)
entry_senha = tk.Entry(frame, font=("Segoe UI", 10), bg="#f1f2f6", relief="flat", show="*")
entry_senha.pack(fill="x", padx=30, pady=(0, 25))

btn_login = tk.Button(frame, text="Entrar", font=("Segoe UI", 11, "bold"), bg="#273c75", fg="#ffffff",
                      activebackground="#40739e", activeforeground="#ffffff", relief="flat", command=autenticar)
btn_login.pack(fill="x", padx=30, pady=(0, 15))

janela_login.mainloop()
