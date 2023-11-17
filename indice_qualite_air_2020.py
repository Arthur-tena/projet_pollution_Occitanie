import pandas as pd

# Charger les données de pollution à partir d'un fichier CSV
data = pd.read_csv(r'C:\Users\aicha\Downloads\indice_qualite_air_2020.csv')

# Afficher les premières lignes du DataFrame pour vérifier les données
print(data.head())

# Afficher les noms des colonnes
column_names = data.columns
print(column_names)

# Supprimer une ou plusieurs colonnes
columns_to_drop = ['id', 'source', 'type_zone', 'qualif', 'lib_zone', 'couleur', 'ObjectId', 'val_no2', 'val_o3', 'val_pm25']
data = data.drop(columns=columns_to_drop)
print(data.head())

# Sélectionner les colonnes à utiliser pour les tableaux
#data_to_plot = data[['date_ech', 'code_zone','valeur']]

# Convertir la colonne "date_ech" en format de date (si ce n'est pas déjà le cas)
data['date_ech'] = pd.to_datetime(data['date_ech'], dayfirst=True)

# Créer un tableau avec les données récupérées
tableau_de_donnees = data[['date_ech', 'code_zone', 'valeur']]
# Afficher le tableau de données
print(tableau_de_donnees)




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
