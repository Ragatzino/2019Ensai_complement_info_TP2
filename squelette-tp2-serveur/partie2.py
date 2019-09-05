from flask import Flask, request
import json

app = Flask(__name__)


joueurs = []


@app.route("/joueurs", methods=['GET'])
def joueurList():
    return json.dumps({"joueurs": joueurs})


@app.route("/joueur", methods=['POST'])
def addJoueur():
    content = request.get_json()
    joueurs.append(content)
    return json.dumps({"result": "success"})


if __name__ == "__main__":
    app.run()
