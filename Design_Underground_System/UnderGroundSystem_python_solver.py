# Your underground_system object will be instantiated and called as such:
# obj = underground_system()
# obj.check_in(id,station_name,t)
# obj.check_out(id,station_name,t)
# param_3 = obj.get_average_time(start_station,end_station)

class underground_system(object):
    def __init__(self) -> None:
        self.check_in = dict
        self.route = dict

    def check_in(self, id, station_name, time) -> None:
        """
        A customer with a card ID equal to id, checks in at the station stationName at time t.
        A customer can only be checked into one place at a time.
        :type id: int
        :type stationName: str
        :type time: int
        :rtype: None
        """
        self.check_in[id] = (station_name, time)

    def check_out(self, id, station_name, time) -> None:
        """
        A customer with a card ID equal to id, checks out from the station stationName at time t.
        :type id: int
        :type stationName: str
        :type time: int
        :rtype: None
        """

        station, start = self.check_in[id]
        del self.check_in[id]
        route = station + "," + station_name
        if route not in self.route:
            self.route[route] = [0, 0]
        trip = self.route[route]
        trip[0] += 1
        trip[1] += time - start

    def get_average_time(self, start_station, end_station) -> float:
        """
        Returns the average time it takes to travel from startStation to endStation.
        The average time is computed from all the previous traveling times from startStation to endStation that happened directly, 
        meaning a check in at startStation followed by a check out from endStation.
        The time it takes to travel from startStation to endStation may be different from the time it takes to travel from endStation to startStation.
        There will be at least one customer that has traveled from startStation to endStation before getAverageTime is called.
        You may assume all calls to the checkIn and checkOut methods are consistent. If a customer checks in at time t1 then checks out at time t2, then t1 < t2. 
        All events happen in chronological order.
        :type startStation: str
        :type endStation: str
        :rtype: float
        """

        count, route_sum = self.route[start_station + ", " + end_station]
        return route_sum / count

obj = underground_system()
obj.check_in(10, "Leyton", 3)
obj.check_out(5, "Paradies", 8)
param_3 = obj.get_average_time()
print(param_3)