from flask import Flask, render_template

#iniciando
app = Flask(__name__)

#rotas
@app.route('/')
def login():
    return render_template("login.html") 

#execução
if __name__ == "__main__":
    app.run(debug = True)