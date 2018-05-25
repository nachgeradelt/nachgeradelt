# -*- coding: utf-8 -*-
'''
Created on May 17, 2018

@author: iranox
'''
from databasemanager.DatabaseManager import DatabaseManager
from flask.json import jsonify

class RequestHandler(object):
    '''
    classdocs
    '''
    
    def __init__(self):
        self._datamanger = DatabaseManager(configfile=None, host="localhost", database="radfahrerwissen",
                                           user="root", password="password")
    
    def _cityToList(self, data):
        reponse = []
        for rows in data :
            reponse.append({'id': rows[0], 'city': rows[1], 'lat': rows[2], 'lon': rows[3]})
        return reponse
    
    def getAllQoutes(self):
        reponse = []
        for rows in self._datamanger.readSimpleTable("select distinct id, qoute,person, year, category from quotes"):
            reponse.append({'id': rows[0], 'qoute': rows[1], 'person': rows[2], 'year': rows[3], 'category':rows[4]})
        return jsonify(reponse)
        
    def getCity(self,number):
        return jsonify(self._cityToList(self._datamanger.readSimpleTable("Select * from city where id = %(id)s",number)))
    
    def getAllStarts(self):
        reponse = self._cityToList(self._datamanger.readSimpleTable("select distinct tour.start,city.name,city.lat, city.lon from tour inner join city where city.id = tour.start"))
        return jsonify(reponse)
    
    def getAllTargets(self):
        reponse = self._cityToList(self._datamanger.readSimpleTable("select distinct tour.target,city.name,city.lat, city.lon from tour inner join city where city.id = tour.target"))
        return jsonify(reponse)
        
    def getAllCities(self):
        reponse = self._cityToList(self._datamanger.readSimpleTable("Select * from city"))
        return jsonify(reponse)