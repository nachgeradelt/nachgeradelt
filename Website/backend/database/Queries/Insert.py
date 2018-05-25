'''
Created on May 10, 2018

@author: iranox
'''

INSERT = {}
INSERT['waypoints'] = ("INSERT INTO waypoints (name,lat,lon) VALUES (%(name)s, %(lat)s, %(lon)s)")
INSERT['tour'] = ("INSERT INTO tour (name,length,link,year) VALUES (%(name)s,%(length)s,%(link)s, %(year)s)")
INSERT['tour_waypoints'] = ("INSERT INTO tour_waypoints (tour_id,waypoints_id,chronology) VALUES"
                    "(%(tour_id)s,%(waypoint_id)s,%(chronology)s)")
INSERT['quotes'] = ("INSERT INTO quotes (qoute,person,year,category,quelle,link) VALUES"
                    "(%(Zitat)s,%(Person)s,%(Jahr)s, %(Kategorie)s, %(Quelle/Buchtitel)s,  %(Link)s)")
