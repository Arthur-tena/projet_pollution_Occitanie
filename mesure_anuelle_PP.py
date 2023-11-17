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

# Créer un DataFrame par an
df_annee = {}

# Grouper par 'date_debut'
for annee, group in df.groupby('date_debut'):
    df_annee[annee] = group

# Imprimer les DataFrames pour chaque année
for annee, df_annee in df_annee.items():
    print(f"\nDataFrame pour l'année {annee} :")
    print(df_annee)


df_gard=df_departements['GARD']
df_gard=df_gard.dropna()
print(df_gard)
df_gard = df_gard.groupby('nom_poll')['valeur'].sum().reset_index()

name = df_gard['nom_poll']
value=df_gard['valeur']
plt.pie(value, labels=name, autopct='%1.1f%%', startangle=90, shadow=True)
plt.axis('equal')
plt.show()