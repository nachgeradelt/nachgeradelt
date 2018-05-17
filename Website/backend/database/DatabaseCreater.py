'''
Created on May 10, 2018

@author: iranox
'''
from databasemanager.DatabaseManager import  DatabaseManager
from database.Queries.Tables import TABLES
import csv

def getAllDataFromCSV(file="",rows=[]):
    reader = csv.DictReader(open(file, 'r'),
                            skipinitialspace=True,delimiter = ',', quotechar = '"', )
    allData =  []
    for row in reader:
        tmp = {}
        for data in rows:
            tmp[data] = row[data]
        allData.append(tmp)
    return allData


if __name__ == '__main__':
    default = -1
    cnx = DatabaseManager(configfile="../config.yml")
    cnx.createTables(TABLES)
    allData = getAllDataFromCSV(file="../../../tourenverzeichnis.csv",                                         
                            rows = ["Start","Über1","Über2","Über3","Über4","Über5","Über6","Über7","Über8","Ziel",
                                    "Länge in km","Verlinkung zum Fahrtenbuch","Erscheinungsjahr"])
    cnx.insertTableSimple(data=getAllDataFromCSV(file="../../../gps.csv",rows = ["city","lat","lon"]),table="city")
    cnx.insertTableSimple(data=getAllDataFromCSV(file="../../../zitatsammlung.csv",
                                                 rows = ["Zitat","Kategorie","Quelle/Buchtitel","Person","Jahr","Link"]),
                                                 table="quotes")
    rows = cnx.readTable(query="Select id, name from city")
    for x in allData :
            t = {}
            t['via1'] = rows[x['Über1']] if x['Über1'] in rows else None
            t['via2'] = rows[x['Über2']] if x['Über2'] in rows else None
            t['via3'] = rows[x['Über3']] if x['Über3'] in rows else None
            t['via4'] = rows[x['Über4']] if x['Über4'] in rows else None
            t['via5'] = rows[x['Über5']] if x['Über5'] in rows else None
            t['via6'] = rows[x['Über6']] if x['Über6'] in rows else None
            t['via7'] = rows[x['Über7']] if x['Über7'] in rows else None
            t['via8'] = rows[x['Über8']] if x['Über8'] in rows else None
            t['start'] = rows[x['Start']] if x['Start'] in rows else None
            t['target'] = rows[x['Ziel']] if x['Ziel'] in rows else  None
            t['length'] = x['Länge in km']
            t['link'] = x['Verlinkung zum Fahrtenbuch']
            t['year'] = x['Erscheinungsjahr']
            if t['start'] is not None and t['target'] is not None :
                cnx.insertTableSimple(data=[t], table="tour")