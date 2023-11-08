import pandas as pd
import matplotlib.pyplot as plt

# Charger les données de pollution à partir d'un fichier CSV
data = pd.read_csv(r'C:\Users\aicha\Downloads\indice_qualite_air_2020.csv')

# Afficher les premières lignes du DataFrame pour vérifier les données
print(data.head())

# Afficher les noms des colonnes
column_names = data.columns
print(column_names)

# Supprimer une ou plusieurs colonnes
columns_to_drop = ['id', 'source', 'type_zone', 'valeur', 'qualif', 'lib_zone', 'couleur', 'ObjectId', 'code_zone', 'val_no2', 'val_o3', 'val_pm25']
data = data.drop(columns=columns_to_drop)
print(data.head())

# Sélectionner les colonnes à utiliser pour le tracé
data_to_plot = data[['date_ech', 'code_zone','valeur']]

# Convertir la colonne "date_ech" en format de date (si ce n'est pas déjà le cas)
data['date_ech'] = data['date_ech'].apply(pd.to_datetime)


"""#Extraction des données
temp = data[0]['hourly']['temperature_2m']
windspeed = data[0]['hourly']['windspeed_10m']
sunset = data[0]['daily']['sunset']
rain = data[0]['hourly']['precipitation']
sunrise = data[0]['daily']['sunrise']
humidity = data[0]['hourly']['relativehumidity_2m']
snow=data[0]['hourly']['snowfall']"""

"""Regrouper les données par mois et calculer la moyenne
data_grouped = data_to_plot.groupby(data_to_plot['date_ech'].dt.to_period('M')).mean()

# Tracer un graphique à barres
plt.figure(figsize=(4, 5))  # Facultatif : définir la taille du graphique
plt.bar(data_grouped.index.strftime('%b %Y'), data_grouped['val_no2'], label='val_no2')
plt.bar(data_grouped.index.strftime('%b %Y'), data_grouped['val_o3'], label='val_o3')
plt.bar(data_grouped.index.strftime('%b %Y'), data_grouped['val_pm25'], label='val_pm25')
bottom=data_grouped['val_no2'] + data_grouped['val_o3']
plt.xlabel('Mois')
plt.ylabel('Valeurs moyennes')
plt.title('Qualité de l\'air en fonction du mois')
plt.xticks(rotation=45)
plt.legend()

# Afficher le graphique
plt.show()"""
