
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