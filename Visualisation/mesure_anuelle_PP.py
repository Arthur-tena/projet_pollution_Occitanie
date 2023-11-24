import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data=pd.read_csv("/Users/arthurtena/Documents/data/Mesure_annuelle_Region_Occitanie_Polluants_Principaux.csv")
df=pd.DataFrame(data)
columns_to_drop=['code_station','typologie','influence','id_poll_ue', 'unite', 'metrique', 'date_fin', 'statut_valid' ]
df=df.drop(columns=columns_to_drop)
print(df)

# %%
# Créer un DataFrame par département
df_departements = {}
for dept, group in df.groupby('nom_dept'):
 df_departements[dept] = group
    # Imprimer les DataFrames pour chaque département
 for dept, df_dept in df_departements.items():
     print(f"\nDataFrame pour le département {dept} :")
     print(df_dept)

num_cols = 4

# Calculer le nombre total de sous-graphiques nécessaires
total_subplots = len(df_departements)

# Calculer le nombre de lignes nécessaire
num_rows = (total_subplots + num_cols - 1) // num_cols

# Créer une figure et des axes pour les sous-graphiques
fig, axes = plt.subplots(nrows=num_rows, ncols=num_cols, figsize=(10, 3*num_rows))

# Iterer sur les départements et créer un diagramme circulaire pour chacun
for i, (dept, df_dept) in enumerate(df_departements.items()):
    df_dept = df_dept.dropna()
    
    # Grouper par 'nom_poll' et calculer la somme des valeurs
    df_dept = df_dept.groupby('nom_poll')['valeur'].sum().reset_index()

    name = df_dept['nom_poll']
    value = df_dept['valeur']

    # Calculer les coordonnées (ligne, colonne) pour placer le diagramme circulaire
    row = i // num_cols
    col = i % num_cols

    # Placer le diagramme circulaire sur l'axe correspondant
    ax = axes[row, col]
    ax.pie(value, labels=name, autopct='%1.1f%%', startangle=90, shadow=True)
    ax.axis('equal')
    ax.set_title(f"Répartition des polluants - {dept}")

# Ajuster l'espacement entre les sous-graphiques
plt.tight_layout()

# Afficher la figure
plt.show()


#O3=Ozone est formé à partir de réaction chimiqe entre les oxyde d'azote (NOx) et les composés organiques volatile (COV) sous l'effet du soleil
#Il s'agit d'un polluant secondaire car n'est pas émis directement dans l'air (Ecologie.gouv)


# %%
import pandas as pd
import matplotlib.pyplot as plt

# Charger les données
data = pd.read_csv("/Users/arthurtena/Documents/data/Mesure_annuelle_Region_Occitanie_Polluants_Principaux.csv")
df = pd.DataFrame(data)

# Supprimer les colonnes inutiles
columns_to_drop = ['code_station', 'typologie', 'influence', 'id_poll_ue', 'unite', 'metrique', 'date_fin', 'statut_valid']
df = df.drop(columns=columns_to_drop)

# Grouper par 'date_debut' et 'nom_poll', puis calculer la somme des valeurs
grouped_df = df.groupby(['date_debut', 'nom_poll'])['valeur'].sum().reset_index()

# Trier le DataFrame par 'date_debut' et 'nom_poll'
grouped_df = grouped_df.sort_values(by=['date_debut', 'nom_poll'])

# Créer une figure
plt.figure(figsize=(12, 8))

# Obtenir la liste des couleurs standard de matplotlib
colors = plt.cm.get_cmap('tab10', len(grouped_df['nom_poll'].unique()))

# Espacement entre les groupes de barres
bar_width = 0.2
bar_spacing = 0.1

# Créer un dictionnaire pour stocker les index de chaque année
year_indexes = {year: i for i, year in enumerate(grouped_df['date_debut'].unique())}

# Afficher un histogramme pour chaque année avec plusieurs barres pour les polluants
for polluant, color in zip(grouped_df['nom_poll'].unique(), colors.colors):
    plt.bar(
        [year_indexes[annee] + j * (bar_width + bar_spacing) for j, annee in enumerate(grouped_df['date_debut'].unique())],
        grouped_df[grouped_df['nom_poll'] == polluant]['valeur'],
        width=bar_width,
        label=polluant,
        color=color
    )

# Ajouter des étiquettes et un titre
plt.xlabel('Année')
plt.ylabel('Somme des valeurs')
plt.title('Valeurs des principaux polluants par année')
plt.legend(title='Polluant', bbox_to_anchor=(1, 1))  # Placer la légende à l'extérieur du graphique

# Ajuster l'emplacement des ticks sur l'axe des x
plt.xticks([i for i in range(len(grouped_df['date_debut'].unique()))], grouped_df['date_debut'].unique())

# Afficher le graphique
plt.show()
# %%
#crée un graphique qui montre l'évolution des polluants années après années avec des lignes 
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import numpy as np
from scipy import stats

# Charger les données
data = pd.read_csv("/Users/arthurtena/Documents/data/Mesure_annuelle_Region_Occitanie_Polluants_Principaux.csv")
df = pd.DataFrame(data)

# Supprimer les colonnes inutiles
columns_to_drop = ['code_station', 'typologie', 'influence', 'id_poll_ue', 'unite', 'metrique', 'date_fin', 'statut_valid']
df = df.drop(columns=columns_to_drop)

# Grouper par 'date_debut' et 'nom_poll', puis calculer la somme des valeurs
grouped_df = df.groupby(['date_debut', 'nom_poll'])['valeur'].sum().reset_index()
print(grouped_df)