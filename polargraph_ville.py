import pandas as pd
import plotly.express as px

# Chargez le fichier CSV dans un DataFrame pandas
chemin_fichier_csv = r'c:\Users\aicha\Downloads\mensuelle.csv'
df = pd.read_csv(chemin_fichier_csv)
df = df.dropna()

# Convertir la colonne 'date_debut' en type datetime
df['date_debut'] = pd.to_datetime(df['date_debut'], format='%Y/%m/%d %H:%M:%S%z')

# Extraire le mois de chaque date
df['mois'] = df['date_debut'].dt.month

# Dictionnaire de correspondance entre les numéros de mois et les noms des mois
liste_des_mois = {1: "Janvier", 2: "Février", 3: "Mars", 4: "Avril", 5: "Mai", 6: "Juin",
                  7: "Juillet", 8: "Août", 9: "Septembre", 10: "Octobre", 11: "Novembre", 12: "Décembre"}

# Remplacer les numéros de mois par les noms dans le DataFrame
df['mois'] = df['mois'].map(liste_des_mois)

# Trier le DataFrame par ordre croissant de date
df = df.sort_values(by='date_debut')

# Définir les polluants et la ville spécifiques
polluants = ['O3', 'PM2.5', 'NO']  # Remplacez par les noms réels de vos polluants
ville = 'TOULOUSE'  # Remplacez par le nom réel de votre ville

# Filtrer les données pour inclure uniquement les polluants spécifiés
df_filtered = df[df['nom_poll'].isin(polluants)]

# Séparer les données pour la ville spécifiée
df_ville = df_filtered[df_filtered['nom_com'] == ville]

# Calculer la moyenne des concentrations de chaque polluant à chaque heure de la journée pour la ville spécifiée
df_moyennes_ville = df_ville.groupby(['nom_poll', 'mois'])['valeur'].mean().reset_index()
df_moyennes_ville.columns = ['nom_poll', 'mois', 'moyenne_valeur']

# Créer un graphique polaire avec Plotly Express
fig = px.line_polar(df_moyennes_ville, r='moyenne_valeur', theta='mois', line_close=True,
                    color='nom_poll', line_dash='nom_poll', title='Évolution des polluants par mois')


# Afficher le graphique
fig.show()
