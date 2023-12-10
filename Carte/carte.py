import os
import pandas as pd

class Load_datasets:
    def __init__(self, path_csv='../data/Mesure_horaire.csv'):
        """
        """
        self.path_csv = path_csv

    def charge_data(self):
        """
        """
        data_path = os.path.join(os.getcwd(), self.path_csv)
        df = pd.read_csv(data_path,usecols=["X","Y",'nom_com',"nom_poll","valeur"])

        return df
    
    def YX_polluant(self, nom_polluant):
        """
        """
        df = self.charge_data()
        get_poll = df[df['nom_poll'] == str(nom_polluant)]['valeur'].tolist()
        # Longitude de chaque zone
        long = df["X"].unique().tolist()
        # Latittude de chaque zone
        lat = df["Y"].unique().tolist()
        Liste_final = list(zip(lat,long,get_poll))
        return Liste_final