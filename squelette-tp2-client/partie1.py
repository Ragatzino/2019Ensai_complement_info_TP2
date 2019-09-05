import requests
from tabulate import tabulate
import properties

if __name__ == '__main__':

    try:

        proxies = {
            'http': properties.http_proxy,
            'https': properties.https_proxy
        }

        # On prépare les params de la requête. On définit les différents paramètres
        params = {'apikey': properties.api_key,
                  'dataset': "equipement-accessibilite-arrets-bus",
                  'facet': 'equip_mobilier',
                  'facet': 'equip_banc',
                  'facet': 'equip_eclairage',
                  'facet': 'equip_poubelle',
                  'facet': 'access_pmr',
                  'facet': 'nomcommune',
                  'refine.nomcommune': 'Bruz',
                  "rows": 100}

        # On effectue une requête http get sur le serveur
        response = requests.get(
            'https://data.rennesmetropole.fr/api/records/1.0/search/',
            params = params,
            proxies=proxies)

        # Une exception est envoyée si le status de la réponse indique une erreur
        response.raise_for_status()

        # On récupère la réponse au format json, et dans cette réponse le tableau de résultats (records)
        arrets = response.json()['records']

        # On filtre sur les film qui contiennent le mot "Star Wars" et on récupére les titres et nombres de prêts
        arretsPMROK = [{'Latitude': arret['fields']['coordonnees'][0], 'Longitude': arret['fields']['coordonnees'][1]}
                       for arret in arrets if
                       'access_pmr' in arret['fields'] and 'OUI' == arret['fields']['access_pmr']]

        # On affiche le résultat sous forme de tableau avec tabulate
        print(tabulate(arretsPMROK, headers="keys", tablefmt='grid'))

    except requests.exceptions.RequestException as error:
        print(error)
