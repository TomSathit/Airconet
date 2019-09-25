import libscrc
import socket
def mainRun():
    server=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #server.bind(("192.168.22.167", 9534))

    # POWER={"on": 0x55,"off": 0xAA}
    # MODE={"cold": 0x11,"hot": 0x22,"auto" 0x33,"fan": 0x44,"dry": 0x55}
    # FAN={"fan1": 0x01,"fan2": 0x02,"fan3": 0x03,"autofan": 0x00}
    # TEMP={16: 0x00A0, 17: 0x00AA, 18: 0x00B4, 19: 0x00BE, 20: 0x00C8, 21: 0x00D2, 22: 0x00DC, 23: 0x00E6, 24: 0x00F0, 25: 0x00FA, 26: 0x0104, 27: 0x010E, 28: 0x0118, 29: 0x0122, 30: 0x012C, 31: 0x0136, 32: 0x0140}
    POWER_CODE="on"
    MODE_CODE ="cold"
    FAN_CODE  ="fan3"
    TEMP_CODE =16
    POWER = {"on": "55", "off": "AA"}
    MODE = {"cold": "11", "hot": "22", "auto" "33", "fan": "44", "dry": "55"}
    FAN = {"fan1": "01", "fan2": "02", "fan3": "03", "autofan": "00"}
    TEMP = {16: "00A0", 17: "00AA", 18: "00B4", 19: "00BE", 20: "00C8", 21: "00D2", 22: "00DC", 23: "00E6", 24: "00F0",
            25: "00FA", 26: "0104", 27: "010E", 28: "0118", 29: "0122", 30: "012C", 31: "0136", 32: "0140"}


    command="01109C4000081000"+POWER[POWER_CODE]+"000000"+MODE[MODE_CODE]+"00"+FAN[FAN_CODE]+"00000000"+TEMP[TEMP_CODE]+"0B01"
    print(command)
    crc16 = libscrc.modbus(bytes.fromhex('01109C4000081000550000001100010000000000A00B01'))

    addr = ("192.168.1.105", 20740)
    a = bytes.fromhex('01109C4000081000550000001100010000000000A00B0158d6')
    #     # while data!='q':

    server.sendto(a,addr)
        #
        # data,addr=server.recvfrom(1024)
        # data=data.decode('utf-8')
        # print("Massage From Server : "+data)
        # data=input("Input Command :")

if __name__=="__main__":
    mainRun()