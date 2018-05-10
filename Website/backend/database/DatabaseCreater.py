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
    cnx = DatabaseManager(user='root', password='password',host='127.0.0.1',database='radfahrerwissen')
    cnx.createTables(TABLES)
    cnx.insertTableSimple(data=getAllDataFromCSV(file="../../../gps.csv",rows = ["city","lat","lon"]),table="city")