#!/usr/bin/env python3

def gas_station(gas, cost):

    begin = 0
    total = 0
    fuel = 0

    for i in range(len(gas)):
        fuel = fuel + gas[i] - cost[i]
        if fuel < 0:
            begin = i + 1
            total = total + fuel
            fuel = 0
        if total + fuel < 0:
            return -1
        else:
            return begin
