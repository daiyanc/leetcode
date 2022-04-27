/**
 * Your UndergroundSystem object will be instantiated and called as such:
 * UndergroundSystem obj = new UndergroundSystem();
 * obj.checkIn(id,stationName,t);
 * obj.checkOut(id,stationName,t);
 * double param3 = obj.getAverageTime(startStation,endStation);
 */

package Design_Underground_System;

import java.util.HashMap;

class UndergroundSystem {
    private HashMap<String, Integer> totalTimeFromStartToEnd;
    private HashMap<String, Integer> numCustomers;
    private HashMap<Integer, Integer> customerIdStartTime;
    private HashMap<Integer, String> customerIdStartStation; 

    public UndergroundSystem() {
        totalTimeFromStartToEnd = new HashMap<>();
        numCustomers = new HashMap<>();
        customerIdStartTime = new HashMap<>();
        customerIdStartStation = new HashMap<>();
    }

    public void checkIn(int id, String stationName, int time) {

        /* A customer with a card ID equal to id, checks in at the station stationName at time t.
        A customer can only be checked into one place at a time. */ 
        
        customerIdStartTime.put(id, time);
        customerIdStartStation.put(id, stationName);
    }

    public void checkOut(int id, String stationName, int time) {

        // A customer with a card ID equal to id, checks out from the station stationName at time t.

        int totalTime = time - customerIdStartTime.get(id);
        String key = customerIdStartStation.get(id) + " | " + stationName;
        totalTimeFromStartToEnd.put(key, totalTimeFromStartToEnd.getOrDefault(key, 0) + totalTime);
        numCustomers.put(key, numCustomers.getOrDefault(key, 0) + 1);
    }

    public double getAverageTime(String startStation, String endStation) {

        /* Returns the average time it takes to travel from startStation to endStation.
        The average time is computed from all the previous traveling times from startStation to endStation that happened directly, 
        meaning a check in at startStation followed by a check out from endStation.
        The time it takes to travel from startStation to endStation may be different from the time it takes to travel from endStation to startStation.
        There will be at least one customer that has traveled from startStation to endStation before getAverageTime is called.
        You may assume all calls to the checkIn and checkOut methods are consistent. If a customer checks in at time t1 then checks out at time t2, then t1 < t2. 
        All events happen in chronological order.*/

        String key = startStation + " | " + endStation;
        return totalTimeFromStartToEnd.get(key) / (double) numCustomers.get(key);
    }

    public static void main(String[] args) {
        UndergroundSystem obj = new UndergroundSystem();
        obj.checkIn(1,"stationName1",5);
        obj.checkOut(2,"stationName2",10);
        double param3 = obj.getAverageTime("stationName1","stationName2");
        System.out.println(param3);
    }
}