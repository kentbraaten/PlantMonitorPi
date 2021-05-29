import traceback
from os import path
import podMonitor
import pots
import waterLogClient
from time import sleep
from timeUtils import num_seconds_to_next_time_delta
import datetime


settings = pots.listOfPots


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
            

def writeError(e):
    f = open("error.txt","a") if path.exists("error.txt") else open("error.txt","w")
    with f:
        f.write(e.__class__)
        f.write("\n")
        f.write(traceback.format_exc())


    
def getSettingsForPots():
    try:
        settings = waterLogClient.getSettings()
    except:
        pass
    return settings

logStart()
monitorPots()

