#!/usr/bin/env python3

def gas_station(gas, cost):
    for i in range(len(cost)):
        count = 0
        fuel = 0

        for j in range(i, i + len(gas)):
            k = j % len(gas)
            # print("k" + str(k))
            fuel = gas[k] - cost[k] + fuel
            # return fuel
            if fuel < 0:
                break

            count = count + 1

            if count == len(gas):
                return i

    return -1
gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
print(gas_station(gas, cost))

gas = [2, 3, 4]
cost = [3, 4, 3]
print(gas_station(gas, cost))

gas = [1, 2]
cost = [2, 1]
print(gas_station(gas, cost))

gas = [3, 4]
cost = [4, 5, 1]
print(gas_station(gas, cost))

