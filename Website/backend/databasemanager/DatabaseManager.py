'''
Created on May 10, 2018

@author: iranox
'''

from mysql.connector import (connection)
from database.Queries.Insert import INSERT
import yaml

class QueryManager(object):
    '''
    classdocs
    '''

    def __init__(self):
        pass
    
    def createTables(self,cursor,tables):
        try:
            for table in tables:
                cursor.execute(tables[table])
        except connection.errors as err:
            print(err)
            exit(1)
    
    def insertTable(self,cursor,data,query):
        try: cursor.execute(query,data)
        except connection.errors as err:
            print(err)
            exit(1)
            
    def readTable(self,cursor,query):
        try: 
            cursor.execute(query)
            rowlist = {}
            for rows in cursor.fetchall() :
                rowlist[rows[1]] = rows[0]
            return rowlist
        except connection.errors as err:
            print(err)
            exit(1)   
    

class DatabaseManager():
    
    def __init__(self,configfile):
        if configfile is not None:
            with open(configfile, 'r') as ymlfile:
                cfg = yaml.load(ymlfile)
            config = cfg['databaseconfig']
            self._host = config['host']
            self._database = config['database']
            self._user = config['user']
            self._password = config['password']
            
        self._query_mangager = QueryManager()
        
    def createTables(self,tables):
        cnx = connection.MySQLConnection(user=self._user, password=self._password,host=self._host,
                                     database=self._database)
        self._query_mangager.createTables(cnx.cursor(), tables)
        cnx.close()
    
    def readTable(self,query):
        cnx = connection.MySQLConnection(user=self._user, password=self._password,host=self._host,
                                     database=self._database)
        return self._query_mangager.readTable(cnx.cursor(), query)
        
              
    def insertTableSimple(self,data,table):
        insertquery = INSERT[table]
        cnx = connection.MySQLConnection(user=self._user, password=self._password,host=self._host,
                                     database=self._database)
        for rows in data:
            self._query_mangager.insertTable(cnx.cursor(), rows, insertquery)
        
        cnx.commit()
        cnx.close()