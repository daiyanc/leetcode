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
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        self.check_in[id] = (station_name, time)

    def check_out(self, id, station_name, time) -> None:
        """
        :type id: int
        :type stationName: str
        :type t: int
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