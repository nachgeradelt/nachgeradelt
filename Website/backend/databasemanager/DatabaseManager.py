'''
Created on May 10, 2018

@author: iranox
'''

from mysql.connector import (connection)
from database.Queries.Insert import INSERT

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

class DatabaseManager():
    
    def __init__(self, user='root', password='password',host='127.0.0.1',
                                     database='radfahrerwissen'):
        self._user = user
        self._password = password
        self._host = host
        self._database = database
        self._query_mangager = QueryManager()
    
    def createTables(self,tables):
        cnx = connection.MySQLConnection(user=self._user, password=self._password,host=self._host,
                                     database=self._database)
        self._query_mangager.createTables(cnx.cursor(), tables)
        cnx.close()
    
    def insertTableSimple(self,data,table):
        insertquery = INSERT[table]
        cnx = connection.MySQLConnection(user=self._user, password=self._password,host=self._host,
                                     database=self._database)
        for rows in data:
            self._query_mangager.insertTable(cnx.cursor(), rows, insertquery)
        
        cnx.commit()
        cnx.close()
        
