import socket
def mainRun():

    server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    server.bind(("",9533))
    print("Server Tom Start")
    while True:
        data, addr = server.recvfrom(1024)
        print(data)

        POWER = {"55": "on", "AA": "off"}
        MODE = {"11": "cold", "22": "hot", "33": "auto", "44": "fan", "55": "dry"}
        FAN = {"01": "fan1", "02": "fan2", "03": "fan3", "00": "autofan"}
        ERROR = {"00": "No error"}

        commandRX = ("".join("{:02x}".format(c) for c in data)).upper()
        print(commandRX)
        print(len(commandRX))
        if len(commandRX) == 42 :

            POWER_CODE=commandRX[8:10]
            print("power "+POWER[POWER_CODE])

            MODE_CODE=commandRX[16:18]
            print("mode "+MODE[MODE_CODE])

            FAN_CODE=commandRX[20:22]
            print("fan "+FAN[FAN_CODE])

            ERROR_CODE=commandRX[24:26]
            print("error "+ERROR[ERROR_CODE])

            ROOMTEMP_CODE=commandRX[26:30]
            print("roomtemp "+str((int(ROOMTEMP_CODE,16))/10))

            SETTEMP_CODE=commandRX[30:34]
            print("settemp "+str((int(SETTEMP_CODE,16))/10))



if __name__=="__main__":
    mainRun()


