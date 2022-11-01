import folium
import pandas
 
data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

def color_chooser(elevation):
    if elevation < 1500:
        return 'green'
    elif 1500 <= elevation < 3500:
        return 'orange'
    else: 
        return 'red'
 
html = """
Volcano name:
<a href="https://www.google.com/search?q=%%22%s Volcano%%22" target="_blank">%s </a><br>
Height: %s m
"""
 
map = folium.Map(location=[38.58, -99.09], zoom_start=5, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name = "My Map")
 
for lt, ln, el, name in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (name, name, el), width=250, height=75)
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius=5, popup=folium.Popup(iframe), 
    tooltip=el, color = color_chooser(el), fill=True, fill_color=color_chooser(el), fill_opacity=0.5))
#    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon = folium.Icon(color = color_chooser(el))))
 
map.add_child(fg)
map.save("Map2_html_Colors.html")