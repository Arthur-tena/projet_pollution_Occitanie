---
title: "Perpignan"
format: html
---
```{python}
#|code-fold: true
import pandas as pd
import requests
from pyproj import Proj, transform
import plotly.express as px
import plotly.graph_objects as go


url='https://services9.arcgis.com/7Sr9Ek9c1QTKmbwr/arcgis/rest/services/mesures_occitanie_annuelle_poll_princ/FeatureServer/0/query?where=1%3D1&outFields=nom_dept,nom_com,insee_com,nom_station,nom_poll,valeur,unite,date_debut,x_l93,y_l93&outSR=4326&f=json'

#Extraction des données
response = requests.get(url)
if response.status_code == 200:
    data = response.json()

    # Extraction des entités de la réponse JSON
    features = data.get('features', [])

    # Extraction des données pertinentes de chaque entité
    records = []
    for feature in features:
        attributes = feature.get('attributes', {})
        records.append(attributes)

    # Création d'un DataFrame
    df_data = pd.DataFrame(records)
    df_data['valeur'].fillna(0, inplace=True)

    # Conversion de la colonne 'date_debut' qui est en millisecondes
    df_data['date_debut'] = pd.to_datetime(df_data['date_debut'], unit='ms')

    # Liste des polluants à afficher
    polluants = ['NO', 'NOX', 'O3', 'PM10', 'NO2','PM2.5']
    # Boucle à travers les polluants pour créer les graphiques
for polluant in polluants:
    #Regrouper les données de la ville de Perpignan
    filt_data = df_data[(df_data['nom_com'] == 'PERPIGNAN') & (df_data['nom_poll'] == polluant)]
    filt_data = filt_data.sort_values(by='date_debut')
        
    # Création d'un graphique
    fig = px.scatter(
        filt_data, x='date_debut', y='valeur',
        color='nom_station', size='valeur', hover_name='date_debut',
        title=f'Évolution de la pollution {polluant} à Perpignan',
        labels={'valeur': f'Valeur {polluant} (ug.m-3)', 'date_debut': 'Année'}
    )

    # Relier les points pour chaque station
    for nom_station in filt_data['nom_station'].unique():
        trace_data = filt_data[filt_data['nom_station'] == nom_station]
        fig.add_trace(go.Scatter(
            x=trace_data['date_debut'],
            y=trace_data['valeur'],
            mode='lines',  
            showlegend=False
        ))
    fig.show()
```

