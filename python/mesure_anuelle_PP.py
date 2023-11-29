import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data=pd.read_csv("/Users/arthurtena/Documents/data/Mesure_annuelle_Region_Occitanie_Polluants_Principaux.csv")
df=pd.DataFrame(data)
columns_to_drop=['code_station','typologie','influence','id_poll_ue', 'unite', 'metrique', 'date_fin', 'statut_valid' ]
df=df.drop(columns=columns_to_drop)
print(df)

# %%
data=pd.read_csv("/Users/arthurtena/Documents/data/Mesure_annuelle_Region_Occitanie_Polluants_Principaux.csv")
df=pd.DataFrame(data)
columns_to_drop=['code_station','typologie','influence','id_poll_ue', 'unite', 'metrique', 'date_fin', 'statut_valid' ]
df=df.drop(columns=columns_to_drop)
df['date_debut'] = pd.to_datetime(df['date_debut'])
df['date_debut'] = df['date_debut'].dt.year
df_departements = {}
for dept, group in df.groupby('nom_dept'):
 df_departements[dept] = group
 for dept, df_dept in df_departements.items():
     print(f"\nDataFrame pour le département {dept} :")
     print(df_dept)

num_cols = 4
num_rows=3
fig, axes = plt.subplots(nrows=num_rows, ncols=num_cols, figsize=(10, 3*num_rows))
for i, (dept, df_dept) in enumerate(df_departements.items()):
    df_dept = df_dept.dropna()
    
    df_dept = df_dept.groupby('nom_poll')['valeur'].sum().reset_index()

    name = df_dept['nom_poll']
    value = df_dept['valeur']

    row = i // num_cols
    col = i % num_cols

    ax = axes[row, col]
    ax.pie(value, labels=name, autopct='%1.1f%%', startangle=90, shadow=True)
    ax.axis('equal')
    ax.set_title(f"Répartition des polluants - {dept}")
plt.tight_layout()

plt.show()


#O3=Ozone est formé à partir de réaction chimiqe entre les oxyde d'azote (NOx) et les composés organiques volatile (COV) sous l'effet du soleil
#Il s'agit d'un polluant secondaire car n'est pas émis directement dans l'air (Ecologie.gouv)


# %%
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("/Users/arthurtena/Documents/data/Mesure_annuelle_Region_Occitanie_Polluants_Principaux.csv")
df = pd.DataFrame(data)

columns_to_drop = ['code_station', 'typologie', 'influence', 'id_poll_ue', 'unite', 'metrique', 'date_fin', 'statut_valid']
df = df.drop(columns=columns_to_drop)
grouped_df = df.groupby(['date_debut', 'nom_poll'])['valeur'].sum().reset_index()
grouped_df = grouped_df.sort_values(by=['date_debut', 'nom_poll'])
grouped_df['date_debut'] = pd.to_datetime(grouped_df['date_debut'])
grouped_df['date_debut'] = grouped_df['date_debut'].dt.year
plt.figure(figsize=(12, 8))
colors = plt.cm.get_cmap('tab10', len(grouped_df['nom_poll'].unique()))
bar_width = 0.2
bar_spacing = 0.1
year_indexes = {year: i for i, year in enumerate(grouped_df['date_debut'].unique())}
for polluant, color in zip(grouped_df['nom_poll'].unique(), colors.colors):
    plt.bar(
        [year_indexes[annee] + j * (bar_width + bar_spacing) for j, annee in enumerate(grouped_df['date_debut'].unique())],
        grouped_df[grouped_df['nom_poll'] == polluant]['valeur'],
        width=bar_width,
        label=polluant,
        color=color
    )
plt.xlabel('Année')
plt.ylabel('Somme des valeurs')
plt.title('Valeurs des principaux polluants par année')
plt.legend(title='Polluant', bbox_to_anchor=(1, 1))
plt.xticks([i for i in range(len(grouped_df['date_debut'].unique()))], grouped_df['date_debut'].unique())

plt.show()
# %%
#crée un graphique qui montre l'évolution des polluants années après années avec des lignes 
import pandas as pd
import plotly.graph_objects as go
import numpy as np

data = pd.read_csv("/Users/arthurtena/Documents/data/Mesure_annuelle_Region_Occitanie_Polluants_Principaux.csv")
df = pd.DataFrame(data)
columns_to_drop = ['code_station', 'typologie', 'influence', 'id_poll_ue', 'unite', 'metrique', 'date_fin', 'statut_valid']
df = df.drop(columns=columns_to_drop)
grouped_df = df.groupby(['date_debut', 'nom_poll'])['valeur'].sum().reset_index()
grouped_df = grouped_df.sort_values(by=['date_debut', 'nom_poll'])
grouped_df['date_debut'] = pd.to_datetime(grouped_df['date_debut'])
grouped_df['date_debut'] = grouped_df['date_debut'].dt.year

fig = go.FigureWidget()
polluants = sorted(df["nom_poll"].unique())
for polluant in polluants:
    trace_data = grouped_df[grouped_df["nom_poll"] == polluant]
    fig.add_trace(
        go.Scatter(
            x=trace_data["date_debut"],
            y=trace_data["valeur"],
            mode='lines',
            name=f"Polluant = {polluant}",
        )
    )
fig.update_layout(
    template="simple_white",
    title="Polluants en fonction de l'année",
    showlegend=True,
    xaxis_title="Polluants",
    yaxis_title="Fréquence normalisée",
)


fig.show()


# %%
import pandas as pd
import plotly.graph_objects as go
import numpy as np

data = pd.read_csv("/Users/arthurtena/Documents/data/Mesure_annuelle_Region_Occitanie_Polluants_Principaux.csv")
df = pd.DataFrame(data)
columns_to_drop = ['code_station', 'typologie', 'influence', 'id_poll_ue', 'unite', 'metrique', 'date_fin', 'statut_valid']
df = df.drop(columns=columns_to_drop)
grouped_df = df.groupby(['date_debut', 'nom_poll'])['valeur'].sum().reset_index()
grouped_df = grouped_df.sort_values(by=['date_debut', 'nom_poll'])
grouped_df['date_debut'] = pd.to_datetime(grouped_df['date_debut'])
grouped_df['date_debut'] = grouped_df['date_debut'].dt.year

fig = go.FigureWidget()

polluants = sorted(df["nom_poll"].unique())
for polluant in polluants:
    trace_data = grouped_df[grouped_df["nom_poll"] == polluant]
    fig.add_trace(
        go.Scatter(
            x=trace_data["date_debut"],
            y=trace_data["valeur"],
            mode='lines',
            name=f"Polluant = {polluant}",
        )
    )

fig.update_layout(
    template="simple_white",
    title="Polluants en fonction de l'année",
    showlegend=True,
    xaxis_title="Année",
    yaxis_title="Fréquence normalisée",
)

fig.show()

# %%
