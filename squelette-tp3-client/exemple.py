import requests
from tabulate import tabulate
import properties

URL_EXEMPLE = "https://data.rennesmetropole.fr/api/records/1.0/search/?dataset=statistiques-de-prets-de-dvd-en-2017-cesson-sevigne&rows=1000&apikey=VOTRE_API_KEY"

if __name__ == '__main__':

    try:

        proxies = {
            'http': properties.http_proxy,
            'https': properties.https_proxy
        }

        # On prépare les params de la requête. C'est requests qui va les mettre en forme pour nous !
        params = {'apikey': properties.api_key,
                  'dataset': "statistiques-de-prets-de-dvd-en-2017-cesson-sevigne",
                  "rows": 1000}

        # On envoie une requête poru récupérer les statistiques d'emprunt de films
        response = requests.get(
            'https://data.rennesmetropole.fr/api/records/1.0/search/'
            , proxies=proxies
            , params=params)

        # Une exception est envoyée si le status de la réponse indique une erreur
        response.raise_for_status()

        # On récupère la réponse au format json, et dans cette réponse le tableau de résultats (records)
        movies = response.json()['records']

        # On filtre sur les film qui contiennent le mot "Star Wars" et on récupére les titres et nombres de prêts
        starWarsMovies = [
            {'Titre': movie['fields']['titre'], 'Nombre de prets en 2017': movie['fields']['nombre_de_prets_2017']}
            for movie in movies if 'Star Wars' in movie['fields']['titre']]

        # On affiche le résultat sous forme de tableau avec tabulate
        print(tabulate(starWarsMovies, headers="keys", tablefmt='grid'))

    except requests.exceptions.RequestException as error:
        print(error)
