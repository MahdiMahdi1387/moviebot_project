import requests


async def get_movie_info_by_id(movie_id: int) -> tuple:
    url = f'https://moviesapi.ir/api/v1/movies/{movie_id}'
    
    response = requests.get(url)
    if response.status_code != 200:
        return 'ERROR'
    else:
        response: str = response.json()
        title: str = response['title']
        country: str = response['country']
        year: int = int(response['year'])
        imdb_rate: float = float(response['imdb_rating'])
        plot: str = response['plot']
        images: str = response['images']

        return (title, country , year, imdb_rate, plot, images)


def get_movie_info_by_name(movie_name: str) -> tuple:
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
        title: str = result['title']
        year: int = int(result['year'])
        country: str =  result['country']
        imdb_rate: float = float(result['imdb_rating'])
        movie_id: int = result['id']

        return (title, country , year, imdb_rate, movie_id)

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
