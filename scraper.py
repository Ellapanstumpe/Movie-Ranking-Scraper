import requests
import sqlite3
import pandas as pd
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = 'https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films'

# Database and file paths
db_name = 'Movies.db'
table_name = 'Top_50'
csv_path = '/home/project/top_50_films.csv'

# Create an empty DataFrame with specified columns
df = pd.DataFrame(columns=["Average Rank", "Film", "Year"])

# Counter for limiting the loop to top 50 films
count = 0

# Fetch HTML content from the webpage
html_page = requests.get(url).text
data = BeautifulSoup(html_page, 'html.parser')

# Find all tables and rows in the HTML
tables = data.find_all('tbody')
rows = tables[0].find_all('tr')

# Iterate through rows to extract film data
for row in rows:
    if count < 50:
        col = row.find_all('td')
        if len(col) != 0:
            # Extract data for each film
            data_dict = {
                "Average Rank": col[0].contents[0],
                "Film": col[1].contents[0],
                "Year": col[2].contents[0]
            }
            # Create a temporary DataFrame for the current film
            df1 = pd.DataFrame(data_dict, index=[0])
            # Concatenate the temporary DataFrame to the main DataFrame
            df = pd.concat([df, df1], ignore_index=True)
            count += 1
    else:
        break

# Print the resulting DataFrame
print(df)

# Save the DataFrame to a CSV file
df.to_csv(csv_path)

# Connect to SQLite database, replace the table if it exists, and close the connection
conn = sqlite3.connect(db_name)
df.to_sql(table_name, conn, if_exists='replace', index=False)
conn.close()
