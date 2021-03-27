from enum import Enum

PotName, SensorI2CPort, SensorPin, RelayI2CPort, RelayPin, StartWaterning, StopWatering = range(0,7)

pot1 = {PotName: "Arugula", SensorI2CPort: 20, SensorPin: 3, RelayI2CPort: 20, RelayPin: 1, StartWaterning: 50, StopWatering: 75}
pot2 = {PotName: "Letus", SensorI2CPort: 20, SensorPin: 4, RelayI2CPort: 20, RelayPin: 2, StartWaterning: 40, StopWatering: 65}
pot3 = {PotName: "Basil", SensorI2CPort: 20, SensorPin: 5, RelayI2CPort: 20, RelayPin: 3, StartWaterning: 30, StopWatering: 50}

ListOfPots = [pot1, pot2, pot3]

def ToMoistureSensorParams(pot):
    return (pot[SensorI2CPort], pot[SensorPin])

def ToRelayParams(pot):
    return (pot[RelayI2CPort], pot[RelayPin])

def ToMoistureRange(pot):
    return (pot[StartWaterning], pot[StopWatering])

