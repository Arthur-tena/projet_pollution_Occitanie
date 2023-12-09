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
    columns_to_drop=['unite','x_l93', 'y_l93', 'nom_station']
    df=df_data.drop(columns=columns_to_drop)
    # Initialiser filt_data en dehors de la boucle
    df_departements = {}
    for dept, group in df.groupby('nom_dept'):
     df_departements[dept] = group
 
    stations_mtp = ['FR50200','FR50201','FR50202','FR50203','FR50204','FR50205','FR50225','FR50227'] 
    stations_Tls = ['FR50004','FR50021','FR50030','FR50039','FR50040','FR50048', 'FR50054', 'FR50821']
    
    """  df_Tls = []

    for station in stations_Tls:
     df_station = df[df['code_station'] == station]
     df_Tls.append(df_station)

     fig = px.line_polar(
        df_Tls,
        r="valeur",
        theta="date_debut",
        color="nom_poll",
        line_close=True,
        range_r=[0, 30],
        start_angle=0,
        template="seaborn",
        title=f"Évolution des polluants pour la station {station}",
     )

     fig.show()
   stations_Tls = ['FR50004', 'FR50021', 'FR50030', 'FR50039', 'FR50040', 'FR50048', 'FR50054', 'FR50821']
  """
 # Filtrer les données pour les stations de Toulouse
    df_Tls = df[df['code_station'].isin(stations_Tls)]

 # Convertir la colonne 'date_debut' en format de date
    df_Tls['date_debut'] = pd.to_datetime(df_Tls['date_debut'], unit='ms')

 # Liste des polluants à afficher
    polluants = ['NO', 'NOX', 'O3', 'PM10', 'NO2', 'PM2.5'] 
    df_Tls["month"] = df_Tls["date_debut"].dt.month
    df_Tls_month = df_Tls.groupby(["month", df_Tls['month']]).size().unstack(level=0)
    print(df_Tls_month.head())

    """df_Tls["month"] = df_Tls.index.month
    df_Tls_month = (
    df_Tls.groupby(["month", df_Tls.index.hour])["valeur"]
    .count()
    .unstack(level=0))
    df_Tls.head()"""
 # Créer un graphique polaire pour chaque station
    for station in stations_Tls:
     df_station = df_Tls_month[df_Tls_month.index.isin(df_Tls[df_Tls['code_station'] == station]["month"].unique())]
     df_station.reset_index(inplace=True)
     df_station.columns = ['date_debut'] + list(df_station.columns[1:])
     df_Tls={df_station,df_Tls}
     print(df_Tls)
     """fig = px.line_polar(
        df_station,
        r="valeur",
        theta="date_debut",
        color="nom_poll",
        line_close=True,
        range_r=[0, 300],
        start_angle=0,
        template="seaborn",
        title=f"Évolution des polluants pour la station {station}",
     )

     fig.show()"""
    
   



    

    
