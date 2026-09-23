import requests


def get_movie_id_by_name(movie_name: str) -> int:
    url = f'https://moviesapi.ir/api/v1/movies'
    params_dict = {
        'q': movie_name
    }
    response = requests.get(url, params=params_dict)
    if response.status_code != 200:
        return 'ERROR'
    else:
        response = response.json()
        result = response['data'][0]
        movie_id: int = result['id']

        return movie_id


def full_info(movie_id: int) -> list:
    url = f'https://moviesapi.ir/api/v1/movies/{movie_id}'
    response = requests.get(url)
    if response.status_code != 200:
        return 'ERROR'
    else:
        response = response.json()
        title: str = response['title']
        country: str = response['country']
        year: int = int(response['year'])
        imdb_rate: float = float(response['imdb_rating'])
        try:
            plot: str | None = response['plot']
        except Exception:
            plot: str | None = None
        try:
            image: str | None = response['images'][0]
        except Exception:
            image: str | None = None

        return (movie_id, title, country , year, imdb_rate, plot, image)
