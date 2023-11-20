import pygal_maps_fr

# Créer une carte de la France
france_map = pygal_maps_fr.Regions()

# Ajouter la région Occitanie avec une couleur spécifique
france_map.add('Occitanie', ['mpl', 'lrr', 'lr', 'ar', 'hp', 'av', 'gm', 'ta'], colors=['#00FF00'])

# Enregistrer la carte dans un fichier SVG
france_map.render_to_file('carte_occitanie.svg')


import pygal  # First import pygal

# from pygal.maps.fr import aggregate_regions


def plot_location(gd):
    fr_chart = pygal.maps.fr.Departments(human_readable=True)
    fr_chart.title = "Accident by region"

    fr_chart.add("Accidents", gd.to_dict())

    fr_chart.render_in_browser()
    # fr_chart.render_to_file('./chart.svg')  # Write the chart in the specified file