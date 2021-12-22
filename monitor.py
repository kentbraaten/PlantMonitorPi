import podMonitor
import waterLogClient
from time import sleep
from utils import num_seconds_to_next_time_delta, writeError


settings = []


def logStart():
    try:
        waterLogClient.addSystemEvent(waterLogClient.START_SYSTEM_EVENT)
    except:
        pass



def monitorPots():
    sleep(num_seconds_to_next_time_delta(30))
    while True:
        try:
            podMonitor.waterPotsIfNeeded(getSettingsForPots())
        except Exception as e:
            reportError(e)
        sleep(num_seconds_to_next_time_delta(30))


def logReadings():
    sleep(num_seconds_to_next_time_delta(60))
    while True:
        try:
            podMonitor.logSensorReadings(getSettingsForPots())
        except Exception as e:
            reportError(e)
        sleep(num_seconds_to_next_time_delta(30))
        

def reportError(e):
    try:
        writeError(e)
        waterLogClient.addSystemEvent(waterLogClient.ERROR_SYSTEM_EVENT)
    except:
        pass

    
def getSettingsForPots():
    try:
        settings = waterLogClient.getSettings()
    except:
        pass
    return settings

logStart()
monitorPots()

