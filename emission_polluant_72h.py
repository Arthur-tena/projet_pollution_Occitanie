import pandas as pd
import matplotlib.pyplot as plt
import requests
from pyproj import Proj, transform
from datetime import datetime, timedelta

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

    # Supposons que vous avez une colonne 'date_debut' avec des durées en millisecondes
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
            
    
   # Charger les données depuis le fichier CSV
    df_emplacements = pd.read_csv('data\code_station_emplacement.csv', encoding='latin-1')


    # Créer un dictionnaire à partir du DataFrame
    dict_emplacements = dict(zip(df_emplacements['code_station'], df_emplacements['emplacement']))

    # Regrouper les données par code_station dans l'ensemble du DataFrame
    df_par_station = df_data.groupby('code_station')

    # Utiliser le dictionnaire pour associer chaque code de station à son emplacement correspondant
    for code_station, df_station in df_par_station:
        emplacement = dict_emplacements.get(code_station, 'Autre')  # 'Autre' par défaut si le code n'est pas dans le dictionnaire
        print(f"\nDataFrame pour la station {code_station} à l'emplacement {emplacement}:")
        print(df_station)

