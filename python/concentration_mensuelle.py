import requests
import json
import pandas as pd
import datetime
from IPython.display import HTML
from IPython.display import display
import numpy as np

url = "https://services9.arcgis.com/7Sr9Ek9c1QTKmbwr/arcgis/rest/services/mesures_occitanie_mensuelle_poll_princ/FeatureServer/0/query?where=1%3D1&outFields=nom_dept,nom_com,nom_poll,valeur,date_debut&outSR=4326&f=json"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    # Extraction des entités de la réponse JSON
    features = data.get("features", [])

    # Extraction des données pertinentes de chaque entité
    records = []
    for feature in features:
        attributes = feature.get("attributes", {})
        records.append(attributes)

    # Création d'un DataFrame
    df_data = pd.DataFrame(records)

    # Supprimer les lignes avec des données manquantes
    df_data = df_data.dropna()

    # Convertir la colonne 'date_debut' en format datetime si ce n'est pas déjà fait
    df_data["date_debut"] = pd.to_datetime(df_data["date_debut"], errors="coerce")

    # Grouper les valeurs de chaque polluant
    grouped_data = df_data.groupby("nom_poll")["valeur"].agg(list).reset_index()

    # Affichage du DataFrame
    pd.set_option(
        "display.max_rows", 10
    )  # Ajustez le nombre de lignes affichées selon vos besoins
    display(df_data)

    print(grouped_data)
