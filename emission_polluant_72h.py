import pandas as pd
import requests
from datetime import datetime, timedelta
import plotly.express as px
import plotly.graph_objects as go

url = 'https://services9.arcgis.com/7Sr9Ek9c1QTKmbwr/arcgis/rest/services/mesures_occitanie_72h_poll_princ/FeatureServer/0/query?where=1%3D1&outFields=nom_dept,nom_station,code_station,nom_poll,valeur,unite,date_debut,x_l93,y_l93&outSR=4326&f=json'

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

    # Supprimer les lignes avec des données manquantes
    df_data = df_data.dropna()

    # Conversion de la colonne 'date_debut' qui est en millisecondes
    df_data['date_debut'] = pd.to_datetime(df_data['date_debut'], unit='ms')

    # Extraire les composants jour, mois, année et heure
    df_data['date_formatee'] = df_data['date_debut'].dt.strftime('%d/%m/%Y %H:%M')
    
    # Liste des polluants à afficher
    polluants = ['NO', 'NOX', 'O3', 'PM10', 'NO2', 'PM2.5']
    
    # Initialiser filt_data en dehors de la boucle
    filt_data = pd.DataFrame()
    
    #Connaitre les stations de la ville de Montpellier
    print(df_data['nom_station'].unique(),'mtp')

    # Liste des stations disponibles dans la ville de Montpellier
    stations_mtp = ['Montpellier - Prés d Arènes Urbain','Montpelier Antigone Trafic','Montpellier - Chaptal Urbain','Montpellier - Pompignane Trafic','Montpellier Liberte Trafic','Montpellier - Saint Denis Trafic','Montpellier Sud - Périurbain','Montpellier Nord - Périurbain'] 
    


    for polluant in polluants:
        for station in stations_mtp:
            # Regrouper les données pour la station et le polluant spécifiques
            filt_data = df_data[(df_data['nom_station'] == station) & (df_data['nom_poll'] == polluant)]
            filt_data = filt_data.sort_values(by='date_debut')
            fig=go.Figure()
            # Ajouter une trace pour chaque combinaison polluant-station
            fig.add_trace(
            go.Scatter(
                x=filt_data['date_debut'],
                y=filt_data['valeur'],
                mode='lines+markers',
                name=f'{polluant} - {station}'
            )
        )

# Mettre à jour la mise en page du graphique
fig.update_layout(
    title='Mesures de polluants dans les stations de Montpellier',
    xaxis_title='Date',
    yaxis_title='Valeur',
    legend_title='Station - Polluant',
    template='plotly_white'
)

# Afficher le graphique
fig.show()