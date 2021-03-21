from smbus2 import SMBus, i2c_msg

def turn_on_valve(address):
    command = 1;
    i2cPort, pin = address
    bytesToSend = command.to_bytes(1,'big') + pin.to_bytes(4,'big')
    with SMBus(1) as bus:
        write = i2c_msg.write(i2cPort, bytesToSend)
        bus.i2c_rdwr(write)
        returnVal = 0x01 #read.buf[0]
        return returnVal

turn_on_valve((4,6))
