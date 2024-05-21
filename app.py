from flask import Flask, render_template

#iniciando
app = Flask(__name__)

#rotas
@app.route('/')
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

#execução
if __name__ == "__main__":
    app.run(debug = True)