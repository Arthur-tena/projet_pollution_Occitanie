# Départements

import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
import os

pd.options.mode.chained_assignment = None


def plot_pie(departement):
    pd.options.mode.chained_assignment = None
    """
    Cette fonction prend en argument un département de l'Occiatnie et renvoie un
    pie chart qui représente la part de chaque polluants au cours des cinq dernières années
    """
    # Chargement du fichier CSV
    data = pd.read_csv(
        "../data_visu/Mesure_annuelle_Region_Occitanie_Polluants_Principaux.csv"
    )
    df = pd.DataFrame(data)  # Création du Data Frame
    columns_to_drop = [
        "code_station",
        "typologie",
        "influence",
        "id_poll_ue",
        "unite",
        "metrique",
        "date_fin",
        "statut_valid",
    ] 
    df = df.drop(columns=columns_to_drop) # Suppression des colonnes à supprimer dans le DataFrame
    df = df.drop(columns=columns_to_drop) 


    df_departement = df[df["nom_dept"] == departement] #Création d'un nouveau Data Frame en extrayant les lignes de df où la colonne "nom_dept" est égale à la variable departement

    df_departement = df_departement.dropna() #Suppression les lignes contenant des valeurs manquantes 
    df_departement = df_departement.groupby("nom_poll")["valeur"].sum().reset_index() 

    name = df_departement["nom_poll"]
    value = df_departement["valeur"]

    plt.figure(figsize=(6, 6))
    plt.pie(value, labels=name, autopct="%1.1f%%", startangle=90, shadow=True)
    plt.axis("equal")
    plt.title(f"Répartition des polluants pour le département {departement}")
    plt.show()



def polluant_evolution_dept_jour(csv, polluants, dept):
    pd.options.mode.chained_assignment = None
    """Cette fonction prend en argument un fichier CSV, la liste des polluants à afficher, ainsi que le département que l'on souhaite afficher et trace un graphique polair qui représente l'évolution de la concentration de chaque polluants choisis au cours de la journée"""
    # Chargement du fichier CSV
    df = pd.read_csv(csv)
    #Conversion en format datetime
    df["date_debut"] = pd.to_datetime(df["date_debut"], format="%Y/%m/%d %H:%M:%S%z")
    #Tri des dates dans l'ordre croissant
    df = df.sort_values(by="date_debut")
    
    df_filtered = df[df["nom_poll"].isin(polluants)]

    df_city = df_filtered[df_filtered["nom_dept"] == dept]

    df_moyennes_city = (
        df_city.groupby(["nom_poll", df_city["date_debut"].dt.weekday])["valeur"]
        .mean()
        .reset_index()
    )
    df_moyennes_city.columns = ["nom_poll", "jour", "moyenne"]

    df_moyennes_city["jour_complet"] = df_moyennes_city["jour"].apply(
        lambda x: [
            "Lundi",
            "Mardi",
            "Mercredi",
            "Jeudi",
            "Vendredi",
            "Samedi",
            "Dimanche",
        ][x]
    )

    fig = px.line_polar(
        df_moyennes_city,
        r="moyenne",
        theta="jour_complet",
        color="nom_poll",
        line_close=True,
        range_r=[0, df_moyennes_city["moyenne"].max() + 10],
        start_angle=0,
        template="seaborn",
        title=f"Évolution des polluants sur toute la semaine à {dept}",
        labels={"jour": "weekday"},
    )

    for i, row in df_moyennes_city.iterrows():
        jour_text = f"{row['jour_complet']}"
        fig.add_annotation(
            x=row["jour"] * (360 // 7),
            y=row["moyenne"],
            text=jour_text,
            showarrow=False,
            font=dict(size=10),
            textangle=0,
        )

    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True),
            angularaxis=dict(
                tickmode="array",
                tickvals=list(range(7)),
                ticktext=[
                    "Lundi",
                    "Mardi",
                    "Mercredi",
                    "Jeudi",
                    "Vendredi",
                    "Samedi",
                    "Dimanche",
                ],
            ),
        )
    )

    fig.show()


def plot_polluant_evolution_annuelle(data_file, department, polluants):
    pd.options.mode.chained_assignment = None
    """Cette fonction prend en argument le fichier CSV, le département et la liste des polluants à afficher et affiche l'évolution de la concentration par station de chaque polluants"""
    # Charger les données
    df = pd.read_csv(data_file)
    df["valeur"].fillna(0, inplace=True)
    # Afficher la liste des polluants présents dans le DataFrame
    liste_polluants = df["nom_poll"].unique()

    # Boucle à travers les polluants pour créer les graphiques
    for polluant in polluants:
        # Filtrer les données pour le polluant et le département spécifiés
        filt = df[(df["nom_dept"] == department) & (df["nom_poll"] == polluant)]
        filt = filt.sort_values(by="date_debut")

        # Convertir la colonne de dates au format mois
        filt["date_debut"] = (
            pd.to_datetime(filt["date_debut"]).dt.to_period("M").astype(str)
        )

        # Créer un graphique interactif avec Plotly Express
        fig = px.scatter(
            filt,
            x="date_debut",
            y="valeur",
            color="nom_station",
            size="valeur",
            hover_name="date_debut",
            title=f"Évolution de la pollution {polluant} dans le {department}",
            labels={"valeur": f"Valeur {polluant} (ug.m-3)", "date_debut": "Année"},
        )

        # Ajouter des lignes reliant les points pour chaque station
        for nom_station in filt["nom_station"].unique():
            trace_data = filt[filt["nom_station"] == nom_station]
            fig.add_trace(
                go.Scatter(
                    x=trace_data["date_debut"],
                    y=trace_data["valeur"],
                    mode="lines",  
                    showlegend=False,
                )
            )
        fig.show()


# Villes


def create_polar_plot(ville):
    """Cette fonction prend en argumenet une ville et renvoie un polar graph qui représente l'évolution de la pollution au cours des heures de la journée"""
    pd.options.mode.chained_assignment = None

    # Chargement du CSV
    df = pd.read_csv("../Mesure_30j.csv")
    # Convertion en format datetime
    # chargez csv
    df = pd.read_csv(r'../data_visu/mensuelle.csv')
    # convert data

    df["date_debut"] = pd.to_datetime(df["date_debut"], format="%Y/%m/%d %H:%M:%S%z")
    # Liste des polluants à afficher
    polluants = ["NO2", "PM2.5", "PM10", "NOX", "NO"]
    # Trier le DataFrame par ordre croissant de date
    df = df.sort_values(by="date_debut")
    df_filtered = df[df["nom_poll"].isin(polluants)]
    df_ville = df_filtered[df_filtered["nom_com"] == ville]
    df_moyennes_ville = (
        df_ville.groupby(["nom_poll", df_ville["date_debut"].dt.hour])["valeur"]
        .mean()
        .reset_index()
    )
    df_moyennes_ville.columns = ["nom_poll", "heure", "moyenne"]

    fig_pol = px.line_polar(
        df_moyennes_ville,
        r="moyenne",
        theta=df_moyennes_ville["heure"] * (360 // 24),
        color="nom_poll",
        title=f"Évolution des polluants sur toutes les heures à {ville}",
    )

    fig_pol.update_polars(
        radialaxis=dict(
            visible=True,  
        ),
        angularaxis=dict(
            visible=True,  
            direction="clockwise",  
            period=360,  
            tickvals=np.arange(0, 360, 15),
            ticktext=[
                str(hour % 24) for hour in range(24)
<<<<<<< HEAD
            ],  
=======
            ], 
>>>>>>> ffbaaace580a5260a0f8414c6c50a543edf47c9d
        ),
    )
    fig_pol.show()


def afficher_evolution_pollution(nom_ville, chemin_fichier_csv, polluants):
    """Cette fonction prend en argument le nom de la ville, le chemin du fichier CSV et les listes des polluants que l'on souhaite afficher et renvoie un graphique pour chaque polluant"""
    pd.options.mode.chained_assignment = None

    # Chargez le fichier CSV dans un DataFrame pandas
    df = pd.read_csv(chemin_fichier_csv)

    # Convertir la colonne 'date_debut' en type datetime
    df["date_debut"] = pd.to_datetime(df["date_debut"], format="%Y/%m/%d %H:%M:%S%z")

    # Trier le DataFrame par ordre croissant de date
    df = df.sort_values(by="date_debut")

    # Afficher la liste des polluants présents dans le DataFrame
    liste_polluants = df["nom_poll"].unique()

    # Boucle à travers les polluants pour créer les graphiques
    for polluant in polluants:
        # Regrouper les données de la ville spécifiée
        filt_data = df[(df["nom_com"] == nom_ville) & (df["nom_poll"] == polluant)]
        filt_data = filt_data.sort_values(by="date_debut")
        filt_data = filt_data.dropna()

        # Création d'un graphique
        fig = px.scatter(
            filt_data,
            x="date_debut",
            y="valeur",
            color="nom_station",
            hover_name="date_debut",
            title=f"Évolution de la pollution {polluant} à {nom_ville}",
            labels={"valeur": f"Valeur {polluant} (ug.m-3)", "date_debut": "Année"},
        )

        # Relier les points pour chaque station
        for nom_station in filt_data["nom_station"].unique():
            trace_data = filt_data[filt_data["nom_station"] == nom_station]
            fig.add_trace(
                go.Scatter(
                    x=trace_data["date_debut"],
                    y=trace_data["valeur"],
                    mode="lines",
                    showlegend=False,
                )
            )
        fig.show()


def pollutants_evolution_ville(csv, polluants, ville):
    """Cette fonction prend en argument le nom de la ville, le chemin du fichier CSV et les listes des polluants que l'on souhaite afficher et renvoie un graphique polair qui représente l'évolution de la pollution au cours de la semaine """
    pd.options.mode.chained_assignment = None
    df = pd.read_csv(csv)

    df["date_debut"] = pd.to_datetime(df["date_debut"], format="%Y/%m/%d %H:%M:%S%z")
    df = df.sort_values(by="date_debut")

    df_filtered = df[df["nom_poll"].isin(polluants)]

    df_city = df_filtered[df_filtered["nom_com"] == ville]

    df_moyennes_city = (
        df_city.groupby(["nom_poll", df_city["date_debut"].dt.weekday])["valeur"]
        .mean()
        .reset_index()
    )
    df_moyennes_city.columns = ["nom_poll", "jour", "moyenne"]

    df_moyennes_city["jour_complet"] = df_moyennes_city["jour"].apply(
        lambda x: [
            "Lundi",
            "Mardi",
            "Mercredi",
            "Jeudi",
            "Vendredi",
            "Samedi",
            "Dimanche",
        ][x]
    )

    fig = px.line_polar(
        df_moyennes_city,
        r="moyenne",
        theta="jour_complet",
        color="nom_poll",
        line_close=True,
        range_r=[0, df_moyennes_city["moyenne"].max() + 10],
        start_angle=0,
        template="seaborn",
        title=f"Évolution des polluants sur toute la semaine à {ville}",
        labels={"jour": "weekday"},
    )

    for i, row in df_moyennes_city.iterrows():
        jour_text = f"{row['jour_complet']}"
        fig.add_annotation(
            x=row["jour"] * (360 // 7),
            y=row["moyenne"],
            text=jour_text,
            showarrow=False,
            font=dict(size=10),
            textangle=0,
        )

    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True),
            angularaxis=dict(
                tickmode="array",
                tickvals=list(range(7)),
                ticktext=[
                    "Lundi",
                    "Mardi",
                    "Mercredi",
                    "Jeudi",
                    "Vendredi",
                    "Samedi",
                    "Dimanche",
                ],
            ),
        )
    )

    fig.show()
    
def polar_plot_mensuelle(ville):  
    """Cette fonction prend en argument le nom de la ville que l'on souhaite afficher et renvoie un graphique polair représentant l'évolution de la pollution au cours de mois"""
    pd.options.mode.chained_assignment = None
    # Chargez le fichier CSV dans un DataFrame pandas
    chemin_fichier_csv = r'../data_visu/mensuelle.csv'
    df = pd.read_csv(chemin_fichier_csv)
    df = df.dropna()

    # Convertir la colonne 'date_debut' en type datetime
    df['date_debut'] = pd.to_datetime(df['date_debut'], format='%Y/%m/%d %H:%M:%S%z')

    # Extraire le mois de chaque date
    df['mois'] = df['date_debut'].dt.month

    # Trier le DataFrame par ordre croissant de date
    df = df.sort_values(by='mois')

    # Définir les polluants et la ville spécifiques
    polluants = ['PM10', 'NOX', 'O3', 'NO2', 'PM2.5', 'NO', 'SO2', 'H2S'] 
     

    # Filtrer les données pour inclure uniquement les polluants spécifiés
    df_filtered = df[df['nom_poll'].isin(polluants)]

    # Séparer les données pour la ville spécifiée
    df_ville = df_filtered[df_filtered['nom_com'] == ville]

    # Calculer la moyenne des concentrations de chaque polluant à chaque heure de la journée pour la ville spécifiée
    df_moyennes_ville = df_ville.groupby(['nom_poll', 'mois'])['valeur'].mean().reset_index()
    df_moyennes_ville.columns = ['nom_poll', 'mois', 'moyenne_valeur']

    # Créer un graphique polaire avec Plotly Express
    fig = px.line_polar(df_moyennes_ville, r='moyenne_valeur', theta=df_moyennes_ville['mois']*(360//12), line_close=True,
                        color='nom_poll', line_dash='nom_poll', title=f'Évolution des polluants par mois de {ville}')
    liste_des_mois = ["Décembre","Janvier","Février", "Mars","Avril","Mai","Juin","Juillet","Août","Septembre","Octobre","Novembre"]
    fig.update_polars(
        radialaxis=dict(
<<<<<<< HEAD
            visible=False,  
=======
            visible=False, 
>>>>>>> ffbaaace580a5260a0f8414c6c50a543edf47c9d
        ),
        angularaxis=dict(
            visible=True,  
            rotation=120,   
            direction='clockwise',  
            period=360,   
            tickvals=np.arange(0, 360, 30),
            ticktext=[i for i in liste_des_mois],  
        )
    )
    # Afficher le graphique
    fig.show()
