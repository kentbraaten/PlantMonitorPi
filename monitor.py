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
    sleep(num_seconds_to_next_time_delta(15))
    try:
        while True:
            podMonitor.waterPotsIfNeeded(getSettingsForPots())
            sleep(num_seconds_to_next_time_delta(15))
    except Exception as e:
        writeError(e)

    
def getSettingsForPots():
    try:
        settings = waterLogClient.getSettings()
    except:
        pass
    return settings

logStart()
monitorPots()

