

import requests as r
from bs4 import BeautifulSoup

# needed to access website
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0'}

# links to webpages
url0 = "https://www.the-numbers.com/movie/budgets/all"
url1 = "https://www.the-numbers.com/movie/budgets/all/101"

html0 = r.get(url0, headers=headers)
html1 = r.get(url1, headers=headers)

soup0 = BeautifulSoup(html0.text, 'lxml')
soup1 = BeautifulSoup(html1.text, 'lxml')

movieTitles0 = soup0.find_all('b')
movieTitles1 = soup1.find_all('b')
movieYears0 = soup0.find_all('td')
movieYears1 = soup1.find_all('td')
movieBudgets0 = soup0.find_all('td', class_ = 'data')
movieBudgets1 = soup0.find_all('td', class_ = 'data')

movies = []
for i in range(1, 101):
    movies.append(str(movieTitles0[i].text))
    movies.append(str(movieTitles1[i].text))

years = []
for i in range(0, len(movieYears0)):
    if str(movieYears0[i]).find("box-office-chart", 13) != -1:
        years.append(str(movieYears0[i].text))
        years.append(str(movieYears1[i].text))

budgets = []
print(movieBudgets0)
for i in range(0, len(movieBudgets0)):
    if i % 4 == 1:
        budgets.append(str(movieBudgets0[i].text).replace('&nbsp;', ' '))
        budgets.append(str(movieBudgets1[i].text).replace('&nbsp;', ' '))

"""
with open("movies.txt", "w", encoding="utf-8") as f:
    for i in range(0, 200):
        n = movies[i] + " " + years[i] + " " + budgets[i]
        f.write(n)
        f.write('\n')
"""