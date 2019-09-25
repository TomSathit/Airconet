import libscrc

def mainRun():
    POWER_CODE="on"
    MODE_CODE ="cold"
    FAN_CODE  ="fan3"
    TEMP_CODE =20
    POWER = {"on": "55", "off": "AA"}
    MODE = {"cold": "11", "hot": "22", "auto": "33", "fan": "44", "dry": "55"}
    FAN = {"fan1": "01", "fan2": "02", "fan3": "03", "autofan": "00"}
    TEMP = {16: "00A0", 17: "00AA", 18: "00B4", 19: "00BE", 20: "00C8", 21: "00D2", 22: "00DC", 23: "00E6", 24: "00F0",
            25: "00FA", 26: "0104", 27: "010E", 28: "0118", 29: "0122", 30: "012C", 31: "0136", 32: "0140"}
    commandTX="01109C4000081000"+POWER[POWER_CODE]+"000000"+MODE[MODE_CODE]+"00"+FAN[FAN_CODE]+"00000000"+TEMP[TEMP_CODE]+"0B01"
    print(commandTX)
    crc16 = str(hex(libscrc.modbus(bytes.fromhex('01109C4000081000550000001100010000000000A00B01'))))
    crc16 = crc16[4:] + crc16[2:4]
    commandTX =  commandTX+crc16
    print(commandTX)
    k = bytes.fromhex(commandTX)
    print(k.decode('utf-8'))


if __name__=="__main__":
    mainRun()