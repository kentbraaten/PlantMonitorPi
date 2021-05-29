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
    while True:
        try:
            podMonitor.waterPotsIfNeeded(getSettingsForPots())
        except Exception as e:
            writeError(e)
            waterLogClient.addSystemEvent(waterLogClient.ERROR_SYSTEM_EVENT)
        sleep(num_seconds_to_next_time_delta(15))
        

    
def getSettingsForPots():
    try:
        settings = waterLogClient.getSettings()
    except:
        pass
    return settings

logStart()
monitorPots()

