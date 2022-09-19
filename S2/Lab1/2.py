gas_stations = [200, 375, 550, 750]


def find_number_of_stations(gas_stations):
    distance = 950
    capacity_of_auto = 400
    counter = 0
    passed_stations = []

    if capacity_of_auto >= distance:
        return 0
    else:
        for i in range(len(gas_stations) - 2):
            if gas_stations[i] <= capacity_of_auto and gas_stations[i + 1] > capacity_of_auto \
                and gas_stations[i] - capacity_of_auto < passed_stations[-1]:

                capacity_of_auto += gas_stations[i]
                counter += 1
                passed_stations.append(gas_stations[i])


find_number_of_stations(gas_stations)
