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
        """Read the configfile or use parameter as connection properties
           @param configfile: path to configfile
           @param host: Host of the database. default None
           @param database: name of the database. default None
           @param user: username of the database. default None
           @param password: password of the database. default None
        """
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
        """Create a connection to the database and execute  queries again the table
           @param tables: A dictonary that contain all Queries. See ../database/Queries/Tables.py for examples
        """
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
        """Create a connection to the database and execute  queries again the table
           @param query: Query as String
           @return: Result of the query as dictonary. the dictonary used column 1 as key and column 0 as value
        """
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
        """Create a connection to the database and execute  queries again the table
           @param query: Query as String
           @param data: a dictonary for filter the result. Example {id=5} for the Query Select * from foo where id=%(id)s
           @return: Result of the query as json.
        """
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
        """Create a connection to the database and insert  Data again the table
           @param query: Query as String
           @param data: data
        """
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
