PotName, SensorI2CPort, SensorPin, RelayI2CPort, RelayPin, StartWaterning, StopWatering = range(0,7)

pot1 = {PotName: "Test", SensorI2CPort: 4, SensorPin: 1, RelayI2CPort: 4, RelayPin: 5, StartWaterning: 50, StopWatering: 75}


listOfPots = [pot1]

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
