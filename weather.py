import requests
import json
import matplotlib.pyplot as plt
from datetime import datetime

# Remplacez l'URL par votre URL réelle
url = "https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/donnees-synop-essentielles-omm/records?limit=20&refine=nom_reg%3A%22Occitanie%22"

# Effectuer la requête HTTP
response = requests.get(url)

# Gérer les erreurs
if response.status_code == 200:
    # Charger les données JSON
    weather_data = response.json()

    # Préparer les données pour le graphique
    months_data = {i: {"sunshine_hours": [], "temperature": []} for i in range(1, 13) if i not in [11, 12]}

    for result in weather_data["results"]:
        # Convertir la date au format datetime
        date = datetime.fromisoformat(result["date"].split("+")[0])

        month = date.month

        # Exclure les mois 11 et 12
        if month not in [11, 12]:
            sunshine_hours = result["vv"] / 3600  # vv est en secondes, convertir en heures
            temperature = result["t"] - 273.15  # Convertir la température de Kelvin à Celsius

            # Accumuler les heures d'ensoleillement et les températures pour chaque mois
            months_data[month]["sunshine_hours"].append(sunshine_hours)
            months_data[month]["temperature"].append(temperature)

    # Calculer les moyennes pour chaque mois
    average_sunshine_hours = [sum(data["sunshine_hours"]) / len(data["sunshine_hours"]) if data["sunshine_hours"] else 0 for data in months_data.values()]
    average_temperature = [sum(data["temperature"]) / len(data["temperature"]) if data["temperature"] else 0 for data in months_data.values()]

    # Créer le graphique avec deux ordonnées (deuxième axe Y)
    fig, ax1 = plt.subplots(figsize=(10, 6))

    ax1.set_xlabel("Mois de l'année")
    ax1.set_ylabel("Ensoleillement (heures)", color='tab:blue')
    ax1.plot(range(1, 11), average_sunshine_hours, marker='o', linestyle='-', color='tab:blue', label="Ensoleillement")
    ax1.tick_params(axis='y', labelcolor='tab:blue')

    ax2 = ax1.twinx()
    ax2.set_ylabel("Température (°C)", color='tab:red')
    ax2.plot(range(1, 11), average_temperature, marker='o', linestyle='-', color='tab:red', label="Température")
    ax2.tick_params(axis='y', labelcolor='tab:red')

    fig.tight_layout()

    # Ajouter les numéros de chaque mois en bas du graphique
    plt.xticks(range(1, 11), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct'])

    plt.title("Moyenne de la quantité d'ensoleillement et de la température par mois (mois 11 et 12 exclus)")
    plt.show()
else:
    print(f"Échec de la requête avec le code d'état {response.status_code}")
    print(response.text)  # Affiche le contenu de la réponse pour déboguer