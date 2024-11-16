import re as Chercher


def convertCityDataToString(temp):
    str(temp)
    print('Data temperature has been converted to string. Thank you')

def weatherTempFetcher(data):

    weatherTemp = data.find(string=Chercher.compile("°"))

    print(f"\033[1mFound temperature: {weatherTemp.strip()}\033[0m\n")
    global_weatherTemp = weatherTemp.strip()

    convertCityDataToString(global_weatherTemp)






