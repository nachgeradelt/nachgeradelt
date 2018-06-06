# -*- coding: utf-8 -*-
'''
Created on May 10, 2018

@author: iranox
'''
from databasemanager.DatabaseManager import  DatabaseManager
from database.Queries.Tables import TABLES
import csv
from database.Queries.Insert import INSERT
from database.Queries.Indexe import Indexe

def getAllDataFromCSV(file="",rows=[]):
    """ Read all columms of a CSV file
        @param file: path to the CSV file
        @param rows: header of the CSV file
    """
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
    cnx = DatabaseManager(configfile="config.yml")
    print("Create Tables")
    cnx.createTables(TABLES)
    print("Insert Tables")
    cnx.insertTableSimple(data=getAllDataFromCSV(file="../../zitatsammlung.csv",
                                                 rows = ["Zitat","Kategorie","Quelle/Buchtitel","Person","Jahr","Link"]),
                                                 query=INSERT["quotes"])
    allCities = data=getAllDataFromCSV(file="../../gps.csv",rows = ["city","lat","lon"])
    cityname = [];
    for data in allCities :
        tmp = {'name':data['city'],'lat':data['lat'],'lon':data['lon']}
        cityname.append(tmp)
    cnx.insertTableSimple(cityname,query= INSERT["waypoints"])
    allData = getAllDataFromCSV(file="../../tourenverzeichnis.csv",
                            rows = ["Start","Über1","Über2","Über3","Über4","Über5","Über6","Über7","Über8","Ziel",
                                    "Länge in km","Verlinkung zum Fahrtenbuch","Erscheinungsjahr"])
    allTours = []
    city_rows = cnx.readTable(query="Select id, name from waypoints")
    waypoints_tour = []
    tourid = 1
    for row in allData :
        tmp = {'length':row['Länge in km'],'link':row['Verlinkung zum Fahrtenbuch'],
               'name':row['Start'] +"-" + row['Ziel'] + "-" + row['Erscheinungsjahr'],
               'year':row['Erscheinungsjahr']}
        allTours.append(tmp)
        order = 0
        if row['Start'] in city_rows :
            waypoints_tour.append({'tour_id':tourid,'waypoint_id':city_rows[row['Start']],'chronology':order})
            order += 1
        if row['Über1'] in city_rows :
            waypoints_tour.append({'tour_id':tourid,'waypoint_id':city_rows[row['Über1']],'chronology':order})
            order += 1
        if row['Über2'] in city_rows :
            waypoints_tour.append({'tour_id':tourid,'waypoint_id':city_rows[row['Über2']],'chronology':order})
            order += 1
        if row['Über3'] in city_rows :
            waypoints_tour.append({'tour_id':tourid,'waypoint_id':city_rows[row['Über3']],'chronology':order})
            order += 1
        if row['Über4'] in city_rows :
            waypoints_tour.append({'tour_id':tourid,'waypoint_id':city_rows[row['Über4']],'chronology':order})
            order += 1
        if row['Über5'] in city_rows :
            waypoints_tour.append({'tour_id':tourid,'waypoint_id':city_rows[row['Über5']],'chronology':order})
            order += 1
        if row['Über6'] in city_rows :
            waypoints_tour.append({'tour_id':tourid,'waypoint_id':city_rows[row['Über6']],'chronology':order})
            order += 1
        if row['Über7'] in city_rows :
            waypoints_tour.append({'tour_id':tourid,'waypoint_id':city_rows[row['Über7']],'chronology':order})
            order += 1
        if row['Über8'] in city_rows :
            waypoints_tour.append({'tour_id':tourid,'waypoint_id':city_rows[row['Über8']],'chronology':order})
            order += 1
        if row['Ziel'] in city_rows :
            waypoints_tour.append({'tour_id':tourid,'waypoint_id':city_rows[row['Ziel']],'chronology':order})
            order = 0
        tourid += 1
    cnx.insertTableSimple(data=allTours, query=INSERT['tour'])
    cnx.insertTableSimple(data=waypoints_tour, query=INSERT['tour_waypoints'])
    print("Create Indexe")
    cnx.createTables(Indexe)
