# Movie-Ranking-Scraper
This Python script scrapes the top 50 films' ranking, film names, and release years from the webpage 100 Most Highly-Ranked Films and stores the information in both a CSV file and a SQLite database.

# Prerequisites
Make sure you have the following dependencies installed:

requests
sqlite3
pandas
beautifulsoup4
Install them using the following command:


pip install requests sqlite3 pandas beautifulsoup4
Usage
Clone the repository:


git clone https://github.com/yourusername/your-repo.git
cd your-repo
Run the script:


python scraper.py
Check the output:

The script will print the top 50 films' data to the console.
A CSV file (top_50_films.csv) containing the same data will be created in the project directory.
A SQLite database (Movies.db) will be created, and a table (Top_50) will be populated with the scraped data.


Note

Make sure to respect the terms of service and policies of the website being scraped.
Adjust the URLs, file paths, and database names as needed for your use case.
This script is intended for educational purposes and scraping websites should be done responsibly and within legal and ethical boundaries.
Feel free to customize and improve the script according to your needs!
