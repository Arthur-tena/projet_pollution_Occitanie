import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data=pd.read_csv("/Users/arthurtena/Documents/data/Mesure_annuelle_Region_Occitanie_Polluants_Principaux.csv")
df=pd.DataFrame(data)
columns_to_drop=['code_station','typologie','influence','id_poll_ue', 'unite', 'metrique', 'date_fin', 'statut_valid' ]