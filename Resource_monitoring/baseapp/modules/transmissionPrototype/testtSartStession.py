from serialPort import serialPort
from readData import readData
from decodeData import decodeData
from transmit import *

try:
    def startSession():
        get_message = ""
        # serialData = serialPort()

        # Data = readData(serialData)

        UID = decodeData("5A5D061286400F0214160F172E2D3403")

        # transmitOK(serialData,"01",UID)

        # transmitDeviceID(serialData)

        NEW_DATA = "Hellp" #readData(serialData)
        serialData = "test"
        loop = 5
        while True:
            if NEW_DATA[4:10] != "4f4b03":
                # transmitDeviceID(serialData)
                print(NEW_DATA[4:10])
                NEW_DATA = "5A5D4f4b03" #readData(serialData)
                print(NEW_DATA[4:10])
                print("Try",loop)
            else:
                get_message += "\nTransmit device ID status - OK" 
                NEW_DATA = "Hellp" 
                break
            loop = loop - 1
            if loop == 0:
                repeat = input("Transmit device ID failed, do you want to try again ?(y/n)")
                if repeat == "n":
                    get_message = "Transmit device ID failed"
                    return get_message
                else:
                    loop = 5
            
        # transmitTimestamp = transmitTimestamp(serialData)
        # NEW_DATA = readData(serialData)

        loop = 5
        while True:
            if NEW_DATA[4:10] != "4f4b03":
                # transmitTimestamp(serialData)
                NEW_DATA = "5A5D4f403" #readData(serialData)
                print(NEW_DATA[4:10])
                print("Try",loop)
            else:
                get_message += "\nTransmit timestamp status - OK" 
                NEW_DATA = "Hellp" 
                break
            loop = loop - 1
            if loop == 0:
                repeat = input("Transmit timestamp failed, do you want to try again ?(y/n)")
                if repeat == "n":
                    get_message += "\nTransmit timestamp failed"
                    return get_message
                else:
                    loop = 5

        loop = 5
        while True:
            if NEW_DATA[4:10] != "4f4b03":
                # [ transmitProbeConfig(serialData,UID,"00","01") for _ in range(8) ]
                NEW_DATA = "5A5D4f03" #readData(serialData)
                print(NEW_DATA[4:10])
                print("Try",loop)
            else:
                get_message += "\nTransmit Probe Config status - OK" 
                break
            loop = loop - 1
            if loop == 0:
                repeat = input("Transmit Probe Config failed, do you want to try again ?(y/n)")
                if repeat == "n":
                    get_message += "\nTransmit Probe Config Failed"
                    return get_message
                else:
                    loop = 5

        return get_message

except Exception as err:
    print("Error",err)

print(startSession())