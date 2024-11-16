from weatherDataStore import *

from datetime import datetime
from weatherTempFetcher import *
from bs4 import BeautifulSoup


def main():

    while True:
        print("\n==============================")
        print("The Most Weather Data Center")
        print("==============================")
        city = input("Please enter the city name: ").strip()
        city = city + " city weather celcius"

        currentDateTime = datetime.now()


        print("\nFetching weather data from Google Servers...\n")

        fetchingWheaterDataWithSoup(city)

        choiceToStore = input("\nWould you like to store and collect this data? (yes to store, or no): ").strip().lower()
        choiceToContinue = input("\nWould you like to search for another city? (yes to continue, no to exit): ").strip().lower()

        if choiceToStore != 'yes':
            print('No storing. Thank you')
        if choiceToContinue != 'yes':
            print("\nThank you for using The Most Weather Data Center. Goodbye!\n")
            break

if __name__ == "__main__":
    main()
