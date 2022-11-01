import folium
import pandas as pd

data = pd.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
long = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

html = """<h4>Volcano Information:</h4>
Name: %s <br>
Height: %s m
"""

map = folium.Map(location=[38,-115], zoom_start=5, tiles = "Stamen Terrain")
fg = folium.FeatureGroup(name="My Map")

for lt, ln, el, nm in zip(lat, long, elev, name):
    iframe = folium.IFrame(html=html % (nm, str(el)), width=200, height=100)
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(color='red')))

map.add_child(fg)

map.save("Map1.html")