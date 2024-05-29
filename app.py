from flask import Flask, render_template, redirect, request, flash
import json

#iniciando
app = Flask(__name__)
app.config['SECRET_KEY'] = "batatamuitofrita"

#rotas
@app.route('/', methods = ["POST", "GET"])
def login():
    return render_template("login.html")

@app.route('/login.html')
def login_():
    return render_template("login.html") 

@app.route('/cadastro.html')
def cadastro():
    return render_template("cadastro.html") 

@app.route('/report.html')
def report():
    return render_template("report.html")

@app.route('/report', methods = ["POST"])
def verificaLogin():
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")
    with open('usuarios.json') as usuarios:
        lista = json.load(usuarios)
        cont = 0
        for c in lista:
            cont += 1
            if usuario == c['nome'] and senha == c['senha']:
                return render_template("/report.html")
            else:
                flash('Usuário Inválido')
                return redirect("/login.html")
            
#execução
if __name__ == "__main__":
    app.run(debug = True)