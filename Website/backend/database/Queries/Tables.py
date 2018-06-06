# -*- coding: utf-8 -*-
'''
Created on May 10, 2018

@author: iranox
'''

"""This are all needed Tables """

TABLES = {}
TABLES['waypoints'] = ("CREATE TABLE IF NOT EXISTS `waypoints` ( `id` int(11) NOT NULL AUTO_INCREMENT,"
    "`name` varchar(30) NOT NULL,"
    "`description` text,"
    "  `lat` float,"
    "  `lon` float,"
    "  PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB")
TABLES['tour'] = ("CREATE TABLE IF NOT EXISTS `tour` ( `id` int(11) NOT NULL AUTO_INCREMENT,"
    "`name` varchar(100) NOT NULL,"
    " `quelle` varchar(100),"
    " `description` text,"
    " `length` float(10),"
    " `link` text,"
    " `year` int(4),"
    "  PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB")
TABLES['tour_waypoints'] = ("CREATE TABLE IF NOT EXISTS `tour_waypoints` ( `id` int(11) NOT NULL AUTO_INCREMENT,"
    "`tour_id` int(10) NOT NULL,"
    "`waypoints_id` int(10),"
    "`chronology` int(10),"
    "  PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB")
TABLES['quotes'] = ("CREATE TABLE IF NOT EXISTS `quotes` ( `id` int(11) NOT NULL AUTO_INCREMENT,"
    "`qoute`text NOT NULL,"
    "`person` varchar(100),"
    " `year` int(4),"
    "category varchar(100),"
    " `quelle` varchar(100),"
    " `link` text,"
    "  PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB")
