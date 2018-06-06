# -*- coding: utf-8 -*-
from flask import Flask
from databasemanager.DatabaseManager import DatabaseManager
from api.queries.readqueries import SELECTS
from flask import request
from flasgger import Swagger
import yaml


app = Flask(__name__)



configfile = "config.yml"

datamanger = DatabaseManager(configfile=configfile)

@app.route("/v1/city")
def getAllCities():
    """Return all waypoints
    ---
    responses:
      200:
        description: Return a List of all waypoints form the database)
    """
    return datamanger.readTableAsJson(query=SELECTS['allWaypoints'])


@app.route("/v1/tour")
def getAllTours():
    """Return all tours
        /v1/tour?start=1 Return all tours with start waypoint 1
        /v1/tour?start=1&end=10 Return all tours with start waypoint 1 and includes the waypoint 10
    ---
    parameters:
      - name: start
        in: query
        type: integer
        required: false
        default: 4
      - name: target
        in: query
        type: integer
        required: false
        default: 4
    responses:
      200:
        description: /v1/tour Return a List of all tours form the database)
    """
    if request.args.get("start")  is not None:
        if len(request.args) > 1:
            start = {'start':request.args.get("start"),"end":request.args.get("target")}
            return   datamanger.readTableAsJson(query=SELECTS['tourStartEnd'],data=start)
        start = {'start':request.args.get("start")}
        return datamanger.readTableAsJson(query=SELECTS['tourStart'],data=start)
    return datamanger.readTableAsJson(query=SELECTS['allTours'])

@app.route("/v1/city/<id>")
def getCity(id):
    """Return all targets
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        default: 4
    responses:
      200:
        description: Return a specific waypoint
    """
    return datamanger.readTableAsJson(query=SELECTS['waypoint'],data={'id':id})

@app.route("/v1/tour/<id>")
def getTour(id):
    """Return all targets
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        default: 4
    responses:
      200:
        description: Return a specific tour
    """
    return datamanger.readTableAsJson(query=SELECTS['tour'],data={'id':id})

@app.route("/v1/targets")
def getAllTargets():
    """Return all targets
    ---
    responses:
      200:
        description: Return a List of all targets form the database)
    """
    return datamanger.readTableAsJson(query=SELECTS['allTargets'])

@app.route("/v1/start")
def getAllStarts():
    """Return all starts
    ---
    responses:
      200:
        description: Return a List of all starts form the database)
    """
    return datamanger.readTableAsJson(query=SELECTS['allStarts'])

@app.route("/v1/qoutes")
def getAllQoutes():
    """Return all qoutes
    ---
    responses:
      200:
        description: Return a List of all qoutes form the database)
    """
    return datamanger.readTableAsJson(query=SELECTS['allQoutes'])

swag = Swagger(app)

if __name__ == "__main__":
    with open(configfile, 'r') as ymlfile:
        cfg = yaml.load(ymlfile)
        config = cfg['backend']
    app.run(debug=config['debug'],host=config['host'],port=config['port'])
