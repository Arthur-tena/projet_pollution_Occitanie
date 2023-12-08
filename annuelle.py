import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def afficher_evolution_pollution(nom_ville, chemin_fichier_csv, polluants):
    pd.options.mode.chained_assignment = None

    # Chargez le fichier CSV dans un DataFrame pandas
    df = pd.read_csv(chemin_fichier_csv)

    # Convertir la colonne 'date_debut' en type datetime
    df['date_debut'] = pd.to_datetime(df['date_debut'], format='%Y/%m/%d %H:%M:%S%z')

    # Trier le DataFrame par ordre croissant de date
    df = df.sort_values(by='date_debut')


    # Afficher la liste des polluants présents dans le DataFrame
    liste_polluants = df['nom_poll'].unique()
    print("Liste des polluants :", liste_polluants)

    # Boucle à travers les polluants pour créer les graphiques
    for polluant in polluants:
        # Regrouper les données de la ville spécifiée
        filt_data = df[(df['nom_com'] == nom_ville) & (df['nom_poll'] == polluant)]
        filt_data = filt_data.sort_values(by='date_debut')
        filt_data = filt_data.dropna()

        # Création d'un graphique
        fig = px.scatter(
            filt_data, x='date_debut', y='valeur',
            color='nom_station', hover_name='date_debut',
            title=f'Évolution de la pollution {polluant} à {nom_ville}',
            labels={'valeur': f'Valeur {polluant} (ug.m-3)', 'date_debut': 'Année'}
        )

        # Relier les points pour chaque station
        for nom_station in filt_data['nom_station'].unique():
            trace_data = filt_data[filt_data['nom_station'] == nom_station]
            fig.add_trace(go.Scatter(
                x=trace_data['date_debut'],
                y=trace_data['valeur'],
                mode='lines',
                showlegend=False
            ))
        fig.show()

# Spécifiez le chemin du fichier CSV
chemin_fichier_csv = r'c:\Users\aicha\Downloads\annuelle.csv'

# Liste des polluants à afficher
polluants_a_afficher = ['NO2', 'PM2.5', 'PM10', 'NOX', 'NO']

# Nom de la ville
nom_de_la_ville = 'TOULOUSE'

# Appeler la fonction
afficher_evolution_pollution(nom_de_la_ville, chemin_fichier_csv, polluants_a_afficher)
