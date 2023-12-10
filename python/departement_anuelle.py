import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

pd.options.mode.chained_assignment = None


def plot_pollutant_evolution(data_file, department, polluants):
    # Charger les données
    df = pd.read_csv(data_file)
    df["valeur"].fillna(0, inplace=True)
    # Afficher la liste des polluants présents dans le DataFrame
    liste_polluants = df["nom_poll"].unique()
    print("Liste des polluants :", liste_polluants)

    # Boucle à travers les polluants pour créer les graphiques
    for polluant in polluants:
        # Filtrer les données pour le polluant et le département spécifiés
        filt = df[(df["nom_dept"] == department) & (df["nom_poll"] == polluant)]
        filt = filt.sort_values(by="date_debut")

        # Convertir la colonne de dates au format mois-année
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
                    mode="lines",  # Ajout de ligne pour relier les points
                    showlegend=False,
                )
            )
        fig.show()


# Exemple d'utilisation de la fonction
data_file_path = r"c:\Users\aicha\Downloads\Mesure_annuelle.csv"
department_name = "HAUTE-GARONNE"
polluants_list = ["NO", "NOX", "O3", "PM10", "NO2", "PM2.5"]

# Pour le tarn pas d'affichage de PM2.5 pas de données
# Pour le GARD pas de NO et de NOX

plot_pollutant_evolution(data_file_path, department_name, polluants_list)
