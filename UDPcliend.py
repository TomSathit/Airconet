import libscrc
import socket
def mainRun():
    server=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #server.bind(("192.168.22.167", 9534))
    addr = ("192.168.43.78", 20740)

    POWER_CODE = "off"
    MODE_CODE = "cold"
    FAN_CODE = "fan3"
    TEMP_CODE = 27
    POWER = {"on": "55", "off": "AA"}
    MODE = {"cold": "11", "hot": "22", "auto": "33", "fan": "44", "dry": "55"}
    FAN = {"fan1": "01", "fan2": "02", "fan3": "03", "autofan": "00"}
    TEMP = {16: "00A0", 17: "00AA", 18: "00B4", 19: "00BE", 20: "00C8", 21: "00D2", 22: "00DC", 23: "00E6", 24: "00F0",
            25: "00FA", 26: "0104", 27: "010E", 28: "0118", 29: "0122", 30: "012C", 31: "0136", 32: "0140"}

    if POWER_CODE == "off":
        command = "01069C4000AA2631"
        print(command)
    elif POWER_CODE == "on":
        command = "01069C4000556671"
        print(command)
    else:
        command = "01109C4000081000" + POWER["on"] + "000000" + MODE[MODE_CODE] + "00" + FAN[FAN_CODE] + "00000000" + \
                  TEMP[TEMP_CODE] + "0B01"
        print(command)
        crc16 = str(hex(libscrc.modbus(bytes.fromhex(command))))
        crc16 = crc16[4:] + crc16[2:4]
        command = command + crc16


    print(command)
    print(len(command))
    a = bytes.fromhex(command) # a = bytes.fromhex('01109C4000081000550000001100010000000000A00B0158d6')
    #     # while data!='q':
    print(a)
    server.sendto(a,addr)
        # data,addr=server.recvfrom(1024)
        # data=data.decode('utf-8')
        # print("Massage From Server : "+data)
        # data=input("Input Command :")

if __name__=="__main__":
    mainRun()
