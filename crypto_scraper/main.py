#!/usr/bin/env python3

import requests
import re
import sqlite3
from bs4 import BeautifulSoup


con = sqlite3.connect("crypto.db")
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS crypto_data(rank, name, price, day_change)")


r = requests.get('https://www.coingecko.com/')

soup = BeautifulSoup(r.text, 'html.parser')

data = []
for i in range(1, 11):
    coins = soup.find_all('tr')[i].get_text().strip().replace('\n', ' ').splitlines()
    data.append(coins)

cleaned = []
for j in range(0, len(data)):
    for k in range(0, len(data[j])):
            cleaned.append(data[j][k].split(' '))


cleaned_2 = []
for j in range(0, len(cleaned)):
    new_data = []
    for k in range(0, len(cleaned[j])):
        if cleaned[j][k] != '': 
            new_data.append(cleaned[j][k])
    cleaned_2.append(new_data)


for i in range(0, len(cleaned_2)):
    rank = cleaned_2[i][0]
    name = cleaned_2[i][1]
    price = cleaned_2[i][3]
    day_change = cleaned_2[i][5]

    data_t = (rank, name, price, day_change)

    query = """INSERT INTO crypto_data(rank, name, price, day_change) VALUES(?, ?, ?, ?)"""

    cur.execute(query, data_t)


con.commit()

