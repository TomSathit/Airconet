import libscrc

crc16 = libscrc.modbus(bytes.fromhex('01109C4000081000550000001100010000000000A00B01'))
print(hex(crc16))
crc16 = libscrc.modbus(bytes.fromhex('010310005500AA002200020000010400A00B01'))
print(hex(crc16))