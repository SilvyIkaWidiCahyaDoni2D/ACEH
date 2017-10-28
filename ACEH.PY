import folium

m = folium.Map(location=[4.695135,   96.749397],zoom_start=10,)
folium.Marker(location=[4.629343, 96.787586],popup='Kabupaten Aceh Tengah',icon=folium.Icon(icon='info-sign')).add_to(m)
folium.Marker(location=[4.377438, 97.161121],popup='Linge',icon=folium.Icon(icon='info-sign')).add_to(m)
folium.Marker(location=[5.291523, 95.535145],popup='Kabupaten Aceh Besar',icon=folium.Icon(icon='info-sign')).add_to(m)
folium.Marker(location=[5.521737, 95.267446],popup='Peukan Bada',icon=folium.Icon(icon='info-sign')).add_to(m)
folium.Marker(location=[5.540874, 95.424001],popup='Kuta Baro',icon=folium.Icon(icon='info-sign')).add_to(m)
folium.Marker(location=[4.892097, 96.117719],popup='Kabupaten Pidie',icon=folium.Icon(icon='info-sign')).add_to(m)
folium.Marker(location=[4.662186, 97.414106],popup='Serba Jadi',icon=folium.Icon(icon='info-sign')).add_to(m)
folium.Marker(location=[5.078158, 95.908979],popup='Tangse',icon=folium.Icon(icon='info-sign')).add_to(m)
folium.Marker(location=[4.738831, 96.216596],popup='Sungai MAS',icon=folium.Icon(icon='info-sign')).add_to(m)
folium.Marker(location=[3.094788, 97.765668],popup='Hutan',icon=folium.Icon(icon='info-sign')).add_to(m)
