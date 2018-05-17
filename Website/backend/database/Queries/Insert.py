'''
Created on May 10, 2018

@author: iranox
'''

INSERT = {}
INSERT['city'] = ("INSERT INTO city (name,lat,lon) VALUES (%(city)s, %(lat)s, %(lon)s)")
INSERT['tour'] = ("INSERT INTO tour (start,target,via1,via2,via3,via4,via5,via6,via7,via8,length,link) VALUES (%(start)s, %(target)s, %(via1)s,"
                  "%(via2)s, %(via3)s, %(via4)s,%(via5)s, %(via6)s, %(via7)s, %(via8)s, %(length)s,%(link)s)")
INSERT['quotes'] = ("INSERT INTO quotes (qoute,person,year,category,quelle,link) VALUES"
                    "(%(Zitat)s,%(Person)s,%(Jahr)s, %(Kategorie)s, %(Quelle/Buchtitel)s,  %(Link)s)")
#"Zitat","Kategorie","Quelle/Buchtitel","Person","Jahr","Link"
