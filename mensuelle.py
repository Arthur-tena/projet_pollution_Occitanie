import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

def pollutants_evolution_ville(csv, polluants, ville):
    df = pd.read_csv(csv)

    df['date_debut'] = pd.to_datetime(df['date_debut'], format='%Y/%m/%d %H:%M:%S%z')
    df = df.sort_values(by='date_debut')
    couleurs = ['blue', 'red', 'green', 'purple', 'orange', 'pink', 'brown']

    df_filtered = df[df['nom_poll'].isin(polluants)]

    df_city = df_filtered[df_filtered['nom_com'] == ville]

    df_moyennes_city = df_city.groupby(['nom_poll', df_city['date_debut'].dt.weekday])['valeur'].mean().reset_index()
    df_moyennes_city.columns = ['nom_poll', 'jour', 'moyenne']


    df_moyennes_city['jour_complet'] = df_moyennes_city['jour'].apply(lambda x: ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche'][x])

    fig = px.line_polar(
        df_moyennes_city,
        r="moyenne",
        theta="jour_complet",
        color="nom_poll",
        line_close=True,
        range_r=[0, df_moyennes_city['moyenne'].max() + 10],
        start_angle=0,
        template="seaborn",
        title=f"Évolution des polluants sur toute la semaine à {ville}",
        labels={"jour": "weekday"}
    )

    for i, row in df_moyennes_city.iterrows():
        jour_text = f"{row['jour_complet']}"
        fig.add_annotation(
            x=row['jour'] * (360 // 7),
            y=row['moyenne'],
            text=jour_text,
            showarrow=False,
            font=dict(size=10),
            textangle=0
        )

    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True),
            angularaxis=dict(
                tickmode='array',
                tickvals=list(range(7)),
                ticktext=["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
            )
        )
    )


    fig.show()
pollutants_evolution_ville("/Users/arthurtena/Downloads/Mesure_horaire_(30j)_Region_Occitanie_Polluants_Reglementaires.csv", ['NO2', 'PM2.5', 'PM10', 'NOX', 'NO'],"MONTPELLIER")
pollutants_evolution_ville("/Users/arthurtena/Downloads/Mesure_horaire_(30j)_Region_Occitanie_Polluants_Reglementaires.csv", ['NO2', 'PM2.5', 'PM10', 'NOX', 'NO'],"TOULOUSE")





def plot_pie(department):
    data = pd.read_csv("/Users/arthurtena/Documents/data/Mesure_annuelle_Region_Occitanie_Polluants_Principaux.csv")
    df = pd.DataFrame(data)
    columns_to_drop = ['code_station', 'typologie', 'influence', 'id_poll_ue', 'unite', 'metrique', 'date_fin', 'statut_valid']
    df = df.drop(columns=columns_to_drop)

    df_department = df[df['nom_dept'] == department]

    if df_department.empty:
        print(f"Aucune donnée disponible pour le département {department}.")
        return

    df_department = df_department.dropna()
    df_department = df_department.groupby('nom_poll')['valeur'].sum().reset_index()

    name = df_department['nom_poll']
    value = df_department['valeur']

    plt.figure(figsize=(6, 6))
    plt.pie(value, labels=name, autopct='%1.1f%%', startangle=90, shadow=True)
    plt.axis('equal')
    plt.title(f"Répartition des polluants pour le département {department}")
    plt.show()

plot_pie("ARIEGE")



import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
def pollutants_evolution_dept(csv, polluants, dept):
    df = pd.read_csv(csv)

    df['date_debut'] = pd.to_datetime(df['date_debut'], format='%Y/%m/%d %H:%M:%S%z')
    df = df.sort_values(by='date_debut')
    couleurs = ['blue', 'red', 'green', 'purple', 'orange', 'pink', 'brown']

    df_filtered = df[df['nom_poll'].isin(polluants)]

    df_city = df_filtered[df_filtered['nom_dept'] == dept]

    df_moyennes_city = df_city.groupby(['nom_poll', df_city['date_debut'].dt.weekday])['valeur'].mean().reset_index()
    df_moyennes_city.columns = ['nom_poll', 'jour', 'moyenne']


    df_moyennes_city['jour_complet'] = df_moyennes_city['jour'].apply(lambda x: ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche'][x])

    fig = px.line_polar(
        df_moyennes_city,
        r="moyenne",
        theta="jour_complet",
        color="nom_poll",
        line_close=True,
        range_r=[0, df_moyennes_city['moyenne'].max() + 10],
        start_angle=0,
        template="seaborn",
        title=f"Évolution des polluants sur toute la semaine à {dept}",
        labels={"jour": "weekday"}
    )

    for i, row in df_moyennes_city.iterrows():
        jour_text = f"{row['jour_complet']}"
        fig.add_annotation(
            x=row['jour'] * (360 // 7),
            y=row['moyenne'],
            text=jour_text,
            showarrow=False,
            font=dict(size=10),
            textangle=0
        )

    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True),
            angularaxis=dict(
                tickmode='array',
                tickvals=list(range(7)),
                ticktext=["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
            )
        )
    )


    fig.show()