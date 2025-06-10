# -*- coding: utf-8 -*-
import pyodbc

# Altere conforme seu ambiente
CONN_STR = (
    "DRIVER={SQL Server};"
    "SERVER=localhost\\SQLEXPRESS;"
    "DATABASE=GerenciadorTarefas;"
    "Trusted_Connection=yes;"
)

def conectar():
    return pyodbc.connect(CONN_STR)

def cadastrar_usuario(nome, email, senha):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Usuarios (Nome, Email, Senha) VALUES (?, ?, ?)",
        (nome, email, senha)
    )
    conn.commit()
    cursor.close()
    conn.close()

def autenticar_usuario(nome, senha):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT UsuarioId, Nome FROM Usuarios WHERE Nome = ? AND Senha = ?",
        (nome, senha)
    )
    usuario = cursor.fetchone()
    cursor.close()
    conn.close()
    return usuario  # None se não encontrado, ou (UsuarioId, Nome)

def listar_usuarios():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT UsuarioId, Nome, Email FROM Usuarios")
    usuarios = cursor.fetchall()
    cursor.close()
    conn.close()
    return usuarios