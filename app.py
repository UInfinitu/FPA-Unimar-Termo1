#Downloads

# pip install folium
# pip install geopandas 
# pip install pandas
# pip install geopy
# pip install Flask
# pip install pyscript
# pip install pyinstaller

from flask import Flask, render_template, redirect, request, flash, url_for
import json

#iniciando
app = Flask(__name__)
app.config['SECRET_KEY'] = "batatamuitofrita"

#rotas
@app.route('/', methods = ["POST", "GET"])
def login():
    return render_template("login.html")

@app.route('/mapa.html')
def main():
    return render_template("mapa.html")

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
                return redirect(url_for("report"))
        else:
            flash("Usuário Inválido")
            return redirect(url_for("login"))
            
@app.route('/cadastro', methods = ["POST"])
def criaConta():
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")
    confSenha = request.form.get("confSenha")
    if senha == confSenha:
        with open('usuarios.json', 'r+') as f:
            data = json.load(f)
            for c in data:
                if usuario == c['nome']:
                    flash("Nome de usuário já existe!")
                    return redirect(url_for("cadastro"))
            data.append({"nome": usuario, "senha": senha})
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
        return redirect(url_for("report"))
    else:
        flash("Senha e confirmação diferentes!")
        return redirect(url_for("cadastro"))

@app.route('/toMap', methods = ["POST"])
def mapa():
    import folium
    import folium.plugins
    import geopandas as gpds
    import pandas as pds

    #Pegando a localização
    end = request.form.get("end") # R. Manoel Santos Chieira, 92
    corPin = request.form["situacao"]
    coord = gpds.tools.geocode(end, provider = "nominatim", user_agent = "myGeocode")["geometry"]  # só funciona na janela interativa
    string = str(coord[0])
    separacao = string.split()
    separacao.remove(separacao[0])
    lat = (separacao[1].replace(')',''))
    lon = (separacao[0].replace('(',''))
    
    with open('localiza.json', 'r+') as f:
       data = json.load(f)
       data.append({"lat": lat, "lon": lon, "sit": corPin})
       f.seek(0)
       json.dump(data, f, indent=4)
       f.truncate()

    #Configurações do mapa
    m = folium.Map(location=(-22.2127829,-49.9557924), zoom_start = 12, control_scale = True, )
    folium.plugins.Geocoder().add_to(m)
    folium.plugins.Fullscreen(position="topright", title="Expand me", title_cancel="Exit me", force_separate_button=True, ).add_to(m)

    # Marcador
    with open('localiza.json', 'r') as localiza:
        lista = json.load(localiza)

    for c in lista:
        corPin = c["sit"]
        if corPin == "bur":
            folium.Marker(location = [c['lat'], c['lon']], icon=folium.Icon(color='red')).add_to(m)
        elif corPin == "sem":
            folium.Marker(location = [c['lat'], c['lon']], icon=folium.Icon(color='blue')).add_to(m)
        elif corPin == "vaz":
            folium.Marker(location = [c['lat'], c['lon']], icon=folium.Icon(color='green')).add_to(m)
        else:
            folium.Marker(location = [c['lat'], c['lon']], icon=folium.Icon(color='black')).add_to(m)

    # Legenda
    legend_html = '''
     <div style="position: fixed; 
     bottom: 5px; left: 5px; width: 200px; height: 200px; 
     border: 2px solid grey; z-index: 9999; font-size: 18px;
     background-color: white; text-align: center; padding: 10px;
     border-radius: 6px;
     ">&nbsp; <b style="font-size: 22px">Legenda</b> <br>
     &nbsp; Buraco &nbsp; <i class="fa fa-map-marker fa-2x" style="color:#d53e2a"></i><br>
     &nbsp; Semáforo &nbsp; <i class="fa fa-map-marker fa-2x" style="color:#36a3d3"></i><br>
     &nbsp; Vazamento &nbsp; <i class="fa fa-map-marker fa-2x" style="color:#6eaa25"></i><br>
     &nbsp; Obstrução &nbsp; <i class="fa fa-map-marker fa-2x" style="color:#2e2e2e"></i><br>
      </div>
     '''
    m.get_root().html.add_child(folium.Element(legend_html))
    
    # Rodando
    m.save("templates/mapa.html")
    return redirect(url_for("main"))

#execução
if __name__ == "__main__":
    app.run(debug = True)