# -*- coding: utf-8 -*-
from flask import Flask
from databasemanager.DatabaseManager import DatabaseManager
from api.queries.readqueries import SELECTS
from flask import request


app = Flask(__name__)

datamanger = DatabaseManager(configfile=None, host="localhost", database="radfahrerwissen",
                                           user="root", password="password")

configfile = "../config.yml"

@app.route("/v1/city")
def getAllCities():
    return datamanger.readTableAsJson(query=SELECTS['allWaypoints'])

@app.route("/v1/tour")
def getAllTours():
    if request.args.get("start")  is not None:
        if len(request.args) > 1:
            start = {'start':request.args.get("start"),"end":request.args.get("target")}
            return   datamanger.readTableAsJson(query=SELECTS['tourStartEnd'],data=start)  
        start = {'start':request.args.get("start")}
        return datamanger.readTableAsJson(query=SELECTS['tourStart'],data=start)
    return datamanger.readTableAsJson(query=SELECTS['allTours'])

@app.route("/v1/city/<id>")
def getCity(id):
    return datamanger.readTableAsJson(query=SELECTS['waypoint'],data={'id':id})

@app.route("/v1/tour/<id>")
def getTour(id):
    return datamanger.readTableAsJson(query=SELECTS['tour'],data={'id':id})

@app.route("/v1/targets")
def getAllTargets():
    return datamanger.readTableAsJson(query=SELECTS['allTargets'])

@app.route("/v1/start")
def getAllStarts():
    return datamanger.readTableAsJson(query=SELECTS['allStarts'])

@app.route("/v1/qoutes")
def getAllQoutes():
    return datamanger.readTableAsJson(query=SELECTS['allQoutes'])

if __name__ == "__main__":
    app.run(debug=True)