
# Sistema de Cadastro de Usuários – CRUD em Python + SQLite

## 📌 Descrição
Este sistema permite cadastrar, listar, editar e excluir usuários utilizando Python, SQLite e Tkinter.
As senhas são criptografadas com Fernet.

## 🧩 Funcionalidades
✔ Cadastrar usuários  
✔ Listar usuários  
✔ Editar nome e email  
✔ Excluir usuários  
✔ Criptografia de senha  

## 🧱 Estrutura do Banco
Tabela: usuarios

| Campo | Tipo | Descrição |
|-------|------|-----------|
| id | INTEGER | ID |
| nome | TEXT | Nome |
| email | TEXT | Email único |
| senha | TEXT | Senha criptografada |

## ▶ Como executar
1. Instale as dependências:
```
pip install -r requirements.txt
```

2. Gere a key:
```
from cryptography.fernet import Fernet
key = Fernet.generate_key()
open("key.key", "wb").write(key)
```

3. Rode o sistema:
```
python main.py
```

## Tecnologias
- Python
- SQLite
- Tkinter
- Cryptography
```

## Membros da Dupla
```
- Victoria Larissa
- Mariah Aparecida
