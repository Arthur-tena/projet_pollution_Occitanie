import pandas as pd
import requests
import plotly.express as px

url='https://services9.arcgis.com/7Sr9Ek9c1QTKmbwr/arcgis/rest/services/mesures_occitanie_mensuelle_poll_princ/FeatureServer/0/query?where=1%3D1&outFields=nom_dept,nom_com,nom_station,nom_poll,valeur,unite,date_fin&outSR=4326&f=json'
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

    # Conversion de la colonne 'date_fin' qui est en millisecondes
    df_data['date_fin'] = pd.to_datetime(df_data['date_fin'], unit='ms')
    print(df_data)
    #Liste des polluants à afficher
    polluants = ['NO', 'NOX', 'O3', 'PM10', 'NO2','PM2.5']
    # Boucle à travers les polluants pour créer les graphiques
    for polluant in polluants:
        #Regrouper les données de la ville de Toulouse
        filt_data = df_data[(df_data['nom_com'] == 'TOULOUSE') & (df_data['nom_poll'] == polluant)]
        filt_data = filt_data.sort_values(by='date_fin')
        filt_data = filt_data.dropna()
        # Créer le graphique en ligne avec une couleur différente pour chaque polluant
        fig = px.line(
            filt_data, x='date_fin', y='valeur',
            color='nom_poll', labels={'valeur': 'Concentration (unité)', 'date_fin': 'Date de fin'},
            title='Évolution des polluants à Toulouse'
    )

        # Afficher le graphique
        fig.show()

