import folium
import geopandas as gpd

# Charger le fichier GeoJSON pour les contours de l'Occitanie
occitanie_geojson = gpd.read_file('Carte/Data_Carte/departements-d-occitanie.geojson')

# Projeter les données dans le système de coordonnées latitudes/longitudes (EPSG:4326)
occitanie_geojson = occitanie_geojson.to_crs(epsg=4326)

# Créer une carte centrée sur l'Occitanie
latitude, longitude = 43.648785, 2.343568
carte = folium.Map(location=[latitude, longitude], zoom_start=8)

# Ajouter les contours de l'Occitanie à la carte
folium.GeoJson(occitanie_geojson).add_to(carte)

# Enregistrer la carte au format HTML
carte.save("ma_carte_occitanie.html")

# Afficher la carte dans le navigateur (facultatif)
carte
