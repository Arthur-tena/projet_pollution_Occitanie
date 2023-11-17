import pandas as pd
import matplotlib.pyplot as plt
import requests

url='https://services9.arcgis.com/7Sr9Ek9c1QTKmbwr/arcgis/rest/services/mesures_occitanie_72h_poll_princ/FeatureServer/0/query?where=1%3D1&outFields=nom_dept,nom_station,code_station,nom_poll,id_poll_ue,valeur,unite,date_debut,x_l93,y_l93&outSR=4326&f=json'

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
else:
    print("Erreur")

print(df_data)
