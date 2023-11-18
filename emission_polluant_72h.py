import pandas as pd
import matplotlib.pyplot as plt
import requests
from pyproj import Proj, transform
from datetime import datetime

url='https://services9.arcgis.com/7Sr9Ek9c1QTKmbwr/arcgis/rest/services/mesures_occitanie_72h_poll_princ/FeatureServer/0/query?where=1%3D1&outFields=nom_dept,nom_station,code_station,nom_poll,valeur,unite,date_debut,date_fin,x_l93,y_l93&outSR=4326&f=json'

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
    
    # Conversion des données temporelles en format conventionnel (datetime)
    #df_data['date_debut'] = pd.to_datetime(df_data['date_debut'])
   
    # Conversion des coordonnées Lambert 93 en latitude et longitude
    in_proj = Proj(init='epsg:2154')  # Lambert 93
    out_proj = Proj(init='epsg:4326')  # WGS84 (latitude, longitude)
    df_data['longitude'], df_data['latitude'] = transform(in_proj, out_proj, df_data['x_l93'].values, df_data['y_l93'].values)
    
    print(df_data.tail()) 
    #reste a voir comment on va les gérer pour les faires apparaitre sur la carte

    # Créer un DataFrame par département
    df_departements = {}
    for dept, group in df_data.groupby('nom_dept'):
        df_departements[dept] = group
    # Imprimer les DataFrames pour chaque département
    for dept, df_dept in df_departements.items():
        print(f"\nDataFrame pour le département {dept} :")
        print(df_dept)



