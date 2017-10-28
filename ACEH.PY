import folium

m = folium.Map(
  location=[4.695135,   96.749397],
  zoom_start=10,)

folium.Marker(
  location=[4.629343, 96.787586],
  popup='Kabupaten Aceh Tengah',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[4.377438, 97.161121],
  popup='Linge',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[5.403978, 94.8649394],
  popup='Kabupaten Aceh Besar',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[5.521737, 95.267446],
  popup='Peukan Bada',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[5.540874, 95.424001],
  popup='Kuta Baro',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[4.892097, 96.117719],
  popup='Kabupaten Pidie',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[4.662186, 97.414106],
  popup='Serba Jadi',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[5.078158, 95.908979],
  popup='Tangse',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[4.738831, 96.216596],
  popup='Sungai MAS',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[3.094788, 97.765668],
  popup='Hutan',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[4.7747372, 96.7121891],
  popup='Kab. Bener Meriah',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[4.7025774, 97.0787132],
  popup='Kab. Aceh Timur',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[4.993586, 96.8704841],
  popup='Kab. Aceh Utara',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[3.8354523, 96.5870526],
  popup='Kab. Aceh Barat Daya',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[3.0700274, 96.8644272],
  popup='Kab. Aceh selatan',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[3.3379887, 97.0568133],
  popup='Kab. Aceh Tenggara',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[4.2184441, 97.7212565],
  popup='Kab. Aceh Tamiang',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[3.9808591, 96.7630114],
  popup='Kab. Aceh GayoLues',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[4.788100, 96.381874],
  popup='Rusip Antara. Kabupaten Aceh Tengah',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[4.5092677,96.1253181,15],
  popup='Jl. Geumpang-Tutut',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[5.385298,95.2575132,14],
  popup='Jl. Banda aceh-Calang',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[5.5589877,95.3220353,15],
  popup='Tugu Simpang Lima Banda Aceh',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[5.535423,95.3905828,13],
  popup='Bandara Internasional Sultan Iskandar Muda',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[5.4710423,95.4069452,16],
  popup='PT.POS (Persero) Montasik',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[5.5484305,95.3153775,13],
  popup='Masjid Raya Baiturrahman',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[5.5484305,95.3153775,13]
  popup='Hall Stadion Harapan Bangsa Lhong Raya',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[5.5442072,95.5000587,12]
  popup='Pemandian Air Panas Aceh Besar',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[5.4887222,95.2206677],
  popup='Surf Cafe Lampuuk Beach',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[5.4887222,95.2206677],
  popup='Lampuuk Beach',
  icon=folium.Icon(icon='info-sign')
).add_to(m)

m.save('index.html')
