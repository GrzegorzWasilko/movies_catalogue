import requests, random
API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhNGY3NWRhZDNjOWNmMDYwYThiMjY4MGY3NTQxOTE3OSIsInN1YiI6IjYxNWVlZWUzNjdlMGY3MDA0Mzg4YjA0OSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.4TCwbzHc7Wajk13HfNEm4v2AH_DLzQ2x3y2WVpj6Jf4"

###+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def get_popular_movies():# stworzenie funkcji, która pobierze dane o ____________
    #____________________#_najpopularniejszych filmach.__________________________
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()
###_______________________________________________________________________________


#____________________________________Print chwilowo sprawdza zawartość data_______
data = get_popular_movies()
for key  in data:
    print( key )
#_________________________________________________________________________________    
##_____________Pobiera wybraną listę filmów_______________________________________
def get_movies_list(list_type):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()
###_______________________________________________________________________________
# ______funkcja przyjmuje w parametrze ścieżkę do plakatu oraz rozmiar.___________
# ______domyślną wartość obrazka ma w342 _________________________________________
def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"
###_______________________________________________________________________________
#__________funkcja przycina listę filmów i tworzy dane do wyśwetlania_____________
def get_movies(how_many, list_type):
    data = get_movies_list(list_type)['results']
    return random.sample(data, k=len(data))[:how_many]
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def get_genres():
    endpoint = "https://api.themoviedb.org/3/genre/tv/list"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    response = response.json()['genres'] 
    return response

def get_genre_movies(collection_id):
    endpoint = f"https://api.themoviedb.org/3/collection/{collection_id}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()


def list_check(list_type):
    genres = get_genres()
    genres = [genres['name'] for genres in genres]   
    for genre in genres:
        if list_type == genre:
            return True
        get_movies(how_many=8, list_type="popularr")
    return genres    


#=================================================================================
###_________________________SZABLON MOVIE DETAILS_________________________________
#__________________def która pobierze szczegóły konkretnego filmu z API. _________
def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()
###_____________________________________________Image____________________________
def get_movie_images(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()
###_____________________________________________Aktors___________________________
def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()["cast"]
###===============================================================================

