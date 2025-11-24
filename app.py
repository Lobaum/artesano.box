from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_bcrypt import Bcrypt
import mysql.connector
from mysql.connector import Error

app = Flask(__name__, template_folder="templates", static_folder="static")

app.secret_key = "anoesdejardimcostumammudar"

bcrypt = Bcrypt(app)

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "root",
    "database": "artesano",
}

def get_db():
    return mysql.connector.connect(**DB_CONFIG)


@app.route("/")
def index():
    usuario = None
    if "usuario_id" in session:
        usuario = {
            "id": session["usuario_id"],
            "nome": session["usuario_nome"]
        }
    return render_template("index.html", usuario=usuario)


@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        email = request.form.get("email", "").lower().strip()
        senha = request.form.get("senha", "")
        confirmar = request.form.get("confirmarsenha", "")
        tipo = request.form.get("tipodeconta", "cliente")
        if not nome or not email or not senha or not confirmar:
            flash("Preencha todos os campos.", "error")
            return redirect(url_for("cadastro"))
        if senha != confirmar:
            flash("As senhas não conferem.", "error")
            return redirect(url_for("cadastro"))
        senha_hash = bcrypt.generate_password_hash(senha).decode("utf-8")
        try:
            db = get_db()
            cursor = db.cursor()
            cursor.execute("SELECT id FROM usuarios WHERE email = %s", (email,))
            if cursor.fetchone():
                flash("E-mail já cadastrado.", "error")
                return redirect(url_for("cadastro"))
            cursor.execute(
                "INSERT INTO usuarios (nome, email, senha, tipo_conta) VALUES (%s, %s, %s, %s)",
                (nome, email, senha_hash, tipo)
            )
            db.commit()
            flash("Conta criada com sucesso. Faça login!", "success")
            return redirect(url_for("login"))
        except Error as e:
            print("Erro no MySQL:", e)
            flash("Erro no servidor. Tente novamente.", "error")
            return redirect(url_for("cadastro"))
    return render_template("cadastro.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        login_field = request.form.get("email_or_user", "").strip()
        senha = request.form.get("senha", "")

        if not login_field or not senha:
            flash("Preencha e-mail/usuário e senha.", "error")
            return redirect(url_for("login"))

        try:
            conn = get_db()
            cursor = conn.cursor(dictionary=True)

            cursor.execute("SELECT * FROM usuarios WHERE email = %s", (login_field.lower(),))
            usuario = cursor.fetchone()

            if not usuario:
                cursor.execute("SELECT * FROM usuarios WHERE nome = %s", (login_field,))
                usuario = cursor.fetchone()

            cursor.close()
            conn.close()

            if usuario and bcrypt.check_password_hash(usuario["senha"], senha):
                session["usuario_id"] = usuario["id"]
                session["usuario_nome"] = usuario["nome"]
                session["usuario_tipo"] = usuario["tipo_conta"]

                flash(f"Bem vindo, {usuario['nome']}!", "success")

                if usuario["tipo_conta"] == "cliente":
                    return redirect("/catalogo")
                
                if usuario["tipo_conta"] == "artesao":
                    return redirect("/dashboard")

                return redirect(url_for("index"))

            flash("E-mail/usuário ou senha incorretos.", "error")
            return redirect(url_for("login"))

        except Error as e:
            print("Erro DB:", e)
            flash("Erro no servidor. Tente novamente mais tarde.", "error")
            return redirect(url_for("login"))

    return render_template("login.html")

@app.route("/catalogo")
def catalogo():
    return "Página de catálogo (cliente)."

@app.route("/dashboard")
def dashboard():
    return "Dashboard do artesão."




@app.route("/logout")
def logout():
    session.clear()
    flash("Você saiu da sua conta.", "info")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)