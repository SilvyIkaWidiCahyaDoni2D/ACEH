#!/bin/python

import folium
def  inisiasi ( panjang , lat ):
	m = folium.Map (
    lokasi = [ panjang , lat],
    zoom_start = 12 ,
    ubin = ' medan stamen ' )
	kembali m
	
def  hitam ( panjang , lat ):
	c = folium.Map (
    lokasi = [ panjang , lat],
    zoom_start = 12 ,
    tile = ' Stamen Toner ' )	
	kembali c

def  masukkin ( apa , ini ):
	d = folium.Map (
	lokasi = [apa, ini],
	zoom_start = 12 ,
    ubin = ' medan stamen ' )	
	kembali d
	
def  simpan ( anu , gede ):
	anu.save (gede)

d = masukkin ( - 6.966667 , 110.416667 )
c = hitam ( - 6.966667 , 110.416667 )
m = inisiasi ( - 6.966667 , 110.416667 )
tooltip =  ' klik saya! '



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
  location=[5.6279369,95.1505769,10],
  popup='Suka Makmur',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[5.5442072,95.5000587,12],
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
folium.Marker(
  location=[5.868271, 95.332800],
  popup='Sabang',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[5.901489, 95.220230],
  popup='Iboih',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[5.906413, 95.218188],
  popup='Unnamed Road',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[5.882337, 95.257476],
  popup='Pulau Rubiah',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[5.895571, 95.253356],
  popup='Pulau Seulako',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[5.846136, 95.275071],
  popup='Batee Shoek',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[5.824106, 95.279019],
  popup='Paya',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[5.879597, 95.340429],
  popup='Ujong Kareung',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[5.850618, 95.345770],
  popup='Cot Abeuk',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[5.862454, 95.340713],
  popup='Pulau We',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[4.021332, 96.827483],
  popup='Persada Tongra Terangun, Kabupaten Gayo Lues',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[4.508936, 96.126242],
  popup='Geudong',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[4.490047, 96.205635],
  popup='Panton Reu',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[4.501000, 96.029854],
  popup='Woyla Tim.',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[4.862339, 95.810127],
  popup='Krueng Sabee',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[4.873285, 95.705757],
  popup='Gampong Baroh',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[4.993687, 95.623360],
  popup='Sampoiniet',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[4.692642, 95.760689],
  popup='Panga',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[4.829497, 96.024361],
  popup='Mane',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[4.424329, 96.392403],
  popup='Pantai Ceuremen',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[4.254529, 96.293526],
  popup='Seunagan',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[4.5065868, 97.9302927],
  popup='Langsa, Kota Langsa',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[5.1720572, 97.0375946],
  popup='	Kota Lhokseumawe',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[5.9670211, 5.0957705],
  popup='Kota Sabang',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[2.7578791, 97.6614605],
  popup='Kota Subulussalam',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[4.4520047, 95.9055919],
  popup='Kabupaten Aceh Barat',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[4.6338398, 95.5730575],
  popup='Calang, Bahagia, Kabupaten Aceh Jaya',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[5.186493,95.5404471],
  popup='Kota Jantho',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[4.3313354, 97.9990071],
  popup='Karang Baru',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[4.086729, 96.672382],
  popup='Krueng Alem',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[4.145971, 96.432056],
  popup='Alue Sepeng',
  icon=folium.Icon(icon='info-sign')
 ).add_to(m)
folium.Marker(
  location=[5.357149, 95.283201],
  popup='Leupung',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[4.090838, 96.410083],
  popup='Gunong Geulugo',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[4.119261, 96.472568],
  popup='Babah Rot',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[4.136040, 96.568012],
  popup='Blang Luah',
  icon=folium.Icon(icon='info-sign')
 ).add_to(m)
folium.Marker(
  location=[5.187582, 96.645506],
  popup='Kabupaten Bireun',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[5.154757, 96.293944],
  popup='Kabupaten Pidie Jaya',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[4.508871, 95.777586],
  popup='Teunom',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[3.989141, 96.512983],
  popup='Tuwi Buya',
  icon=folium.Icon(icon='info-sign')
 ).add_to(m)
folium.Marker(
  location=[2.572206, 96.225522],
  popup='Air Pinang',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[2.592098, 96.135572],
  popup='Luan Balu',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[2.599644, 96.112226],
  popup='Sambai',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[2.634626, 96.087507],
  popup='Kuala Bakti',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[2.426089, 96.495374],
  popup='Labuhan Bakti',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[2.455588, 96.451429],
  popup='Lataling',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[2.446670, 96.323026],
  popup='Batu Batu',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[2.479599, 96.247495],
  popup='Salur Latun',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[2.546139, 96.246808],
  popup='Air Pinang',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[2.549569, 96.316846],
  popup='Ganting',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[5.5314922,95.385386,13],
  popup='Universitas Abulyatama',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[5.5521747,95.372461,13],
    popup='Stmik Abulyatama',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[5.5531961,95.3173653],
    popup='Akademi Perikanan Dan Ilmu Kelautan',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[5.5531961,95.3173653],
    popup='Akademi Kebidanan Saleha',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[5.5531961,95.3173653],
    popup='Universitas Serambi Mekkah',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[5.5531961,95.3173653],
    popup='Toko Buku NEW ZIKRA',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[5.5528544,95.3034607,13],
    popup='Badan Pemberdayaan Masyarakat',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[5.5614688,95.327047,16],
    popup='88 hotel atjeh',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[5.5613162,95.3300383,17],
    popup='SMAN 3 Banda Aceh',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[5.5613162,95.3300383,17],
    popup='MTsN Model Banda Aceh',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[4.560078, 96.790258],
    popup='Pegasing',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[4.524262, 95.784252],
    popup='Tuwi Kareung Panga',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[4.638098, 97.020142],
    popup='Hutan Syiah Utama Sel.',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[4.159119, 96.142497],
    popup='Meulaboh',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[4.029476, 97.772076],
    popup='Pertik',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[5.050723, 95.635235],
    popup='Blang Luah',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[4.020514, 97.013798],
    popup='Bukut',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[5.400694, 95.962064],
    popup='Selat Malaka',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[5.408190, 95.294083],
    popup='Leupung',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[5.242617, 95.557376],
    popup='Kota Jantho',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[2.205858, 97.244300],
    popup='Pulau Tuangku',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[2.204485, 97.177009],
    popup='Asantola',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[2.091717, 97.338180],
    popup='Haloban',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[2.349702, 97.398605],
    popup='Pulau Banyak',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[2.179547, 97.431564],
    popup='Pulau Baguk',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[2.072504, 97.101974],
    popup='Pulau Bangkaru',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[2.168568, 96.621322],
    popup='Pulau Lasia',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[2.391265, 96.423824],
    popup='Kebun Baru',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[2.365195, 96.400478],
    popup='Batu Ralang',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[2.494619, 96.258466],
    popup='Salur Latun',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[2.511082, 96.204049],
    popup='Naibos',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[4.457239,97.9676183,15],
  popup='IAIN Langsa',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[4.457239,97.9676183,15],
  popup='Universitas Samudra',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[4.4683234,97.9678442,16],
  popup='RSUD Langsa',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[4.4713258,97.9664169,17],
  popup='Taman Bambu Runcing',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[4.4713258,97.9664169,17],
  popup='Ibams Coffee',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[4.4713258,97.9664169,17],
  popup='Stasiun Kupi',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[4.4711097,97.9680125,17],
  popup='Bank Mandiri Langsa',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[4.469669,97.9722034,17],
  popup='Fish Market Kota Langsa',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[4.6516293,96.8304486,18],
  popup='Apotek Kaisara',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[4.649122,96.8329087,18],
  popup='Waroeng Bebek Ijo Binjai',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[4.1583434,96.1110499],
  popup='Meulaboh, Kabupaten Aceh Barat',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[4.6309604,96.8290581],
  popup='Takengon',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[4.7509349,96.7578312],
  popup='Lampahan, Mude Benara, Kabupaten Bener Meriah, Aceh',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[4.7139139,96.8563036],
  popup='Tingkem Benyer, Kabupaten Bener Meriah, Aceh',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[4.7399133,96.7874634],
  popup='Simpang Balek, Kabupaten Bener Meriah, Aceh',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[4.6357725,96.8403251],
  popup='Simpang Empat, Kabupaten Aceh Tengah, Aceh',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[4.7346177,96.7931669],
  popup='Pante Raya, Kabupaten Bener Meriah, Aceh',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[5.0642054,96.7482257],
  popup='Sawang, Kabupaten Aceh Utara, Aceh',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[5.1951285,97.0098696],
  popup='Jalan Elak, Kabupaten Aceh Utara, Aceh',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[5.2162534,97.0182723],
  popup='Paloh Gadeng, Kabupaten Aceh Utara, Aceh',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[5.1738861,96.9756457],
  popup='Nisam, Kabupaten Aceh Utara, Aceh',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[5.18403,96.9392327],
  popup='Banda Baro, Kabupaten Aceh Utara, Aceh',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[5.098764, 96.353761],
  popup='Bandar Dua',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[5.232972, 95.602515],
  popup='Jantho',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[4.900749, 95.588472],
  popup='Krueng Tho',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[4.760816, 95.497191],
  popup='Sawang',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[5.414747, 95.911466],
  popup='Batee',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[5.173534, 96.483728],
  popup='Pandrah',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[4.423289, 97.824776],
  popup='Jambur Labu',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[4.280607, 96.409161],
  popup='Beutong',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[3.138267, 97.395492],
  popup='Kluet Utara',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[3.077031, 98.003644],
  popup='Mangan Molih',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[2.907538, 97.880288],
  popup='Trumon Tim.',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[3.092676, 97.832000],
  popup='Kec. Babul Rahman',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[2.320018, 97.401256],
  popup='Samudra Hindia',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[2.172318, 97.438210],
  popup='Pulau Baguk',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[2.079998, 97.110248],
  popup='Pulau Bangkaru',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[2.279603, 97.270927],
  popup='Haloban',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[2.320768, 97.225608],
  popup='Tlk. Nibung',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[2.179428, 97.437095],
  popup='Pulau Baguk',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[2.213735, 97.125358],
  popup='Asantola',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[2.084737, 96.637839],
  popup='Pulau Babi',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[2.444613, 97.711219],
  popup='Raket',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[2.439125, 97.815589],
  popup='Kota Baharu',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[2.333385, 97.904677],
  popup='Pertampakan',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[2.481241, 97.754302],
  popup='Gampong Tengah',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[2.422244, 97.773528],
  popup='Tlk. Rumbia',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[2.371477, 97.839446],
  popup='Pea Bumbung',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[2.399605, 97.680144],
  popup='Suka Jaya',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[2.436828, 97.819876],
  popup='Ladang Bisik',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[2.450548, 97.792410],
  popup='Lapahan Buaya',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[2.334240, 97.831090],
  popup='Selok Aceh',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[4.9335748,97.1615209],
  popup='Paya Bakong, Kabupaten Aceh Utara, Aceh',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[4.072104, 96.393694],
  popup='Tadu Raya',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[3.182104, 97.918042],
  popup='Lauser',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[2.809306, 98.063218],
  popup='Penuntungan',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[4.640788, 95.636705],
  popup='Krueng Sabee',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[4.496074, 98.094327],
  popup='Manyak Payed',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[4.227242, 98.021739],
  popup='Kejuruan Muda',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[5.622988, 95.428234],
  popup='Darussalam',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[4.838365, 95.452703],
  popup='Babah Nipah',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[5.233236, 96.803407],
  popup='Jangka',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[5.603507, 95.589731],
  popup='Lamreh',
  icon=folium.Icon(icon='info-sign')
).add_to(m)

folium.Marker(
  location=[3.199001, 97.458051],
  popup='Kluet Tim.',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[3.166093, 97.694257],
  popup='Hutan',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[3.484159, 97.1559276],
  popup='Meukek',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[3.692490, 97.386640],
  popup='Putri Betung',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[3.741825, 97.013105],
  popup='Hutan Blangpidie',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[4.010374, 97.782148],
  popup='Pertik',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[3.889811, 97.622846],
  popup='Blangtemung',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[3.692490, 97.716230],
  popup='Ketambe',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[3.922694, 97.661298],
  popup='Pintu Rime',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[4.804521, 97.326215],
  popup='Hutan',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[4.612994, 95.783960],
  popup='Panga',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[4.482755, 95.826421],
  popup='Teunom',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[4.401344, 95.993000],
  popup='Woyla Bar.',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[4.313410, 96.071390],
  popup='Bubon',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[4.674849, 95.679439],
  popup='Buntha',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[4.808307, 95.682706],
  popup='Setia Bakti',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[4.931977, 95.744764],
  popup='Gampong Baroh',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[5.003564, 95.398542],
  popup='Indra Jaya',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[5.120691, 95.601049],
  popup='Mareu',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[4.157058, 96.378418],
  popup='Tadu Raya',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[3.0176834, 97.5612038],
  popup='Alur Dua Mas',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[3.0455862, 97.5046413],
  popup='Beutong',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[2.9918179, 97.4515392],
  popup='Bukit Gading',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[4.4621579, 97.9776423],
  popup='Gampong Baro',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[4.1567174, 96.1209121],
  popup='Drien Rampak',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[3.0404027, 97.5189393],
  popup='Jambo Keupok',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[2.9300844, 7.4625416],
  popup='Keude Bakongan',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[2.9726289, 97.5074177],
  popup='Rambong',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[2.9557534, 97.5499033],
  popup='Seneubok Alur Bulah',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[3.0541172,97.4614924],
  popup='Seunebok Keranji',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[3.0482917, 97.4917939],
  popup='Ujung Gunong Rayek',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[2.9481655, 97.4881798],
  popup='Ujung Gunung Cut ',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[2.9536734, 97.3942737],
  popup='Ujung Mangk',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[2.9603464, 97.4353212],
  popup='Ujung Padang',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[2.9486944, 97.5022408],
  popup='Ujung Tanoh',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[2.90841, 97.5294162],
  popup='Ladang Rimba',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[2.894834, 97.5389398],
  popup='Pasi Seubadeh',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[2.9063503, 97.5551019],
  popup='Sawah Tingkeum',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[2.9069725, 97.5586953],
  popup='Seulekat',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[2.912255, 97.5035872],
  popup='Ujung Pulo Cut',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[2.8985919, 97.5100288],
  popup='Ujung Pulo Rayeuk',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[3.047345, 97.3285258],
  popup='Indra Damai',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[3.0682725, 97.3265981],
  popup='Jua',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[3.0617815, 97.3306073],
  popup='Kapeh',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[3.0638409, 97.3199562],
  popup='Kedai Kandang',
  icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
  location=[3.0660635, 97.3333424],
  popup='Kedai Runding',
  icon=folium.Icon(icon='info-sign')
).add_to(m)


m.save('index.html')
