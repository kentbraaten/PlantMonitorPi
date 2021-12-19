import requests
import json
from datetime import datetime

MOISTURE_SENSOR_READING_RAW = "raw-msr"
MOISTURE_SENSOR_READING_NORMALIZED = "nrm-msr"
OPEN_SOLINOID_ACTION = "os"
START_SYSTEM_EVENT = "start"
STOP_SYSTEM_EVENT = "stop"
ERROR_SYSTEM_EVENT = "error"
MIN_READING = 240
MAX_READING = 600
MAX_ADJUSTED_READING = MAX_READING - MIN_READING



_baseURL = "https://waterlog-311815.uc.r.appspot.com"

def helloWorld():
    url = _baseURL + "?key=" + get_http_key()
    return requests.get(url).content


def addReading(sensorAddress, reading, eventType = MOISTURE_SENSOR_READING_RAW):
    i2CAddress, pin = sensorAddress
    data = {
        "reading": reading,
        "eventType": eventType,
        "dateTime": str(datetime.utcnow()),
        "i2cAddress": i2CAddress,
        "pin": pin  
    }
    response = requests.post(get_url("readings/add"),json = data)
    return response.json()


def addAction(actuatorAddress, actionType = OPEN_SOLINOID_ACTION):
    i2cAddress, pin = actuatorAddress
    data = {
        "actionType": OPEN_SOLINOID_ACTION,
        "dateTime": str(datetime.utcnow()),
        "i2cAddress": i2cAddress,
        "pin": pin
    }
    response = requests.post(get_url("actions/add"),json = data)
    return response.json()


def addSystemEvent(systemEvent):
    data = {
        "dateTime": str(datetime.utcnow()),
        "eventType": systemEvent
    }
    response = requests.post(get_url("systemEvent/add"), json = data)
    return response.json()


def addSettings(potArray):
    settingsDict = _flatenPotArray(potArray, {})
    settingsDict["dateTime"] = str(datetime.utcnow())
    response = requests.post(get_url("settings/add"), json = settingsDict)
    return response.json()


def getSettings():
    response = requests.get(get_url("settings/current"))
    settingsList = response.json()
    if (len(settingsList) > 1):
        return _unFlattenDictionary(sorted(settingsList, key = getDateTime, reverse = True)[0])
    elif (len(response.json() == 1)):
        return _unFlattenDictionary(settingsList[0])
    else:
        return None


def getDateTime(d):
    return d["dateTime"]


def get_http_key():
    with open("clientKey.txt","r") as f:
        return f.readline()


def get_url(route):
    return _baseURL + "/" + route + "?key=" + get_http_key()


def uploadSettings():
    pot1 = {
        "PotName": "green", 
        "SensorI2CPort": 4, 
        "SensorPin": 2, 
        "RelayI2CPort": 4, 
        "RelayPin": 3, 
        "StartWaterning": 45, 
        "StopWatering": 70
     }
    return addSettings([pot1])


def _flatenPotArray(potArray, flatMap):
    if (len(potArray) == 0):
        return flatMap
    else:
        pot = potArray[0]
        idxStr = str(len(flatMap) // len(pot))
        for prop in pot:
            flatMap[prop+idxStr] = pot[prop]
        return _flatenPotArray(potArray[1:len(potArray)], flatMap)


def _unFlattenDictionary(dict):
    lists = {}
    for flatProp in dict:
        if flatProp not in ["dateTime", "id"]:
            prop, idx = _splitPropNameIdx(flatProp)
            _getDict(idx,lists)[prop] = dict[flatProp]
    return [lists[idx]
                for idx in lists]
        

def _getDict(idx, lists):
    if not idx in lists:
        lists[idx] = {}
    return lists[idx]


def _splitPropNameIdx(prop):
    return (prop[0:len(prop) - 1], prop[len(prop)-1: len(prop)])


def normalizeReading(rawReading):
    return round(100 - ((( rawReading - MIN_READING) / MAX_ADJUSTED_READING) * 100))
