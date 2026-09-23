import sqlite3 as sq
from base import MOVIES_DB
from API import full_info, get_movie_id_by_name
import logging as lg


logger = lg.getLogger(__name__)

def init() -> None:
    """Initializing the database by creation two tables."""

    conn = sq.connect(MOVIES_DB)
    cursor = conn.cursor()
    
    query_movies = """
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL UNIQUE,
            year INTEGER,
            country TEXT,
            imdb_rating REAL,
            plot TEXT,
            poster_url TEXT
        )
    """

    cursor.execute(query_movies)
    conn.close()


def add_movie(movie_id: int, title: str, year: int, 
              country: str, imdb_rating: float,
                plot: str, poster_url: str | None=None) -> bool:
    """Adding a new movie to movies database"""

    conn = sq.connect(MOVIES_DB)
    cursor = conn.cursor()
    try:
        query = """
            INSERT OR IGNORE INTO movies
            (id, title, year, country, imdb_rating, plot, poster_url)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """

        cursor.execute(query, (movie_id, title, year, country
                            , imdb_rating, plot, poster_url))
        
        conn.commit()
    except Exception as e:
        logger.error(f'Error occurred: {e}')
    finally:
        conn.close()

    return cursor.rowcount > 0


def db_movie_by_name(title: str) -> dict | None:
    """To search a movie in database by name"""

    conn = sq.connect(MOVIES_DB)
    cursor = conn.cursor()
    try:
        query = """
            SELECT * FROM movies WHERE title LIKE ? LIMIT 1
        """

        row = cursor.execute(query, (f'%{title}%',)).fetchone()
        return dict(row) if row else None
    except Exception as e:
        logger.error(f'Error occurred: {e}')
    finally:
        conn.close()


def db_movie_by_id(movie_id: int) -> dict | None:
    """To search a movie in database by id"""

    conn = sq.connect(MOVIES_DB)
    cursor = conn.cursor()
    try:
        query = """
            SELECT * FROM movies WHERE id = ?
        """

        row = cursor.execute(query, (movie_id,)).fetchone()
        return dict(row) if row else None
    except Exception as e:
        logger.error(f'Error occurred: {e}')
    finally:
        conn.close()


def update_movie(movie_id: int, **fields) -> bool:
    """To update a record in database."""

    conn = sq.connect(MOVIES_DB)
    cursor = conn.cursor()
    try:

        query = 'UPDATE movies SET '
        query += ', '.join(f'{field} = ?' for field in fields.keys())
        query += ' WHERE id = ?'

        cursor.execute(query, tuple(fields.values()) + (movie_id,))

        conn.commit()
        return True
    except Exception as e:
        logger.error(f'Error occurred: {e}')
        return False
    finally:
        conn.close()


def db_api_checker(title_id: str | int) -> bool | None:
    conn = sq.connect(MOVIES_DB)
    cursor = conn.cursor()
    type_check = type(title_id).__name__
    try:
        if type_check == 'str':
            query = 'SELECT * FROM movies WHERE title LIKE ? LIMIT 1'

            row = cursor.execute(query, (f'%{title_id}%',)).fetchone()

            if row:
                return True
            else:
                return False
        elif type_check == 'int':
                query = 'SELECT * FROM movies WHERE id = ?'
            
                row = cursor.execute(query, (title_id,)).fetchone()
    
                if row:
                    return True
                else:
                    return False
    except ValueError as e:
        logger.error(f'Error occurred: {e}')


def db_manage(input: int | str) -> bool | None:
    type_check = type(input).__name__
    try:
        if db_api_checker(input) == False:
            if type_check == 'int':
                API_in = full_info(input)
                add_movie(
                            API_in[0],
                            API_in[1],
                            API_in[2],
                            API_in[3],
                            API_in[4],
                            API_in[5],
                            API_in[6]
                        )
                return False
            if type_check == 'str':
                movie_id = get_movie_id_by_name(input)
                API_in = full_info(movie_id)
                add_movie(
                            API_in[0],
                            API_in[1],
                            API_in[2],
                            API_in[3],
                            API_in[5],
                            API_in[6]
                        )
        else:
            return True
    except Exception as e:
        logger.error(f'Error occurred: {e}')


if __name__ == '__main__':
    pass
