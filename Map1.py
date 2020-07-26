import folium
import pandas
data_Volcanoes = pandas.read_csv("Volcanoes_USA.txt")
lat_v = list(data_Volcanoes["LAT"])
long_v = list(data_Volcanoes["LON"])
elev = list(data_Volcanoes["ELEV"])
name = list(data_Volcanoes["NAME"])
data_city = pandas.read_csv("worldcities.csv")
# lat_c = list(data_city["lat"])
# long_c = list(data_city["lng"])


def colour(el):
    if el > 0 and el <= 1000:
        return "green"
    elif el > 1000 and el <= 3000:
        return "orange"
    else:
        return "red"


# 19.212768,72.839758
# tiles="Stamen Toner"
map = folium.Map(location=[38.58, -99.09], zoom_start=6)
fgv = folium.FeatureGroup(name="Volcanoes")
for lt, ln, el, nm in zip(lat_v, long_v, elev, name):
    # fg.add_child(folium.Marker(location=[lt,ln], popup=nm+","+str(el)+"m", icon=folium.Icon(color=colour(el))))  Marker
    fgv.add_child(folium.CircleMarker(location=[lt, ln], popup=nm + "," + str(
        el) + "m", radius=6, fill_opacity=0.7, color="grey", fill_color=colour(el)))
# for lt,ln in zip(lat_c,long_c):
#     fg.add_child(folium.Marker(location=[lt,ln], popup="Cities", icon = folium.Icon(color="green")))
fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read(),
                            style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
                                                      else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map1.html")
