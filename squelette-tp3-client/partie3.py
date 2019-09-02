import requests
from tabulate import tabulate
from operator import itemgetter

if __name__ == '__main__':

    try:
        # On envoie une requête pour ajouter un joueur
        response = requests.post(
            'http://localhost:5000/joueur', json={'pseudonyme': 'biggy', 'score': 50})

        # Une exception est envoyée si le status de la réponse indique une erreur
        response.raise_for_status()

        response = requests.post(
            'http://localhost:5000/joueur', json={'pseudonyme': 'woupy', 'score': 60})

        # Une exception est envoyée si le status de la réponse indique une erreur
        response.raise_for_status()

        response = requests.post(
            'http://localhost:5000/joueur', json={'pseudonyme': 'caly', 'score': 55})

        # Une exception est envoyée si le status de la réponse indique une erreur
        response.raise_for_status()

        response = requests.post(
            'http://localhost:5000/joueur', json={'pseudonyme': 'sorry', 'score': 70})

        # Une exception est envoyée si le status de la réponse indique une erreur
        response.raise_for_status()

        response = requests.get('http://localhost:5000/joueurs')

        print(response.json()['joueurs'])

        finish = sorted(response.json()['joueurs'],
                        key=itemgetter('score'), reverse=True)

        # On affiche le résultat sous forme de tableau avec tabulate
        print(tabulate(finish[0:3], headers="keys", tablefmt='grid'))

    except requests.exceptions.RequestException as error:
        print(error)
