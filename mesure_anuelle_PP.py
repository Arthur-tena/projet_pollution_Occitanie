import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data=pd.read_csv("/Users/arthurtena/Documents/data/Mesure_annuelle_Region_Occitanie_Polluants_Principaux.csv")
df=pd.DataFrame(data)
columns_to_drop=['code_station','typologie','influence','id_poll_ue', 'unite', 'metrique', 'date_fin', 'statut_valid' ]
df=df.drop(columns=columns_to_drop)
print(df)


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

# Créer un DataFrame par an
df_annee = {}

# Grouper par 'date_debut'
for annee, group in df.groupby('date_debut'):
    df_annee[annee] = group

# Imprimer les DataFrames pour chaque année
for annee, df_annee in df_annee.items():
    print(f"\nDataFrame pour l'année {annee} :")
    print(df_annee)


