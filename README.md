# PROJET: Pollution en Occitanie

# Formulation du problème 

La pollution de l'air est devenue une préoccupation majeure dans notre société. Notre objectif est d'exploiter des données mises à disposition par l'API afin de fournir des informations aux utilisateurs de notre site web de manière interactive, en offrant un aperçu de la situation actuelle de la pollution en Occitanie. À l'aide notamment, d'analyse en temps réel et d'une carte interactive qui résume l'état de la pollution dans la région.

# Données utilisées

On  a utilisé les données mises à notre disposition par le site [data_atmo-occitanie](https://data-atmo-occitanie.opendata.arcgis.com/) afin de pouvoir offrir l'aperçu le plus complet possible sur la situation écologique de la région Occitanie au cours de ces dernières années.

# Architecture du site 

## Approche Géographique

Nous avons finalement décidé d'avoir une approche géographique dans la structure de notre site. En effet, la page d'accueil et la carte offrent un aperçu de la pollution en Occitanie. Alors que la section **Visiualisation** des données regroupent tout d'abord les départements ( à noter que les départements de la Lozère, le Lot et l'Aude ne sont pas représentés par manque de données), puis nous avons choisi de nous intéresser à plusieurs villes (Toulouse , Montpellier, Nîmes , Perpignan , Albi et enfin Rodez).

## Approche Temporelle

Puis, dans chaque catégorie, l'objectif était là aussi de rétrécir au fur et à mesure l'intervalle de temps. Dans la catégorie **Département** , nous avons commencé par nous intéresser à l'échelle anuelle et hebdomadaire, alors que dans la catégorie **Ville** nous avons commencé par traiter les données à l'échelle anuelle, mensuelle, hebdomadaire et enfin journalière.

# Récupération des données 

Dans un premier, nous avons essayé de récupérer les données à l'aide d'une URL qui nous permettaient d'extraire les données souhaitées au format JSON . Néanmoins, nous avons très vite été confronter à un problème, le nombre de données récupérees par l'URL se limite à 1000. Par conséquent, nous avions une perte de données trés importantes. 

Nous avons donc décidé de télécharger les CSV les plus récentes mises à notre disposition.

## Création de fonction

Afin de pouvoir récupérer les données et les visualiser, notre objectif était de créé des fonctions capables dans un premier temps d'extraire les données du fichier CSV à étudier, puis d'afficher les données qu'on voulait visualiser.
Par exemple , pour l'étude des départements et des villes, nous avons créé une fonction qui prenait en argument le fichier CSV que l'ont souhaité étudier, le département ou la ville a étudié ainsi que la liste des polluants à afficher qui a été adapté aux données que l'on pouvait obtenir pour chaque département et ville que l'ont souhaité approfondir.

## Création d'un module

L'étape suivante a été de regrouper toutes les fonctions créées afin de pouvoir les appeler et les éxécuter dans chaque fichier **Quarto** souhaités. 