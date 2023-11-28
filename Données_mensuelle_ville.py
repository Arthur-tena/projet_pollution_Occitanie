import pandas as pd
import requests

url='https://services9.arcgis.com/7Sr9Ek9c1QTKmbwr/arcgis/rest/services/mesures_occitanie_mensuelle_poll_princ/FeatureServer/0/query?where=1%3D1&outFields=nom_dept,nom_com,nom_station,nom_poll,valeur,unite,date_debut,x_l93,y_l93&outSR=4326&f=json'

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
# Liste des polluants à afficher
polluants = ['NO', 'NOX', 'O3', 'PM10', 'NO2','PM2.5']
for polluant in polluants:
    # Conversion de la colonne 'date_debut' qui est en millisecondes
    df_data['date_debut'] = pd.to_datetime(df_data['date_debut'], unit='ms')
    #Filtrage des données
    filt_data = df_data[(df_data['nom_com'] == 'TOULOUSE')& (df_data['nom_poll'] == polluant)]
    filt_data2 = df_data[(df_data['nom_com'] == 'MONTPELLIER')& (df_data['nom_poll'] == polluant)]
    filt_data3 = df_data[(df_data['nom_com'] == 'NIMES')& (df_data['nom_poll'] == polluant)]
    filt_data4 = df_data[(df_data['nom_com'] == 'PERPIGNAN')& (df_data['nom_poll'] == polluant)]
    print(filt_data4)




    
