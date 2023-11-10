import pandas as pd
import matplotlib.pyplot as plt

# Charger les données de pollution à partir d'un fichier CSV
data = pd.read_csv(r'C:\Users\aicha\Downloads\emission_polluant_2018.csv')

# Afficher les premières lignes du DataFrame pour vérifier les données
print(data.head())

# Afficher les noms des colonnes
column_names = data.columns
print(column_names)

# Supprimer plusieurs colonnes
columns_to_drop = ['ESRI_OID', 'lib_epci','version','annee_inv','SHAPE_Length','SHAPE_Area','ges_teqco2']
data = data.drop(columns=columns_to_drop)
print(data.head())

"""# Sélectionner les colonnes à utiliser pour le tracé
data_to_plot = data[['date_ech', 'val_no2', 'val_o3', 'val_pm25']]

# Convertir la colonne "date_ech" en format de date (si ce n'est pas déjà le cas)
data_to_plot['date_ech'] = pd.to_datetime(data_to_plot['date_ech'])

# Regrouper les données par mois et calculer la moyenne
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



"""import pandas as pd
import plotly.express as px
from plotly.offline import plot
import numpy as np
x = np.arange(13)
bdd = pd.read_csv("/home/qufst/projetgroupe2/GroupProject/basededonnee2020/donnees2020.csv")
bdd2 = bdd[bdd['code_zone'] == 200070803]
bdd2['coleur']='haute pyrenees'
bdd3 = bdd[bdd['code_zone'] == 200042372]
bdd3['coleur']='gers'
bdd4 = bdd[bdd['code_zone'] == 248200099]
bdd4['coleur']='tarn et garonne'
bdd5 = bdd[bdd['code_zone'] == 244600573]
bdd5['coleur']='lot'
bdd6 = bdd[bdd['code_zone'] == 241200187]
bdd6['coleur']='aveyron'
bdd7 = bdd[bdd['code_zone'] == 241200914]
bdd7['coleur']='tarn'
bdd8 = bdd[bdd['code_zone'] == 243100518]
bdd8['coleur']='haute garonne'
bdd9 = bdd[bdd['code_zone'] == 200066223]
bdd9['coleur']='ariege'
bdd10 = bdd[bdd['code_zone'] == 200069144]
bdd10['coleur']='lozere'
bdd11 = bdd[bdd['code_zone'] == 200034692]
bdd11['coleur']='gard'
bdd12 = bdd[bdd['code_zone'] == 243400819]
bdd12['coleur']='herault'
bdd13 = bdd[bdd['code_zone'] == 200035715]
bdd13['coleur']='aude'
bdd14 = bdd[bdd['code_zone'] == 200027183]
bdd14['coleur']='pyrenees orientales'

BDD = pd.concat([bdd2, bdd3, bdd4, bdd5, bdd6, bdd7, bdd8, bdd9, bdd10, bdd11, bdd12, bdd13, bdd14], ignore_index=True)


fig = px.scatter(BDD, x='date_ech', y='val_no2', animation_frame='date_ech',animation_group='code_zone', color='coleur',size = 'val_no2',hover_name='date_ech',log_x=False,range_x=(0,355),range_y=(-1,5))
#fig = px.line(BDD, x='date_ech', y='val_no2', animation_frame='date_ech', animation_group='code_zone', color='coleur', line_shape='linear')
fig.update_layout(
    title='évolution du no2 en stade en occitanie durant2020',
    xaxis_title='2020',
    yaxis_title='Stade de pollution')
fig.show()"""