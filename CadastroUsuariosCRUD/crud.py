
import sqlite3
from cryptography.fernet import Fernet
from database import conectar

with open("key.key", "rb") as file:
    key = file.read()

fernet = Fernet(key)

def criar_usuario(nome, email, senha):
    conn = conectar()
    cursor = conn.cursor()
    senha_cripto = fernet.encrypt(senha.encode()).decode()
    cursor.execute(
        "INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)",
        (nome, email, senha_cripto)
    )
    conn.commit()
    conn.close()

def listar_usuarios():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, email FROM usuarios")
    dados = cursor.fetchall()
    conn.close()
    return dados

def atualizar_usuario(id_user, nome, email):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE usuarios SET nome = ?, email = ? WHERE id = ?",
        (nome, email, id_user)
    )
    conn.commit()
    conn.close()

def excluir_usuario(id_user):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM usuarios WHERE id = ?", (id_user,))
    conn.commit()
    conn.close()
