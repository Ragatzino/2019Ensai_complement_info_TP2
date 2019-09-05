from flask import Flask, request
import json

from DAO.movie_dao import MovieDao
from business_object.movie import Movie

app = Flask(__name__)


@app.route("/films", methods=['GET'])
def movieList():
    """
    Permet de récupérer tous les films sauvegardés
    :return: la liste des films sous forme json
    """
    movie_dao = MovieDao()

    # On met transforme les données en json avant de les retouner
    return json.dumps({"movies": [movie.__dict__ for movie in movie_dao.find_all()] })


@app.route("/film", methods=['POST'])
def addMovie():
    """
    Ajoute une film dans le fichier.
    :return: {"result" : "success"} si aucune erreur ne s'est produite
    """
    content = request.get_json()
    movie_to_add = Movie(content["title"])
    movie_dao = MovieDao()
    movie_dao.add(movie_to_add)

    return json.dumps({"result": "success"})


if __name__ == "__main__":
    app.run()
