from smbus2 import SMBus, i2c_msg
import struct


def turn_on_valve(address):
    command = 1;
    i2cPort, pin = address
    bytesToSend = command.to_bytes(1,'big') + pin.to_bytes(4,'big')
    with SMBus(1) as bus:
        write = i2c_msg.write(i2cPort, bytesToSend)
        bus.i2c_rdwr(write)
        returnVal = 0x01 #read.buf[0]
        return returnVal

    
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
