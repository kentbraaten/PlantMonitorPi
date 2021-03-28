import time
from pots import toMoistureSensorParams, toMoistureRange, toRelayParams, potInfo
from I2CFuncs import getSensorReading, turnOnValve


maxCycles = 2


def monitorPots(potsToMonitor):
    while True:
        waterPotsIfNeeded(potsToMonitor)
        time.sleep(900)


def waterPotsIfNeeded(potsToWater):
    for x in range(0,maxCycles):
        readings = getMoistureSensorReadings(potsToWater)
        potsToWater = getPotsThatNeedWatering(readings, isBelowLowerRange)
        if (len(potsToWater) == 0):
            break
        logPotsBeingWatered(potsToWater)
        waterPots(potsToWater)
        if x < maxCycles - 1:
            time.sleep(22)


def waterPots(potsToWater):
    for pot in potsToWater:
        turnOnValve(toRelayParams(pot))
        time.sleep(22)


def getMoistureSensorReadings(potsToWater):
    return [(pot, getSensorReading(toMoistureSensorParams(pot)))
                    for pot in potsToWater]


def getPotsThatNeedWatering(tuples):
    return getPotsThatNeedWatering(tuples, isBelowLowerRange)


def getPotsThatNeedWatering(tuples, compareFunc):
    pots = []
    for tuple in tuples:
        if compareFunc(tuple):
            pots.append(tuple[0])
    return pots


def isBelowLowerRange(readingTuple):
    range = toMoistureRange(readingTuple[0])
    return readingTuple[1] < range[0]


def isBelowUpperRange(readingTuple):
    range = toMoistureRange(readingTuple[0])
    return readingTuple[1] < range[0]


def logPotsBeingWatered(pots):
    print("The following pots will be watered")
    for p in pots:
        print(potInfo(p))
        
