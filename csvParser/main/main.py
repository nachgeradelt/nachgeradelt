'''
Created on Apr 28, 2018

@author: iranox
'''
import csv
import requests

def parse_csv():
    """
    Liest die Datei tourenverzeichnis.csv und speichert alle Staedte in eine Menge.
    Pfad ist hard gecodet.
    """
    reader = csv.DictReader(open('../../tourenverzeichnis.csv', 'rb'),
                            skipinitialspace=True,delimiter = ',', quotechar = '"', )
    allCities = set()
    for row in reader:
        allCities.add(row['Ziel'])
        allCities.add(row['Start'])
        allCities.add(row['\xc3\x9cber1'])
        allCities.add(row['\xc3\x9cber2'])
        allCities.add(row['\xc3\x9cber3'])
        allCities.add(row['\xc3\x9cber4'])
        allCities.add(row['\xc3\x9cber5'])
        allCities.add(row['\xc3\x9cber6'])
        allCities.add(row['\xc3\x9cber7'])
        allCities.add(row['\xc3\x9cber8'])
    return allCities


def get_city_gps(cities):
    """
    Die Funktion sucht fuer die Staedtenamen die entsprechende GPS-Koordinaten raus.
    Dazu nutzt es den Service nominatim.openstreetmap.org. Dabei ist zu beachten,
    dass er immer nur den ersten Treffer nimmt, was bei mehrdeutigen Staedtenamen
    falsche Treffer erzeugen kann. Bei zu vielen Anfragen blockiert der Service die
    IP temporaer.
    """
    cities_with_gps = []
    for city in cities:
        print("Search for " + city)
        city_gps_json = requests.get(url="https://nominatim.openstreetmap.org/search/de/%20"
                                 +city+"?format=json&limit=1&addressdetails=1").json()
        if len(city_gps_json) is not 0 and city_gps_json[0]['address']['country'] in "Deutschland" :
            cities_with_gps.append({'city':city,"lon":city_gps_json[0]['lon'],
                                    "lat":city_gps_json[0]["lat"]})
    return cities_with_gps


def write_into_csv(cities):
    """
        Die Staedte werden den Namen nach sotiert und in eine CSV-Datei geschrieben. Die Datei hat den Aufbau:
        city,lon, lat
         Pfad ist hard gecodet.
    """
    with open('../../gps.csv', 'w') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        writer.writerow(['city', 'lon', 'lat'])
        cities.sort(key=lambda k: k['city'])
        for item in cities:
            if 'lat' in item:
                writer.writerow([item['city'], item['lon'], item['lat']])
            else :
                writer.writerow([item['city']])

if __name__ == '__main__':
    write_into_csv(get_city_gps(parse_csv()))
