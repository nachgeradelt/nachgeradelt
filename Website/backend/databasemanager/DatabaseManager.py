# -*- coding: utf-8 -*-
'''
Created on May 10, 2018

@author: iranox
'''

from mysql.connector import (connection)
from flask.json import jsonify
import yaml


class DatabaseManager():

    def __init__(self,configfile,host=None,database=None,user=None,password=None):
        if configfile is not None:
            with open(configfile, 'r') as ymlfile:
                cfg = yaml.load(ymlfile)
            config = cfg['databaseconfig']
            self._host = config['host']
            self._database = config['database']
            self._user = config['user']
            self._password = config['password']
        else:
            self._host = host
            self._database = database
            self._user = user
            self._password = password

    def createTables(self,tables):
        cnx = connection.MySQLConnection(user=self._user, password=self._password,host=self._host,
                                     database=self._database)
        coursor = cnx.cursor()
        try:
            for table in tables:
                coursor.execute(tables[table])
        except connection.errors as err:
            print(err)
            exit(1)
            
        cnx.close()

    def readTable(self,query):
        cnx = connection.MySQLConnection(user=self._user, password=self._password,host=self._host,
                                     database=self._database)
        cursor = cnx.cursor()
        try:
            cursor.execute(query)
            rowlist = {}
            for rows in cursor.fetchall() :
                rowlist[rows[1]] = rows[0]
            return rowlist
        except connection.errors as err:
            print(err)
            exit(1)
    
    def readTableAsJson(self,query,data = None):
        cnx = connection.MySQLConnection(user=self._user, password=self._password,host=self._host,
                                     database=self._database)
        
        cursor = cnx.cursor()
        if data is None:
            cursor.execute(query)
        else:
            cursor.execute(query,data)
        rv = cursor.fetchall()
        row_headers=[x[0] for x in cursor.description]
        json_data=[]
        for result in rv:
            json_data.append(dict(zip(row_headers,result)))
        return jsonify(json_data)
    


    def insertTableSimple(self,data,query):
        cnx = connection.MySQLConnection(user=self._user, password=self._password,host=self._host,
                                     database=self._database)
        
        cursor = cnx.cursor()
        for row in data:
            try: cursor.execute(query,row)
            except connection.errors as err:
                print(err)
                exit(1)
        cnx.commit()
        cnx.close()
