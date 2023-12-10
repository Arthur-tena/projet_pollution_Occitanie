# Récupération de données 2020
import requests
import json
import pandas as pd

url_2020 = "https://services9.arcgis.com/7Sr9Ek9c1QTKmbwr/arcgis/rest/services/mesures_occitanie_annuelle_poll_princ/FeatureServer/0/query?where=1%3D1&outFields=nom_dept,nom_com,code_station,nom_poll,unite&outSR=4326&f=json"

# Faire une requête GET pour obtenir les données JSON depuis l'URL
response = requests.get(url_2020)

# Vérifier si la requête a réussi
if response.status_code == 200:
    # Les données sont dans le format JSON, vous pouvez les récupérer en utilisant .json()
    data = response.json()
    # Maintenant, vous pouvez travailler avec les données JSON
    print(data)
    # Création Dataframe
    df_data = pd.DataFrame(data)
    pd.set_option("display.max_rows", None)

else:
    # En cas d'erreur dans la requête
    print(f"La requête a échoué avec le code d'état : {response.status_code}")

# Extraction des données
# nom_poll=
