import requests
API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhNGY3NWRhZDNjOWNmMDYwYThiMjY4MGY3NTQxOTE3OSIsInN1YiI6IjYxNWVlZWUzNjdlMGY3MDA0Mzg4YjA0OSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.4TCwbzHc7Wajk13HfNEm4v2AH_DLzQ2x3y2WVpj6Jf4"

###______________________________________________________________________________
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

###_______________________________________________________________________________
# ______funkcja przyjmuje w parametrze ścieżkę do plakatu oraz rozmiar.___________
# ______domyślną wartość obrazka ma w342 _________________________________________
def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"


###_______________________________________________________________________________
#__________funkcja przycina listę filmów i tworzy dane do wyśwetlania_____________
def get_movies(how_many):
    data = get_popular_movies()
    return data["results"][:how_many]


###_______________________________________________________________________________
#__________________def która pobierze szczegóły konkretnego filmu z API. _________
def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()


###______________________________________________________________________________
def get_movie_images(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/backdrop_path"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()
