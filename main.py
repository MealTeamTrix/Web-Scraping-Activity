import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 3.1: Fetch HTML Content
url = 'http://example.com/sports-data'
response = requests.get(url)

if response.status_code == 200:
    html_content = response.text
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
    
# Step 3.2: Extract the Required Data
soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find('table', class_='stats-table')
rows = table.find_all('tr')

game_data = []
for row in rows:
    cols = row.find_all('td')
    game_info = [col.text.strip() for col in cols]
    game_data.append(game_info)

# Step 4.1: Convert to a DataFrame
headers = ['Date', 'Team1', 'Team2', 'Score', 'Location']
df = pd.DataFrame(game_data, columns=headers)

# Step 4.2: Inspect the DataFrame
print(df.head())

# Step 5.1: Save to a CSV File
df.to_csv('sports_statistics.csv', index=False)