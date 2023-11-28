import pandas as pd
import requests
from pyproj import Proj, transform
from datetime import datetime, timedelta
import os

url='https://services9.arcgis.com/7Sr9Ek9c1QTKmbwr/arcgis/rest/services/mesures_occitanie_72h_poll_princ/FeatureServer/0/query?where=1%3D1&outFields=nom_dept,nom_station,code_station,nom_poll,valeur,unite,date_debut,x_l93,y_l93&outSR=4326&f=json'

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

    #Supprimer les lignes avec des données manquantes
    df_data=df_data.dropna()
    
    # Conversion des coordonnées Lambert 93 en latitude et longitude
    in_proj = Proj(init='epsg:2154')  # Lambert 93
    out_proj = Proj(init='epsg:4326')  # WGS84 (latitude, longitude)
    df_data['longitude'], df_data['latitude'] = transform(in_proj, out_proj, df_data['x_l93'].values, df_data['y_l93'].values)

    # Conversion de la colonne 'date_debut' qui est en millisecondes
    df_data['date_debut'] = pd.to_datetime(df_data['date_debut'], unit='ms')

    # Extraire les composants jour, mois, année et heure
    df_data['date_formatee'] = df_data['date_debut'].dt.strftime('%d/%m/%Y %H:%M')

    # Créer un DataFrame par département
    df_departements = {}
    for dept, group in df_data.groupby('nom_dept'):
        df_departements[dept] = group
    """# Imprimer les DataFrames pour chaque département
    for dept, df_dept in df_departements.items():
        print(f"\nDataFrame pour le département {dept} :")
    pd.set_option('display.max_rows', None)  # Afficher toutes les lignes du DataFrame    
    print(df_departements['GERS'])"""
    
    # Regrouper les données par code_station dans chaque DataFrame de département
    df_departements_par_station = {}
    for dept, df_dept in df_departements.items():
        df_station = df_dept.groupby('code_station')
        df_departements_par_station[dept] = df_station

    # Imprimer les DataFrames regroupés par code_station pour chaque département
    for dept, df_station in df_departements_par_station.items():
        print(f"\nDataFrame pour le département {dept} regroupé par code_station:")
        for station, df in df_station:
            print(f"\nCode de station {station}:")
            
    
    # Créer un dictionnaire pour stocker les DataFrames par emplacement
    df_emplacements = {}
    # Ajouter des paires clé-valeur
    df_emplacements['FR50004','FR50021','FR50030','FR50039','FR50040','FR50048','FR50054','FR50821'] = 'Toulouse'

    # Regrouper les données par code_station dans l'ensemble du DataFrame
    df_par_station = df_data.groupby('code_station')

    print(df_par_station,'par station')


