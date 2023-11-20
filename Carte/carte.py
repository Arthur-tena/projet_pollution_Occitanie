import folium
from folium import plugins

# Création de la carte centrée sur l'Occitanie
occitanie_map = folium.Map(location=[43.9339, 2.6322], zoom_start=7)

# Ajout d'un fond de carte (CartoDB positron)
folium.TileLayer("CartoDB positron", name="Light Map", control=False).add_to(occitanie_map)

# Charger les données GeoJSON pour l'Occitanie (remplacez "occitanie.geojson" par le chemin de votre fichier)
occitanie_geojson_path = "occitanie.geojson"
occitanie_data = folium.GeoJson(
    data=occitanie_geojson_path,
    style_function=lambda x: {
        "color": "blue",  # Couleur de la frontière
        "fillColor": "yellow",  # Couleur de remplissage
        "fillOpacity": 0.5,
        "weight": 1,
    },
    highlight_function=lambda x: {"weight": 3, "fillOpacity": 0.7},
    tooltip=folium.features.GeoJsonTooltip(fields=["nom"], aliases=["Region: "], localize=True),
    name="Occitanie",
).add_to(occitanie_map)

# Ajout du contrôle des couches
folium.LayerControl().add_to(occitanie_map)

# Enregistrement de la carte sous forme de fichier HTML
occitanie_map.save('occitanie_map.html')


template = """
{% macro html(this, kwargs) %}

<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>jQuery UI Draggable - Default functionality</title>
  <link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">

  <script src="https://code.jquery.com/jquery-1.12.4.js"></script>
  <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
  
  <script>
  $( function() {
    $( "#maplegend" ).draggable({
                    start: function (event, ui) {
                        $(this).css({
                            right: "auto",
                            top: "auto",
                            bottom: "auto"
                        });
                    }
                });
});

  </script>
</head>
<body>

 
<div id='maplegend' class='maplegend' 
    style='position: absolute; z-index:9999; border:2px solid grey; background-color:rgba(255, 255, 255, 0.8);
     border-radius:6px; padding: 10px; font-size:14px; right: 20px; bottom: 20px;'>
     
<div class='legend-title'>Nbr Fleurs Communes <br> IDF 2020 </div>
<div class='legend-scale'>
  <ul class='legend-labels'>
    <li><span style='background:#f6eff7;opacity:0.7;'></span>0</li>
    <li><span style='background:#bdc9e1;opacity:0.7;'></span>1</li>
    <li><span style='background:#67a9cf;opacity:0.7;'></span>2</li>
    <li><span style='background:#1c9099;opacity:0.7;'></span>3</li>
    <li><span style='background:#016c59;opacity:0.7;'></span>4</li>

  </ul>
</div>
</div>
 
</body>
</html>

<style type='text/css'>
  .maplegend .legend-title {
    text-align: center;
    margin-bottom: 5px;
    font-weight: bold;
    font-size: 90%;
    }
  .maplegend .legend-scale ul {
    margin: 0;
    margin-bottom: 5px;
    padding: 0;
    float: left;
    list-style: none;
    }
  .maplegend .legend-scale ul li {
    font-size: 80%;
    list-style: none;
    margin-left: 0;
    line-height: 18px;
    margin-bottom: 2px;
    }
  .maplegend ul.legend-labels li span {
    display: block;
    float: left;
    height: 16px;
    width: 30px;
    margin-right: 5px;
    margin-left: 0;
    border: 1px solid #999;
    }
  .maplegend .legend-source {
    font-size: 80%;
    color: #777;
    clear: both;
    }
  .maplegend a {
    color: #777;
    }
</style>
{% endmacro %}"""

macro = MacroElement()
macro._template = Template(template)

m.get_root().add_child(macro)
m.save("index.html")