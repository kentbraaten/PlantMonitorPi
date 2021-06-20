PotName = "PotName"
SensorI2CPort = "SensorI2CPort"
SensorPin = "SensorPin"
RelayI2CPort = "RelayI2CPort"
RelayPin = "RelayPin" 
StartWaterning = "StartWaterning" 
StopWatering = "StopWatering"

pot1 = {PotName: "Carrots", SensorI2CPort: 4, SensorPin: 1, RelayI2CPort: 4, RelayPin: 3, StartWaterning: 60, StopWatering: 75}
pot2 = {PotName: "Arugula", SensorI2CPort: 4, SensorPin: 2, RelayI2CPort: 4, RelayPin: 4, StartWaterning: 60, StopWatering: 75}


listOfPots = [pot1, pot2]

def toMoistureSensorParams(pot):
    return (pot[SensorI2CPort], pot[SensorPin])


def toRelayParams(pot):
    return (pot[RelayI2CPort], pot[RelayPin])


def toMoistureRange(pot):
    return (pot[StartWaterning], pot[StopWatering])


def potInfo(pot):
    sensorPort, sensorPin = toMoistureSensorParams(pot)
    relayPort, relayPin = toRelayParams(pot)
    potName = pot[PotName]
    sensorInfo = "(" + str(sensorPort) + "," + str(sensorPin) + ")"
    relayInfo = "(" + str(relayPort) + "," + str(relayPin) + ")"
    return pot[PotName] + ":  Sensor-" + sensorInfo + ":  " + "Relay-" + relayInfo
