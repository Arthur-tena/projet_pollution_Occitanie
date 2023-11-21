import pygal


Occ_map = pygal.maps.fr.Regions()

# Ajouter la région Occitanie avec une couleur spécifique
Occ_map.add('Occitanie', ['mpl', 'lrr', 'lr', 'ar', 'hp', 'av', 'gm', 'ta'], colors=['#00FF00'])

# Enregistrer la carte dans un fichier SVG
Occ_map.render_to_file('carte_occitanie.svg')
