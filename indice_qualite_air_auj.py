import pandas as pd
import requests
import geopandas as gpd


url='https://services9.arcgis.com/7Sr9Ek9c1QTKmbwr/arcgis/rest/services/Indice_quotidien_de_qualité_de_l’air_pour_les_collectivités_territoriales_en_Occitanie/FeatureServer/0/query?where=1%3D1&outFields=date_ech,code_qual,lib_qual,code_zone,code_no2,code_so2,code_o3,code_pm10,code_pm25,x_wgs84,y_wgs84,x_reg,y_reg,coul_qual&outSR=4326&f=json'
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

    # Supposons que vous avez une colonne 'date_debut' avec des durées en millisecondes
    df_data['date_ech'] = pd.to_datetime(df_data['date_ech'], unit='ms')
    # Extraire les composants jour, mois, année et heure
    df_data['date_formatee'] = df_data['date_ech'].dt.strftime('%d/%m/%Y')

    print(df_data)

    # Créer un GeoDataFrame à partir du DataFrame avec les données
    gdf_data = gpd.GeoDataFrame(df_data, geometry=gpd.points_from_xy(df_data['x_wgs84'], df_data['y_wgs84']), crs='EPSG:4326')

    # Charger les données des départements
    departements = gpd.read_file('data/departements_occitanie.geojson')

    # Fusion des deux GeoDataFrames
    result = gpd.sjoin(gdf_data, departements, how='inner', op='within')

    # Afficher le résultat
    print(result)

    """# Créer un GeoDataFrame à partir du DataFrame avec les données
    gdf_data = gpd.GeoDataFrame(df_data, geometry=gpd.points_from_xy(df_data['x_wgs84'], df_data['y_wgs84']),crs='EPSG:4326')

    #Charger les données des départements 
    departements = gpd.read_file('data/departements_occitanie.geojson')

    #Fusion des deux GeoDataFrames
    result = gpd.sjoin(gdf_data, departements, how='inner', op='within')

    # Afficher le résultat
    print(gdf_data)"""

   

