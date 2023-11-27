import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

df_h=pd.read_csv('C:/Users/aicha/OneDrive/Bureau/Projet pollution Occitanie/projet_pollution_Occitanie/data/HERAULT.csv')
df_h['valeur'].fillna(0, inplace=True)

# Liste des polluants à afficher
polluants = ['NO', 'NOX', 'O3', 'PM10', 'NO2']

# Créer un graphique en ligne pour chaque polluant
for polluant in polluants:
    fig = px.scatter(df_h[df_h['nom_poll'] == polluant], x='date_debut', y='valeur', 
                  title=f'Évolution de {polluant} au fil du temps',
                  labels={'valeur': 'Concentration de Polluant', 'date_debut': 'Date'})

    fig.show()

#MONTPELLIER

montpellier72h=pd.read_csv('C:/Users/aicha/OneDrive/Bureau/Projet pollution Occitanie/projet_pollution_Occitanie/data/Montpellier.csv')
montpellier72h['valeur'].fillna(0, inplace=True)

# Liste des polluants à afficher
polluants = ['NO', 'NOX', 'O3', 'PM10', 'NO2']

# Créer un graphique en ligne pour chaque polluant
for polluant in polluants:
    fig = px.scatter(montpellier72h[montpellier72h['nom_poll'] == polluant], x='date_debut', y='valeur', 
                  title=f'Évolution de {polluant} au fil du temps à Montpellier',
                  labels={'valeur': 'Concentration de Polluant', 'date_debut': 'Date'})

    fig.show()

