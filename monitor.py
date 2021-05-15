import podMonitor
import pots
import waterLogClient

waterLogClient.addSystemEvent(waterLogClient.START_SYSTEM_EVENT)
podMonitor.monitorPots(waterLogClient.getSettings())
