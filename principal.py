# -*- coding: utf-8 -*-
import tkinter as tk
import usuario

def centralizar_janela(janela, largura, altura):
    janela.update_idletasks()
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    x = (largura_tela // 2) - (largura // 2)
    y = (altura_tela // 2) - (altura // 2)
    janela.geometry(f"{largura}x{altura}+{x}+{y}")

def abrir_formulario_cadastro_usuario(janela_principal):
    cadastro = tk.Toplevel(janela_principal)
    cadastro.title("Cadastrar Usuário")
    centralizar_janela(cadastro, 400, 300)
    cadastro.configure(bg="#f5f6fa")

    tk.Label(cadastro, text="Nome:", font=("Segoe UI", 12), bg="#f5f6fa").pack(pady=(20, 5))
    entry_nome = tk.Entry(cadastro, font=("Segoe UI", 12), width=30)
    entry_nome.pack()

    tk.Label(cadastro, text="E-mail:", font=("Segoe UI", 12), bg="#f5f6fa").pack(pady=(10, 5))
    entry_email = tk.Entry(cadastro, font=("Segoe UI", 12), width=30)
    entry_email.pack()

    tk.Label(cadastro, text="Senha:", font=("Segoe UI", 12), bg="#f5f6fa").pack(pady=(10, 5))
    entry_senha = tk.Entry(cadastro, font=("Segoe UI", 12), show="*", width=30)
    entry_senha.pack()

    def salvar_usuario():
        nome = entry_nome.get()
        email = entry_email.get()
        senha = entry_senha.get()
        if nome and email and senha:
            try:
                usuario.cadastrar_usuario(nome, email, senha)
                tk.messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
                cadastro.destroy()
            except Exception as e:
                tk.messagebox.showerror("Erro", f"Erro ao cadastrar usuário:\n{e}")
        else:
            tk.messagebox.showwarning("Atenção", "Preencha todos os campos.")

    btn_salvar = tk.Button(cadastro, text="Salvar", font=("Segoe UI", 12, "bold"),
                           bg="#273c75", fg="#fff", relief="flat", width=15,
                           command=salvar_usuario)
    btn_salvar.pack(pady=20)

def abrir_formulario_principal(janela_login):
    janela_principal = tk.Toplevel()
    janela_principal.title("Gerenciador de Tarefas")
    largura, altura = 600, 350
    centralizar_janela(janela_principal, largura, altura)
    janela_principal.configure(bg="#f5f6fa")

    label_bemvindo = tk.Label(
        janela_principal,
        text="Bem-vindo ao Gerenciador de Tarefas!",
        font=("Segoe UI", 22, "bold"),
        bg="#f5f6fa",
        fg="#273c75"
    )
    label_bemvindo.pack(pady=(30, 30))

    frame_botoes = tk.Frame(janela_principal, bg="#f5f6fa")
    frame_botoes.pack(expand=True)

    estilo_botao = {
        "font": ("Segoe UI", 14, "bold"),
        "bg": "#273c75",
        "fg": "#ffffff",
        "activebackground": "#40739e",
        "activeforeground": "#ffffff",
        "relief": "flat",
        "bd": 0,
        "width": 20,
        "height": 2,
        "cursor": "hand2"
    }

    def sair():
        janela_principal.destroy()
        janela_login.destroy()

    btn1 = tk.Button(frame_botoes, text="Cadastrar Usuários", **estilo_botao,
                     command=lambda: abrir_formulario_cadastro_usuario(janela_principal))
    btn2 = tk.Button(frame_botoes, text="Gerenciar Tarefas", **estilo_botao)
    btn3 = tk.Button(frame_botoes, text="Sair", **estilo_botao, command=sair)

    btn1.pack(pady=10)
    btn2.pack(pady=10)
    btn3.pack(pady=10)

    janela_login.withdraw()

    def ao_fechar():
        sair()
    janela_principal.protocol("WM_DELETE_WINDOW", ao_fechar)