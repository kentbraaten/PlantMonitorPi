from time import sleep
from pots import toMoistureSensorParams, toMoistureRange, toRelayParams, potInfo
from I2CFuncs import getSensorReading, turnOnValve
from waterLogClient import addAction, addReading, normalizeReading, MOISTURE_SENSOR_READING_NORMALIZED, MOISTURE_SENSOR_READING_RAW
from datetime import *


maxCycles = 4


def monitorPots(potsToMonitor):
    sleep(find_time_delta_to_15())
    while True:
        waterPotsIfNeeded(potsToMonitor)
        sleep(find_time_delta_to_15())


def waterPotsIfNeeded(potsToWater):
    for x in range(0,maxCycles):
        readings = getMoistureSensorReadings(potsToWater)
        logReadings(readings)
        potsToWater = getPotsThatNeedWatering(readings, isBelowLowerRange)
        if (len(potsToWater) == 0):
            break
        waterPots(potsToWater)
        logWaterEvents(potsToWater)
        if x < maxCycles - 1:
            sleep(22)


def waterPots(potsToWater):
    for pot in potsToWater:
        turnOnValve(toRelayParams(pot))
        sleep(22)


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
    return normalizeReading(readingTuple[1]) < range[0]


def isBelowUpperRange(readingTuple):
    range = toMoistureRange(readingTuple[0])
    return normalizeReading(readingTuple[1]) < range[1]


def logReadings(readings):
    try:
        for reading in readings:
            logReading(reading)
    except:
        pass


def logReading(reading):
    sensorAddress = toMoistureSensorParams((reading[0]))
    rawReading = reading[1]
    addReading(sensorAddress,rawReading, MOISTURE_SENSOR_READING_RAW)
    addReading(sensorAddress,normalizeReading(rawReading),MOISTURE_SENSOR_READING_NORMALIZED)



def logWaterEvents(pots):
    try:
        for p in pots:
            relayParams = toRelayParams(p)
            addAction(relayParams)
    except:
        pass

    
def find_time_delta_to_15():
    now = datetime.datetime.now()
    seconds = 900 - ((now.minute * 60 + now.second) % 900)
    if (seconds == 0):
        return 900
    else:
        return seconds
        
