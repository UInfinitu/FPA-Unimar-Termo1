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

@app.route('/mapa.html')
def cadastro():
    import folium
    import folium.plugins
    import geopandas as gpds
    import pandas as pds

    #Pegando a localização
    end = input("Endereço: ") # R. Manoel Santos Chieira, 92
    coord = gpds.tools.geocode(end, provider = "nominatim", user_agent = "myGeocode")["geometry"]  # só funciona na janela interativa
    string = str(coord[0])
    separacao = string.split()
    separacao.remove(separacao[0])
    lat = (separacao[1].replace(')',''))
    lon = (separacao[0].replace('(',''))
    print(lat, lon)

    #Configurações do mapa
    m = folium.Map(location=(-22.2127829,-49.9557924), zoom_start = 12, control_scale = True, )
    folium.plugins.Geocoder().add_to(m)
    folium.plugins.Fullscreen(position="topright", title="Expand me", title_cancel="Exit me", force_separate_button=True, ).add_to(m)

    # Marcador
    folium.Marker(location = [lat, lon]).add_to(m)

    # Rodando
    m
    return render_template("mapa.html")

#execução
if __name__ == "__main__":
    app.run(debug = True)