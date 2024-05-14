# downloads
# pip install folium
# 
#


import folium
import folium.plugins
import geopandas as gpds
import pandas as pds


# transformando a localização
end = input("Endereço: ") # R. Manoel Santos Chieira, 92
coord = gpds.tools.geocode(end, provider = "nominatim", user_agent = "myGeocode")["geometry"]  # só funciona na janela interativa
lista = []
lista = str(coord).split(" ")
lista

## configurações do mapa
##lat, lon = input('Digite a localização: ').split(',')
#m = folium.Map(location=(-22.2127829,-49.9557924), zoom_start = 12, control_scale = True, )
#folium.plugins.Geocoder().add_to(m)
#folium.plugins.Fullscreen(position="topright", title="Expand me", title_cancel="Exit me", force_separate_button=True, ).add_to(m)
#
## marcadores
#folium.Marker(location = [coord], tooltip = 'RyuLol', popup="Que cara foda", icon=folium.Icon(color=""), ).add_to(m)
#
## start
#m
