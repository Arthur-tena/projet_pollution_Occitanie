def create_polar_plot(ville):
    # chargez csv
    df = pd.read_csv("/home/zack/gprojet_pollution_occitanie/Mesure_30j.csv")
    # convert data
    df["date_debut"] = pd.to_datetime(df["date_debut"], format="%Y/%m/%d %H:%M:%S%z")
    # polluants
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
            visible=True,  # Set to False if you want to hide the radial axis
        ),
        angularaxis=dict(
            visible=True,  # Set to False if you want to hide the angular axis
            direction="clockwise",  # Set the direction of the angular axis
            period=360,  # Set the period of the angular axis
            tickvals=np.arange(0, 360, 15),
            ticktext=[
                str(hour % 24) for hour in range(24)
            ],  # Specify tick values on the angular axis
        ),
    )
    fig_pol.show()
