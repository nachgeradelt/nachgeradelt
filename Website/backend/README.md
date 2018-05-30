### Create database

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
# install dependencies
pip install -r requirements.txt

# create database
python DatabaseCreater.py
```

### Run Python Flask
First change the properties in the config.yml:


``` yml
backend:
    host: localhost
    port: 5000
    debug: True
```


``` bash
# install dependencies
pip install -r requirements.txt

# Runa at localhost:5000 in background
python main.py &
```
