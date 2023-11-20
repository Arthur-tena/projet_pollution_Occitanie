import pygal_maps_fr

# Créer une carte de la France
france_map = pygal_maps_fr.Regions()

# Ajouter la région Occitanie avec une couleur spécifique
france_map.add('Occitanie', ['mpl', 'lrr', 'lr', 'ar', 'hp', 'av', 'gm', 'ta'], colors=['#00FF00'])

# Enregistrer la carte dans un fichier SVG
france_map.render_to_file('carte_occitanie.svg')