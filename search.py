import requests
from bs4 import BeautifulSoup
import sys
import io
from datetime import datetime

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='iso8859-1')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='iso8859-1')

url = "http://rank.ezme.net/trand"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

results = soup.findAll('li', 'mdl-list__item')

search_rank_file = open("rankresult.txt", "w", encoding='iso8859-1')

print(datetime.today().strftime("Today trending topics: %Y.%m.%d"))

for result in results:
    search_rank_file.write(result.get_text())
    print(result.get_text())