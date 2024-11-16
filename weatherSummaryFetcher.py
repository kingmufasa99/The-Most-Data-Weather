import re as Chercher

def weatherSummaryFetcher(data):

    weatherSummary = data.find_all(string=Chercher.compile('Current Weather'))
    for i in weatherSummary:
        print(i.strip())