'''
Created on May 10, 2018

@author: iranox
'''

TABLES = {}
TABLES['city'] = ("CREATE TABLE IF NOT EXISTS `city` ( `id` int(11) NOT NULL AUTO_INCREMENT,`name` varchar(30) NOT NULL,"
    "  `lat` float,"
    "  `lon` float,"
    "  PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB")
TABLES['tour'] = ("CREATE TABLE IF NOT EXISTS `tour` ( `id` int(11) NOT NULL AUTO_INCREMENT,`start` int(30) NOT NULL,"
    "`target` int(30) NOT NULL,"
    " `via1` int(30),"
    " `via2` int(30),"
    " `via3` int(30),"
    " `via4` int(30),"
    " `via5` int(30),"
    " `via6` int(30),"
    " `via7` int(30),"
    " `via8` int(30),"
    " `length` float,"
    " `quelle` varchar(100),"
    " `link` text,"
    " `year` int(4),"
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
    