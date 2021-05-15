import podMonitor
import pots
import waterLogClient
from time import sleep

def logStart():
    try:
        waterLogClient.addSystemEvent(waterLogClient.START_SYSTEM_EVENT)
    except:
        pass

sleep(900)
logStart()
podMonitor.monitorPots(waterLogClient.getSettings())
