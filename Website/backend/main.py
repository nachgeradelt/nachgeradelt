# -*- coding: utf-8 -*-
from flask import Flask
from api.RequestHandler import RequestHandler


app = Flask(__name__)

configfile = "../config.yml"
r = RequestHandler()

@app.route("/v1/city")
def getAllCities():
    return r.getAllCities()

@app.route("/v1/city/<id>")
def getCity(id):
    return r.getCity(number={'id':id})

@app.route("/v1/targets")
def getAllTargets():
    return r.getAllTargets()

@app.route("/v1/start")
def getAllStarts():
    return r.getAllStarts()

@app.route("/v1/qoutes")
def getAllQoutes():
    return r.getAllQoutes()

if __name__ == "__main__":
    app.run(debug=True)