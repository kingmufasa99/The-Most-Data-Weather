import requests
# from weatherTempFetcher import weatherTempFetcher
from weatherSummaryFetcher import weatherSummaryFetcher
from datetime import datetime

from bs4 import BeautifulSoup

from weatherTempFetcher import *


def fetchingWheaterDataWithSoup(cityName):

    cityName=cityName.replace(" ", "+")
    _GOOGLE_WEATHER_SERVER = f'https://www.google.com/search?q={cityName}&oq={cityName}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8'
    response = requests.get(_GOOGLE_WEATHER_SERVER)

    dataSoup = BeautifulSoup(response.text, 'html.parser')


    # print(currentDateTime)

    weatherTempFetcher(dataSoup)
    weatherSummaryFetcher(dataSoup)
