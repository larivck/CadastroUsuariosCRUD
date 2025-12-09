
import tkinter as tk
from tkinter import ttk, messagebox
from crud import criar_usuario, listar_usuarios, atualizar_usuario, excluir_usuario

class App:
    def __init__(self, root):
        self.root = root
        root.title("Sistema de Cadastro de Usuários")

        tk.Label(root, text="Nome").grid(row=0, column=0)
        self.nome = tk.Entry(root)
        self.nome.grid(row=0, column=1)

        tk.Label(root, text="Email").grid(row=1, column=0)
        self.email = tk.Entry(root)
        self.email.grid(row=1, column=1)

        tk.Label(root, text="Senha").grid(row=2, column=0)
        self.senha = tk.Entry(root, show="*")
        self.senha.grid(row=2, column=1)

        tk.Button(root, text="Cadastrar", command=self.cadastrar).grid(row=3, column=0, pady=5)

        self.tabela = ttk.Treeview(root, columns=("ID", "Nome", "Email"), show="headings")
        self.tabela.heading("ID", text="ID")
        self.tabela.heading("Nome", text="Nome")
        self.tabela.heading("Email", text="Email")
        self.tabela.grid(row=4, column=0, columnspan=3)

        tk.Button(root, text="Atualizar", command=self.atualizar).grid(row=5, column=0)
        tk.Button(root, text="Excluir", command=self.excluir).grid(row=5, column=1)
        tk.Button(root, text="Recarregar", command=self.carregar_tabela).grid(row=5, column=2)

        self.carregar_tabela()

    def carregar_tabela(self):
        for item in self.tabela.get_children():
            self.tabela.delete(item)
        for user in listar_usuarios():
            self.tabela.insert("", "end", values=user)

    def cadastrar(self):
        nome = self.nome.get()
        email = self.email.get()
        senha = self.senha.get()
        if nome == "" or email == "" or senha == "":
            messagebox.showwarning("Erro", "Preencha todos os campos!")
            return
        criar_usuario(nome, email, senha)
        messagebox.showinfo("Sucesso", "Usuário cadastrado!")
        self.carregar_tabela()

    def atualizar(self):
        item = self.tabela.focus()
        if not item:
            messagebox.showwarning("Erro", "Selecione um usuário!")
            return
        id_user = self.tabela.item(item)["values"][0]
        atualizar_usuario(id_user, self.nome.get(), self.email.get())
        messagebox.showinfo("Sucesso", "Usuário atualizado!")
        self.carregar_tabela()

    def excluir(self):
        item = self.tabela.focus()
        if not item:
            messagebox.showwarning("Erro", "Selecione um usuário!")
            return
        id_user = self.tabela.item(item)["values"][0]
        excluir_usuario(id_user)
        messagebox.showinfo("Sucesso", "Usuário excluído!")
        self.carregar_tabela()
