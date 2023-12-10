import requests
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import datetime
import plotly.graph_objects as go
import numpy as np


# url='https://services9.arcgis.com/7Sr9Ek9c1QTKmbwr/arcgis/rest/services/mesures_occitanie_mensuelle_poll_princ/FeatureServer/0/query?where=1%3D1&outFields=nom_dept,nom_com,nom_station,nom_poll,valeur,unite,date_fin&outSR=4326&f=json'


def graph(url, attribute, city):
    def get_data(url):
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Échec de la récupération des données depuis {url}")
            return None

    # Récupérer les données de l'URL fournie
    data = get_data(url)

    if data is not None:
        # Extraction des entités de la réponse JSON
        features = data.get("features", [])

        # Extraction des données pertinentes de chaque entité
        records = []
        for feature in features:
            attributes = feature.get("attributes", {})
            records.append(attributes)

        # Création d'un DataFrame
        df_data = pd.DataFrame(records)
        df_data["valeur"].fillna(0, inplace=True)

        # Conversion de la colonne 'date_fin' qui est en millisecondes
        df_data["date_fin"] = pd.to_datetime(df_data["date_fin"], unit="ms")

        # Liste des polluants à afficher
        polluants = ["NO", "NOX", "O3", "PM10", "NO2", "PM2.5"]

        # Vérifier si la ville spécifiée est dans les données
        if city.upper() not in df_data["nom_com"].str.upper().unique():
            print(f"Ville '{city}' introuvable dans les données.")
            return

        # Filtrer les données par ville et polluant
        filt_data = df_data[
            (df_data["nom_com"].str.upper() == city.upper())
            & (df_data["nom_poll"].isin(polluants))
        ]
        filt_data = filt_data.sort_values(by="date_fin").dropna()

        # Agrégation des données par mois et polluant
        agg_data = (
            filt_data.groupby(["nom_poll", pd.Grouper(key="date_fin", freq="M")])[
                "valeur"
            ]
            .mean()
            .reset_index()
        )

        # Créer la figure
        fig = px.line(
            agg_data,
            x="date_fin",
            y="valeur",
            color="nom_poll",
            labels={"valeur": "Valeur moyenne"},
        )

        # Personnaliser la mise en page
        fig.update_layout(
            title=f"Valeur moyenne mensuelle des polluants à {city} en (ug.m-3)",
            xaxis_title="Mois",
            yaxis_title="Valeur moyenne en (ug.m-3)",
            template="simple_white",
        )

        # Afficher le graphique
        fig.show()
