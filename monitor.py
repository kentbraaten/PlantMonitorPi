import podMonitor
import pots
import waterLogClient
from time import sleep
import datetime


settings = pots.listOfPots


def logStart():
    try:
        waterLogClient.addSystemEvent(waterLogClient.START_SYSTEM_EVENT)
    except:
        pass



def monitorPots():
    sleep(find_time_delta_to_15())
    while True:
        podMonitor.waterPotsIfNeeded(getSettingsForPots())
        sleep(find_time_delta_to_15())

    
    
def getSettingsForPots():
    try:
        settings = waterLogClient.getSettings()
    except:
        pass
    return settings



def find_time_delta_to_15():
    now = datetime.datetime.now()
    seconds = 900 - ((now.minute * 60 + now.second) % 900)
    if (seconds == 0):
        return 900
    else:
        return seconds


logStart()
monitorPots()

