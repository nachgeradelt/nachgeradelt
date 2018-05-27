# -*- coding: utf-8 -*-
'''
Created on May 17, 2018

@author: iranox
'''
from databasemanager.DatabaseManager import DatabaseManager
from api.queries.readqueries import SELECTS

class RequestHandler(object):
    '''
    classdocs
    '''
    
    def __init__(self):
        self._datamanger = DatabaseManager(configfile=None, host="localhost", database="radfahrerwissen",
                                           user="root", password="password")
    
    def getAllQoutes(self):
        return self._datamanger.readTableAsJson(query=SELECTS['allQoutes'])
    
    def getCity(self,number):
        return self._datamanger.readTableAsJson(query=SELECTS['waypoint'],data=number)
    
    def getAllStarts(self):
        return self._datamanger.readTableAsJson(query=SELECTS['allStarts'])
    
    def getAllTargets(self):
        return self._datamanger.readTableAsJson(query=SELECTS['allTargets'])
        
    def getAllCities(self):
        return self._datamanger.readTableAsJson(query=SELECTS['allWaypoints'])