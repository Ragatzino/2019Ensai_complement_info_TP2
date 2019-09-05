import csv
from business_object.movie import Movie


class MovieDao:
    MOVIE_FILE = 'files/movies.csv'
    TITLE_HEADER = 'title'
    REVIEW_HEADER = 'review'

    def find_all(self):
        with open(self.MOVIE_FILE, 'r', encoding="utf-8") as csv_file:
            csvreader = csv.reader(csv_file, delimiter=';', quotechar="'")
            # tableau de résultat
            result = []
            # les clés qui vont nous servir à créer nos dictionnaires
            keys = None
            for row in csvreader:
                print(row)
                # la première ligne va servir pour les clés de nos dictionnaires pythons
                if not (keys):
                    keys = row
                else:
                    # on transforme les lignes suivantes en dictionnaire
                    dictionnary = dict(zip(keys, row))
                    # on l’ajoute au tableau
                    result.append(Movie(dictionnary[self.TITLE_HEADER], dictionnary[self.REVIEW_HEADER]))
                    print(result)
        return result

    def add(self, movie):
        with open(self.MOVIE_FILE, 'a', encoding="utf-8", newline='') as csv_file:
            if movie.title:
                csv_file.write(movie.title +";" + movie.review +  "\n" )
