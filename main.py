import requests
from bs4 import BeautifulSoup
import json

req = requests.get('https://lol.fandom.com/wiki/World_Championship')


soup = BeautifulSoup(req.text, 'html.parser')

tabela = soup.find('table', {'class': 'wikitable'})
tabela2 = tabela.find('tbody')

turniej = []
mistrz = []
nagroda = []

for row in tabela2.find_all('tr'):
    kolumna = 1
    for column in row.find_all('td'):
        if kolumna == 1:
            t = column.find("a")
            if t != None:
                turniej.append(t.text.strip())

        if kolumna == 4:
            teamname = column.find('span', {'class': 'teamname'})
            mistrz.append(teamname.text.strip())
    
        if kolumna == 3:
            nagroda.append(column.text.strip())

        
        kolumna += 1

            

wynik = (list(zip(turniej, mistrz, nagroda)))
with open('lol.json', 'w') as f:
    json.dump(wynik, f)
