import folium as fo #pip install folium

map=fo.Map()

x=fo.FeatureGroup(name="My Map")

x.add_child(fo.Marker(location=[8.407449,77.709568],popup='My point',icon=fo.Icon(color='Black')))

map.add_child(x)