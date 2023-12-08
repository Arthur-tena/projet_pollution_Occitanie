import pandas as pd
import plotly.express as px

def create_polar_plot(chemin_fichier_csv, polluants, ville):
    # Chargez le fichier CSV dans un DataFrame pandas
    df = pd.read_csv(chemin_fichier_csv)

    # Convertir la colonne 'date_debut' en type datetime
    df['date_debut'] = pd.to_datetime(df['date_debut'], format='%Y/%m/%d %H:%M:%S%z')

    # Trier le DataFrame par ordre croissant de date
    df = df.sort_values(by='date_debut')

    # Liste des couleurs pour chaque polluant
    couleurs = ['blue', 'red', 'green', 'purple', 'orange', 'pink', 'brown']

    # Filtrer les données pour inclure uniquement les polluants spécifiés
    df_filtered = df[df['nom_poll'].isin(polluants)]

    # Séparer les données pour la ville spécifiée
    df_ville = df_filtered[df_filtered['nom_com'] == ville]

    noms_communes = df['nom_com'].unique()
    print("Noms de communes présents dans le DataFrame :", noms_communes)

    # Calculer la moyenne des concentrations de chaque polluant à chaque heure de la journée pour la ville spécifiée
    df_moyennes_ville = df_ville.groupby(['nom_poll', df_ville['date_debut'].dt.hour])['valeur'].mean().reset_index()
    df_moyennes_ville.columns = ['nom_poll', 'heure', 'moyenne']

    # Créer un graphique polaire pour l'évolution des polluants sur toutes les heures
    fig = px.line_polar(
        df_moyennes_ville,
        r="moyenne",
        theta=df_moyennes_ville['heure'] * (360//24),
        color="nom_poll",
        line_close=True,
        range_r=[0, df_moyennes_ville['moyenne'].max() + 10],
        start_angle=0,
        template="seaborn",
        title=f"Évolution des polluants sur toutes les heures à {ville}",
        labels={"heure": "Heure"}
    )

    # Ajouter des annotations textuelles pour afficher l'heure correspondante
    for i, row in df_moyennes_ville.iterrows():
        heure_text = f"{row['heure']:02d}:00"
        fig.add_annotation(
            x=row['heure'] * 15,
            y=row['moyenne'],
            text=heure_text,
            showarrow=False,
            font=dict(size=10),
            textangle=row['heure'] * 15
        )

    # Personnaliser l'affichage du graphique polaire pour inclure les heures sur tout le cercle
    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True),
            angularaxis=dict(

                tickmode='array',
                tickvals=list(range(24)),
                ticktext=[f"{i:02d}:00" for i in range(24)]
            )
        )
    )

    # Afficher le graphique polaire interactif
    fig.show()

# Exemple d'utilisation de la fonction
chemin_fichier_csv = r'c:\Users\aicha\Downloads\Mesure_30j.csv'
polluants_a_afficher = ['NO2', 'PM2.5', 'PM10', 'NOX', 'NO']
ville_a_afficher = 'PERPIGNAN'

create_polar_plot(chemin_fichier_csv, polluants_a_afficher, ville_a_afficher)
