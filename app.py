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
    usuario_login = request.form.get("usuario")
    senha_login = request.form.get("senha")
    with open('usuarios.json', 'r') as usuarios:
        lista = json.load(usuarios)
        for c in lista:
            if usuario_login == c['nome'] and senha_login == c['senha']:
                return render_template("/report.html")
        else:
            flash('Usuário Inválido')
            return redirect("/login.html")
            
@app.route('/cadastro', methods = ["POST"])
def criaConta():
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")
    confSenha = request.form.get("confSenha")
    if senha == confSenha:
        with open('usuarios.json', 'r+') as f:
           data = json.load(f)
           data.append({"nome": usuario, "senha": senha})
           f.seek(0)
           json.dump(data, f, indent=4)
           f.truncate()
        return render_template("/report.html")
    else:
        return redirect("/cadastro.html")
#execução
if __name__ == "__main__":
    app.run(debug = True)