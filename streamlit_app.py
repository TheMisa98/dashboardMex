import plotly.express as px
import requests
import pandas as pd
repo_url = 'https://raw.githubusercontent.com/angelnmara/geojson/master/mexicoHigh.json'
# Archivo GeoJSON
mx_regions_geo = requests.get(repo_url).json()

data = {'estado': {
    1: "Aguascalientes",
    2: "Baja California",
    3: "Baja California Sur",
    4: "Campeche",
    5: "Coahuila",
    6: "Colima",
    7: "Chiapas",
    8: "Chihuahua",
    9: "Ciudad de México",
    10: "Durango",
    11: "Guanajuato",
    12: "Guerrero",
    13: "Hidalgo",
    14: "Jalisco",
    15: "México",
    16: "Michoacán",
    17: "Morelos",
    18: "Nayarit",
    19: "Nuevo León",
    20: "Oaxaca",
    21: "Puebla",
    22: "Querétaro",
    23: "Quintana Roo",
    24: "San Luis Potosí",
    25: "Sinaloa",
    26: "Sonora",
    27: "Tabasco",
    28: "Tamaulipas",
    29: "Tlaxcala",
    30: "Veracruz",
    31: "Yucatán",
    32: "Zacatecas"
},
    'population': {
    1:  1425607,
    2:  3769020,
    3:  798447,
    4:  928363,
    5:  3146771,
    6:  731391,
    7:  5543828,
    8:  3741869,
    9:  9209944,
    10: 1832650,
    11: 6166934,
    12: 3540685,
    13: 3082841,
    14: 8348151,
    15: 16992418,
    16: 4748846,
    17: 1971520,
    18: 1235456,
    19: 5784442,
    20: 4132148,
    21: 6583278,
    22: 2368467,
    23: 1857985,
    24: 2822255,
    25: 3026943,
    26: 2944840,
    27: 2402598,
    28: 3527735,
    29: 1342977,
    30: 8062579,
    31: 2320898,
    32: 1622138
}}

df = pd.DataFrame({'estado': data['estado'].values(
), 'population':   data['population'].values()})

fig = px.choropleth(data_frame=df,
                    geojson=mx_regions_geo,
                    # nombre de la columna del Dataframe
                    locations=df['estado'],
                    # ruta al campo del archivo GeoJSON con el que se hará la relación (nombre de los estados)
                    featureidkey="properties.name",
                    # El color depende de las cantidades
                    color=df['population'],
                    color_continuous_scale="burg",
                    # scope="north america"
                    )

fig.update_geos(showcountries=True, showcoastlines=True,
                showland=True, fitbounds="locations")
fig.show()