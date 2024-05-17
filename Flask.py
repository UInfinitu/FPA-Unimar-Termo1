from flask import Flask

#iniciando
app = Flask(__name__)

#rotas
@app.route('/')
def login():
    return 

#execução
app.run(debug = True)