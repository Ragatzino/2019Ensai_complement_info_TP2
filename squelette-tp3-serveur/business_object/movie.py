
class Movie:
    """
    Représente un film
    title : le titre d'un film
    review : avis sur le film. Seul l'admin du site peut ajouter cette info
    """

    def __init__(self, title, review=''):
        self.title = title
        self.review = review


    def __repr__(self):
        return "Titre : %s, Review %s" % (self.title, self.review)

