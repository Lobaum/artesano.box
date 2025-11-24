<p align="center">
  
  <!-- Linguagens -->
  <img src="https://img.shields.io/github/languages/top/Lobaum/artesano.box?logo=python&logoColor=white&label=Linguagem%20Principal" />

  <!-- Python -->
  <img src="https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white" />

  <!-- Flask -->
  <img src="https://img.shields.io/badge/Flask-Framework-black?logo=flask&logoColor=white" />

  <!-- MySQL -->
  <img src="https://img.shields.io/badge/MySQL-Database-005C84?logo=mysql&logoColor=white" />

  <!-- TailwindCSS -->
  <img src="https://img.shields.io/badge/TailwindCSS-Framework-06B6D4?logo=tailwindcss&logoColor=white" />

  <!-- Status do projeto -->
  <img src="https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow" />

  <!-- Último commit -->
  <img src="https://img.shields.io/github/last-commit/Lobaum/artesano.box?color=blue" />

  <!-- Tamanho do repositório -->
  <img src="https://img.shields.io/github/repo-size/Lobaum/artesano.box?color=green" />

</p>

# 🎨 Artesano.Box — Plataforma Acadêmica de E-commerce Artesanal

Este projeto foi desenvolvido como parte de um **trabalho acadêmico da faculdade**, com o objetivo de criar um ambiente simples e funcional que simula um e-commerce voltado para artesanatos.

O foco é demonstrar:
- Integração entre **Frontend + Backend + Banco de Dados**
- Organização de projeto real
- Boas práticas com Flask e Python
- Uso profissional de templates e estilização moderna

---

## 🚀 Tecnologias Utilizadas

### 🖥️ **Frontend**
- **HTML5**
- **CSS3**
- **TailwindCSS** (CDN)
- **Google Fonts**
- Design responsivo e foco em UI/UX

### 🧠 **Backend**
- **Python 3**
- **Flask**
- **Flask-Bcrypt** → criptografia de senhas
- Rotas organizadas e templates dinâmicos (`render_template`)

### 🗄️ **Banco de Dados**
- **MySQL**
- Integração via **mysql-connector-python**
- Validação de login e cadastro

---

## 📌 Funcionalidades Implementadas

- 🔐 **Cadastro de Usuário**
- 🔑 **Login com verificação e hash seguro**
- 🚪 **Logout e controle de sessão**
- 🏠 **Página inicial com botões funcionais**
- 💾 **Gravação de dados no banco MySQL**
- 🧩 Arquitetura organizada usando templates Flask

---

## 🗂️ Estrutura do Projeto

```
/e-commerce
│── app.py
│── README.md
│── /templates
│ ├── index.html
│ ├── login.html
│ └── cadastro.html
│── /static
│ └── /assets
│ └── logo.png
```

## ⚙️ Como Executar

### 📦 1. Instalar dependências

```bash
   pip install -r requirements.txt
   ```
### 🗄️ 3. Configurar o MySQL

- Criar a base e tabela:

```bash
CREATE DATABASE artesano;
USE artesano;

CREATE TABLE usuarios (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(120),
  email VARCHAR(120) UNIQUE,
  senha VARCHAR(255),
);
   ```

### ▶️ 4. Rodar o servidor
   ```bash
   python app.py
   ```

### 🌐 5. Acessar no navegador
   - Página Inicial: http://localhost:5000/
   - Cadastro: http://localhost:5000/cadastro
   - Login: http://localhost:5000/login

## 🎓 Sobre o Projeto

Este projeto não visa fins comerciais.
Foi criado apenas como atividade acadêmica para demonstrar e aprimorar conhecimento sobre:

- Construção de rotas em Flask

- Integração com MySQL

- UI moderna usando Tailwind

- Segurança básica de autenticação

## 🤝 Autor
#### *Pedro Henrique Nascimento da Silva*

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
