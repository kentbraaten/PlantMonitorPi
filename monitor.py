import podMonitor
import pots
import waterLogClient

def logStart():
    try:
        waterLogClient.addSystemEvent(waterLogClient.START_SYSTEM_EVENT)
    except:
        pass

logStart()
podMonitor.monitorPots(waterLogClient.getSettings())
