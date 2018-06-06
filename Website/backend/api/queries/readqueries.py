"""Contains all queries for the Flask api""""

SELECTS = {}
SELECTS['allWaypoints'] = ("select * from waypoints")
SELECTS['allStarts'] = ("select t.id, tour.name as tour, waypoints.name, waypoints.lat, waypoints.lon "
                        "from tour_waypoints as t join tour join waypoints "
                        "where tour.id = t.tour_id and t.waypoints_id = waypoints.id "
                        "and chronology = 0")
SELECTS['allTargets'] = ("select w.id as id, tour.name as tour, ts.name as name, ts.lat as lat, ts.lon as lon"
                         " from tour_waypoints as w join (select tour_id, max(chronology) as end from tour_waypoints  "
                         " group by tour_id) as t join waypoints as ts join tour where t.tour_id = w.tour_id "
                         " and t.end = w.chronology and ts.id = w.waypoints_id and tour.id = w.tour_id;")
SELECTS['waypoint'] = ("select * from waypoints where id = %(id)s")
SELECTS['allQoutes'] = ("select distinct id, qoute,person, year, category from quotes")
SELECTS['allTours'] = ("select id, name, length, year from tour")
SELECTS['tour'] = ("select id, name, length, year from tour where id=%(id)s")
SELECTS['tourStart'] = ("select w.name as city, w.lat, w.lon, tw.id,tw.chronology from tour_waypoints as tw"
                        " join (select tour_id as id from tour_waypoints where chronology=0 and waypoints_id=%(start)s) as t"
                        " join tour"
                        " join waypoints as w"
                        " where t.id = tw.tour_id and tour.id = tw.tour_id and w.id = tw.waypoints_id")
SELECTS['tourStartEnd'] = ("select distinct w.name as city, w.lat, w.lon, tour.name as tour, tour.id,chronology"
                            " from tour_waypoints"
                            " join (select tw.tour_id from tour_waypoints  as tw"
                            " join (select tour_id from tour_waypoints where chronology=0 and waypoints_id=%(start)s) as  t "
                            " where t.tour_id = tw.tour_id and waypoints_id = %(end)s) as k "
                            "  join tour "
                            " join waypoints as w"
                            " where tour_waypoints.tour_id = k.tour_id and tour.id = tour_waypoints.tour_id and w.id = tour_waypoints.waypoints_id")
