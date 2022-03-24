from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
from selenium import  webdriver

#driver = webdriver.chrome()

#
# #creating empty lists
# name = []
# price = []
# change_24h =[]
# change_7d = []
# market_cap = []
# volume_24h =[]
#
#

website = 'https://coinmarketcap.com/gainers-losers/'

response = requests.get(website)

response.status_code



soup = BeautifulSoup(response.content, 'html.parser')


results = soup.find('table', {'class':'h7vnx2-2 cZkmip cmc-table'}).find('tbody').find_all('tr')

y = soup.find('table', {'class':'h7vnx2-2 cZkmip cmc-table'})

tbod = soup.find_all('tbody')

trm = soup.find_all('tr')

tdm = soup.find_all('td')


#

# #name
# results[0].find('p', {'class':'sc-1eb5slv-0 iworPT'}).get_text().strip()
# #price
# results[0].find('div', {'class': 'sc-131di3y-0 cLgOOr'}).get_text().strip()
# price_tr = results.find_all()
#
# #24h
# results[0].find('span', {'class': 'sc-15yy2pl-0 hzgCfk'}).get_text().strip()
# #7d
# results[0].find('span', {'class': 'sc-15yy2pl-0 hzgCfk'}).get_text().strip()
# #market cap
# results[0].find('p', {'class': 'sc-1eb5slv-0 hykWbK'}).get_text().strip()
# #volume
# results[0].find('div', {'class': 'sc-16r8icm-0 j3nwcd-0 cRcnjD'}).get_text().strip()
#
#
# #
#creating empty lists
name = []
price = []
change_24h = []
change_7d = []
market_cap = []
volume_24h = []
data = []


tdmo = tdm[4]


# print(tdmo)





for result in tbod[1] :




    try:
        name.append(result.find('p', {'class':'sc-1eb5slv-0 iworPT'}).get_text().strip())

    except:
        name.append('n/a')

    try:
        price.append(result.find('span').get_text().strip())

    except:
        price.append('n/a')


    try:
        change_24h.append(result.find('span', {'class': 'sc-15yy2pl-0 hzgCfk'}).get_text().strip())

    except:
        change_24h.append('n/a')

    try:
        change_7d.append(result.find('span', {'class': 'sc-15yy2pl-0 hzgCfk'}).get_text().strip())

    except:
        change_7d.append('n/a')

    try:
        market_cap.append(result.find('p', {'class': 'sc-1eb5slv-0 hykWbK'}).get_text().strip())

    except:
        market_cap.append('n/a')

    try:
        data.append(result.find(tdmo.find_all('td')).get_text().strip())

    except:
        data.append('not avai')

#
#     # for result in tdm[4] :
#     #
#     #
#     #      try:
#     #           volume_24h.append(result.find('p').get_text().strip())
#     #
#     #
#     #      except:
#     #           volume_24h.append('n/a')
#
print(data)
