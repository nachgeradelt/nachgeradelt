# -*- coding: utf-8 -*-
'''
@author: iranox
'''
"""Create indexes on column tour_id and chronology of the table tour_waypoints"""

Indexe = {}
Indexe['tour_waypoints_index'] = "CREATE INDEX tour ON tour_waypoints (tour_id)"
Indexe['tour_waypoints_chronology'] = "CREATE INDEX tour_chrono ON tour_waypoints (chronology)"
