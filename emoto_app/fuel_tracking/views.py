from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
from typing import NamedTuple
import re

# CREATE SOUP

URL_E95 = 'https://cenapaliw.pl/stationer/e95/malopolskie/krakow'
URL_E98 = 'https://cenapaliw.pl/stationer/e98/malopolskie/krakow'
URL_ON = 'https://cenapaliw.pl/stationer/on/malopolskie/krakow'
URL_LPG = 'https://cenapaliw.pl/stationer/lpg/malopolskie/krakow'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
           '(KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'}

page_e95 = requests.get(URL_E95, headers=headers)
page_e98 = requests.get(URL_E98, headers=headers)
page_on = requests.get(URL_ON, headers=headers)
page_lpg = requests.get(URL_LPG, headers=headers)

soup_e95 = BeautifulSoup(page_e95.content, 'html.parser')
soup_e98 = BeautifulSoup(page_e98.content, 'html.parser')
soup_on = BeautifulSoup(page_on.content, 'html.parser')
soup_lpg = BeautifulSoup(page_lpg.content, 'html.parser')

price_e95 = soup_e95.findAll('b', attrs={"style" : "color: #000000;"})
price_e95 = [elem.text for elem in price_e95]

price_e98 = soup_e98.findAll('b', attrs={"style" : "color: #000000;"})
price_e98 = [elem.text for elem in price_e98]

price_on = soup_on.findAll('b', attrs={"style" : "color: #000000;"})
price_on = [elem.text for elem in price_on]

price_lpg = soup_on.findAll('b', attrs={"style" : "color: #000000;"})
price_lpg = [elem.text for elem in price_lpg]


def get_places(soup):
    td = soup.findAll('td')
    td = td[0::2]
    del td[8]
    places = []

    for elem in td:
        elem = elem.text
        elem = elem[elem.find('Kraków'):]
        elem = elem[6:]
        places.append(elem)

    return places


places_e95 = get_places(soup_e95)
places_e98 = get_places(soup_e98)
places_on = get_places(soup_on)
places_lpg = get_places(soup_lpg)

print(soup_e95)
def home(request):
    return render(request, 'fuel_tracking/base.html')


def e95_price(request):
    data = {}
    for i in range(0, len(places_e95)):
        data[places_e95[i]] = price_e95[i]

    context = {
        'data': data.items()
    }

    return render(request, 'fuel_tracking/e95_price.html', context)


def e98_price(request):
    data = {}
    for i in range(0, len(places_e98)):
        data[places_e98[i]] = price_e98[i]

    context = {
        'data': data.items()
    }
    return render(request, 'fuel_tracking/e98_price.html', context)


def on_price(request):
    data = {}
    for i in range(0, len(places_on)):
        data[places_on[i]] = price_on[i]

    context = {
        'data': data.items()
    }
    return render(request, 'fuel_tracking/on_price.html', context)


def lpg_price(request):
    data = {}
    for i in range(0, len(places_lpg)):
        data[places_lpg[i]] = price_lpg[i]

    context = {
        'data': data.items()
    }
    return render(request, 'fuel_tracking/lpg_price.html', context)



