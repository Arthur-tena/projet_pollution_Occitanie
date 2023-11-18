import pandas as pd
import requests


url='https://services9.arcgis.com/7Sr9Ek9c1QTKmbwr/arcgis/rest/services/Indice_quotidien_de_qualité_de_lair_pour_les_collectivités_territoriales_en_Occitanie/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json'
esponse = requests.get(url)

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

    print(df_data)

