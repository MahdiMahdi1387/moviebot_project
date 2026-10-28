🎬 Telegram Movie Bot

A Python-based Telegram bot that allows users to search for movies, retrieve movie information, and explore movie plots and ratings. The application uses an external movie API to retrieve movie data and SQLite to store movie information locally for faster access and reuse.

✨ Features

- 🔎 Movie Search: Search for movies by title.
- 🎞️ Movie Information: Retrieve movie titles, release years, countries, and IMDb ratings.
- 📖 Plot Viewer: Display a movie's plot through an inline keyboard.
- 🔥 Popular Movies: Browse a list of movies stored in the local database.
- 💾 Local Database: Store movie information in SQLite to avoid repeatedly fetching the same information.
- 🌐 External API Integration: Retrieve movie IDs and detailed information from the Movies API.
- 🎛️ Interactive Interface: Use Telegram reply keyboards and inline buttons to interact with the bot.
- ⚠️ Basic Error Handling: Display error messages when requests fail or unexpected errors occur.

🛠️ Technologies Used

- Python — Application logic
- pyTelegramBotAPI — Telegram bot functionality
- Requests — HTTP requests to the external movie API
- SQLite3 — Local movie database
- Movies API — External movie information provider

📂 Project Structure

Telegram-Movie-Bot/
├── main.py
├── API.py
├── movies_db_manage.py
├── base.py
├── requirements.txt
├── README.md
└── src/
    └── movies.db

File Descriptions

File| Description
"main.py"| Handles Telegram commands, messages, and callback queries.
"API.py"| Retrieves movie IDs and detailed movie information from the external API.
"movies_db_manage.py"| Manages the local SQLite database and synchronizes movie information from the external API.
"base.py"| Stores application configuration, including the bot token and database path.
"requirements.txt"| Lists the project's Python dependencies.
"src/movies.db"| Stores movie information locally.

The directory structure may vary depending on how the project is organized.

📋 Requirements

- Python 3.10 or later is recommended.
- A Telegram bot token.
- An internet connection for Telegram and external API requests.

⚙️ Installation

1. Clone the Repository

git clone <repository-url>
cd <repository-directory>

Replace the placeholders with your repository URL and directory name.

2. Create a Virtual Environment

python -m venv .venv

Activate the environment on Linux:

source .venv/bin/activate

3. Install Dependencies

If the project includes a "requirements.txt" file:

pip install -r requirements.txt

Otherwise, install the required packages:

pip install pyTelegramBotAPI requests

The "sqlite3" module is included in Python's standard library.

🔑 Configuration

Open "base.py" and configure the Telegram bot token:

TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
MOVIES_DB = "src/movies.db"

Replace "YOUR_TELEGRAM_BOT_TOKEN" with the token obtained from Telegram's BotFather.

Security note: Never commit your actual bot token to a public repository. Consider loading it from an environment variable instead.

🚀 Running the Bot

From the project root, run:

python main.py

The bot uses polling to receive Telegram updates and process incoming messages.

Make sure that the database initialization function is called before database operations are performed.

🤖 Bot Commands

Command| Description
"/start"| Start the bot and display the main keyboard.
"/search"| Search for a movie by title.
"/popular"| Display a list of movies from the local database.
"/help"| Display usage instructions.

🎮 How to Use

1. Start the Bot

Send "/start" to the bot.

The bot displays a keyboard with the following options:

- "search"
- "popular"
- "help"

2. Search for a Movie

1. Select "search" or send "/search".
2. Enter the movie title.
3. Wait for the bot to search for the movie.
4. Select one of the available inline buttons.

3. View Movie Information

Select the "info" button to display information such as:

- Movie title
- Release year
- Country
- IMDb rating

4. View the Plot

Select the "plot" button to display the movie's plot, provided that plot information is available.

5. Browse Popular Movies

Select "popular" to display information about up to ten movies retrieved from the local database.

The current implementation queries movie IDs from "1" through "10"; it does not independently rank every movie by popularity or IMDb rating.

🗄️ Database Structure

The application stores movie information in a SQLite table named "movies".

Column| Type| Description
"id"| INTEGER| Movie identifier and primary key
"title"| TEXT| Movie title; must be unique
"year"| INTEGER| Release year
"country"| TEXT| Country associated with the movie
"imdb_rating"| REAL| IMDb rating
"plot"| TEXT| Movie plot
"poster_url"| TEXT| Optional poster image URL

The database-management module provides functions for:

- Adding movie records
- Searching by movie title
- Retrieving records by ID
- Updating existing records
- Checking whether a movie already exists
- Retrieving movie information from the external API when necessary

🌐 External API Integration

The project uses the Movies API to retrieve movie information.

The integration provides two main functions:

- "get_movie_id_by_name(movie_name)" — Searches for a movie and retrieves its ID.
- "full_info(movie_id)" — Retrieves detailed information about a movie.

The returned information includes the movie ID, title, year, country, IMDb rating, plot, and poster URL.

The database-management layer uses these functions to fetch and store movie information locally.

🏗️ Architecture

The project consists of three main components:

1. Telegram Bot Layer

Handles commands, user messages, reply keyboards, and inline button callbacks.

2. API Integration Layer

Communicates with the external movie API to retrieve movie IDs and detailed information.

3. Database Layer

Uses SQLite to store movie records and retrieve previously saved information.

This separation makes the project easier to understand and provides a foundation for adding new features.

⚠️ Limitations

- The current implementation relies on an external API for movie information.
- Search operations return only the first matching result from the external API.
- The popular-movies feature currently retrieves records using a fixed range of IDs.
- The application uses basic exception handling.
- HTTP requests do not currently specify explicit timeouts.
- The local database path depends on the project's directory structure.
- The bot does not currently implement user authentication or administrative access controls.

🔮 Future Improvements

- Add pagination and multiple search results.
- Implement proper ranking for popular movies.
- Improve API error handling and request timeouts.
- Add caching and database synchronization improvements.
- Support downloading movie posters.
- Add automated tests.
- Use environment variables for configuration.
- Improve logging and user-facing error messages.
- Add Docker support for deployment.

👨‍💻 Author

Mahdi

📄 License

No license has been specified yet.
