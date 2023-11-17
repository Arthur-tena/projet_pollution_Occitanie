import pygal_maps_fr
from pygal_maps_fr import Regions
from pygal.style import LightColorizedStyle

# Créer une carte de l'Occitanie
occitanie_map = pygal_maps_fr.Regions(style=LightColorizedStyle)
occitanie_map.title = 'Carte de l\'Occitanie'

# Ajouter la région Occitanie
occitanie_map.add('Occitanie', ['oc'])

# Enregistrer la carte dans un fichier (optionnel)
#occitanie_map.render_to_file('carte_occitanie.svg')

# Afficher la carte dans une fenêtre (optionnel)
occitanie_map.render_in_browser()
