# Backend application

Programmed by [Tobias Wieprich](http://github.com/Iranox).

The backend delivers the tour data from a SQL database.

At the moment the frontend does not use this service.

# Installation

## config database

First change the properties in the config.yml:

``` yml
databaseconfig :
    host : localhost
    database: database
    user: root
    password: password
    port: 3306
```

``` bash
## install dependencies
pip install -r requirements.txt

## create database
python DatabaseCreater.py
```

## Run Python Flask

### change the properties in the config.yml (the port that listens the
backend):

``` yml
backend:
    host: localhost
    port: 5000
    debug: True
```

``` bash
### Run in background
python main.py &
```
