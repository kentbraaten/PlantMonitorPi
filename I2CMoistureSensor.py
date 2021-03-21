from smbus2 import SMBus, i2c_msg
import struct

def get_sensor_reading(sensorAddress):
    i2CAddress, pin = sensorAddress
    bytes_to_send = pin.to_bytes(4,'big')
    returnVal = 0
    with SMBus(1) as bus:
        print("num bytes is " + str(len(bytes_to_send)))
        write = i2c_msg.write(i2CAddress, b'\x00' + bytes_to_send)
        read = i2c_msg.read(i2CAddress, 4)
        bus.i2c_rdwr(write, read)
        returnVal = bytes_to_int(read)
    return returnVal

def bytes_to_int(msg):
    result = 0
    for b in msg:
        result = result * 256 + int(b)
    return result;

address = (4,1)
print(get_sensor_reading(address))
