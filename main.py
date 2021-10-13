from flask import Flask, render_template
import requests,json
import tmdb_client
import random
app = Flask(__name__)


@app.route('/')
def homepage():
#__Użycie funkcji get_movie_info do zbudowania słownika zawierającego_____#
#__tytuł i URL do plakatu dla każdego filmu, który będziemy wyświetlać____#
   # ver 1. movies = tmdb_client.get_popular_movies()["results"][:8]
     movies = tmdb_client.get_movies(how_many=8)
     return render_template("homepage.html", movies=movies)
    
#_________________________________________________________________________#
###___każdy szablon będzie miał dostępny obiekt o nazwie tmdb_image_url___#
###___czyli funkcję, która przyjmuje dwa parametry: path oraz size________#
@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}
###_______________________________________________________________________#

@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    details = tmdb_client.get_single_movie(movie_id)
   
    movie_images = tmdb_client.get_movie_images(movie_id)
    
    return render_template("movie_details.html", movie=details, selected_backdrop= movie_images)




if __name__ == '__main__':
    app.run(debug=True)