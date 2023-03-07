## Scrape Women's 100 Meter Dash data 
## from World Athletics 
## using BeautifulSoup

from bs4 import BeautifulSoup
import pandas as pd 
from urllib.request import urlopen 


def get100w():
    url = "https://worldathletics.org/records/all-time-toplists/sprints/100-metres/outdoor/women/senior?regionType=world&timing=electronic&windReading=regular&page=1&bestResultsOnly=true&firstDay=1899-12-31&lastDay=2023-03-06"
    page = urlopen(url).read()
    print(page)

    soup = BeautifulSoup(page)
    count = 0 
    table = soup.find("tbody")
    pre_df = dict()
    features = {'competitor' 'rank' 'mark', 'nat', 'pos','date'}

    rows = table.find("tr")
    for row in rows:
        if (row.find('th', {"scope":"row"}) != None):

            for f in features:
                cell = row.find("td",{"data-stat": f})

        a = cell.text.strip().encode()
        text=a.decode("utf-8")
        if f in pre_df:
            pre_df[f].append(text)
        else:
            pre_df[f]=[text]

        df = pd.DataFrame.from_dict(pre_df)




