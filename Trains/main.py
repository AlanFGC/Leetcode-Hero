# don't use queue, it does not work for this problem!!
def calculateMinPatforms(at, dt, n):
    print(at, "\n", dt)
    # sort trains
    at.sort()
    dt.sort()
    stations = 1
    i = 0
    currStart = 1
    currEnd = 0
    maxStations = 1

    while currStart < n:
        # has the previous train left?
        if at[currStart] > dt[currEnd]:
            currEnd += 1
            stations = max(0, stations -1) # stations can never go to zero
        else:
            currStart += 1
            stations += 1
        if currEnd + 1 >= n:
            stations += n - (currStart)
            break

        maxStations = max(stations, maxStations)

    return maxStations



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("TEST-1")
    at = [41, 1616, 297, 2042, 1013, 987, 2050, 525, 636, 109]
    dt = [2275, 2076, 1580, 2144, 1231, 1672, 2137, 1016, 2234, 1043]
    print(calculateMinPatforms(at, dt, len(at)))

    print("TEST-2")
    at = [900, 940]
    dt = [910, 1200]
    print(calculateMinPatforms(at, dt, len(at)))

    print("TEST-3")
    at = [900, 940, 950, 1100, 1500, 1800]
    dt = [910, 1200, 1120, 1130, 1900, 2000]
    print(calculateMinPatforms(at, dt, len(at)))



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
