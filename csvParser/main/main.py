'''
Created on Apr 28, 2018

@author: iranox
'''

import csv
import requests

def parse_csv():
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
    with open('../../gps.csv', 'w') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        writer.writerow(['city', 'lon', 'lat'])
        for item in cities:
            if 'lat' in item:
                writer.writerow([item['city'], item['lon'], item['lat']])
            else :
                writer.writerow([item['city']])

if __name__ == '__main__':
    write_into_csv(get_city_gps(parse_csv()))