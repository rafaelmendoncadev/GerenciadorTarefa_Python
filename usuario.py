import sqlite3

def conectar():
    return sqlite3.connect("banco_tarefas.db")

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL UNIQUE,
            email TEXT,
            senha TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def cadastrar_usuario(nome, email, senha):import sqlite3

def conectar():
    return sqlite3.connect("banco_tarefas.db")

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL UNIQUE,
            email TEXT,
            senha TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def cadastrar_usuario(nome, email, senha):
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)",
            (nome, email, senha)
        )
        conn.commit()
        sucesso = True
    except sqlite3.IntegrityError:
        sucesso = False
    conn.close()
    return sucesso

def autenticar_usuario(nome, senha):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, nome FROM usuarios WHERE nome = ? AND senha = ?",
        (nome, senha)
    )
    usuario = cursor.fetchone()
    conn.close()
    return usuario  # None se não encontrado, ou (id, nome)

def listar_usuarios():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, email FROM usuarios")
    usuarios = cursor.fetchall()
    conn.close()
    return usuarios

# Garante que a tabela exista ao importar o módulo
criar_tabela()
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)",
            (nome, email, senha)
        )
        conn.commit()
        sucesso = True
    except sqlite3.IntegrityError:
        sucesso = False
    conn.close()
    return sucesso

def autenticar_usuario(nome, senha):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, nome FROM usuarios WHERE nome = ? AND senha = ?",
        (nome, senha)
    )
    usuario = cursor.fetchone()
    conn.close()
    return usuario  # None se não encontrado, ou (id, nome)

def listar_usuarios():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, email FROM usuarios")
    usuarios = cursor.fetchall()
    conn.close()
    return usuarios

# Garante que a tabela exista ao importar o módulo
criar_tabela()