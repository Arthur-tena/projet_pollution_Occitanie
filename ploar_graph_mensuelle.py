import pandas as pd
import plotly.express as px
import numpy as np
def create_polar_plot(chemin,)    
    # Chargez le fichier CSV dans un DataFrame pandas
    chemin_fichier_csv = r'/home/zack/projet_pollution_occitanie/mensuelle.csv'
    df = pd.read_csv(chemin_fichier_csv)
    df = df.dropna()

    # Convertir la colonne 'date_debut' en type datetime
    df['date_debut'] = pd.to_datetime(df['date_debut'], format='%Y/%m/%d %H:%M:%S%z')

    # Extraire le mois de chaque date
    df['mois'] = df['date_debut'].dt.month

    # Trier le DataFrame par ordre croissant de date
    df = df.sort_values(by='mois')

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
    fig = px.line_polar(df_moyennes_ville, r='moyenne_valeur', theta=df_moyennes_ville['mois']*(360//12), line_close=True,
                        color='nom_poll', line_dash='nom_poll', title='Évolution des polluants par mois de la région')
    liste_des_mois = ["Décembre","Janvier","Février", "Mars","Avril","Mai","Juin","Juillet","Août","Septembre","Octobre","Novembre"]
    fig.update_polars(
        radialaxis=dict(
            visible=False,  # Set to False if you want to hide the radial axis
        ),
        angularaxis=dict(
            visible=True,  # Set to False if you want to hide the angular axis
            rotation=120,   # Rotate the angular axis (default is 0)
            direction='clockwise',  # Set the direction of the angular axis
            period=360,   # Set the period of the angular axis
            tickvals=np.arange(0, 360, 30),
            ticktext=[i for i in liste_des_mois],  # Specify tick values on the angular axis
        )
    )
    # Afficher le graphique
    fig.show()
