from timestampRM import getTimestamp

def transmitOK(ser,Header,UID):
    response1 = "5a5d"+Header+"05"+UID+ "4f4b03"
    #response1 = bytes(response1,'utf-8')
    #response1 = int(response1,16)
    print(response1)
    packet = bytearray()
    for i in range(0,len(response1),2):
        value1 = str(response1[i]) +str(response1[i+1])
        print(value1)
        value1 = int(value1,base=16)
        print(value1)        
        packet.append(value1)
    
    ser.write(packet)


def transmitDeviceID(ser):
    response2 = "5a5d020312345603"
    packet = bytearray()
    for i in range(0,len(response2),2):
        value1 = str(response2[i]) +str(response2[i+1])
        print(value1)
        value1 = int(value1,base=16)
        print(value1)        
        packet.append(value1)
    ser.write(packet)
        

def transmitTimestamp(ser ):
    
    getTimestamp = getTimestamp()
    Date = getTimestamp[8:10] +  getTimestamp[5:7] + getTimestamp[0:4]
    Time = getTimestamp[11:13] + getTimestamp[14:16] + getTimestamp[17:19]
    response3 ="5a5d0307 " + Date + Time +" 03"

    print(response3)
    packet = bytearray()
    for i in range(0,len(response3),2):
        value1 = str(response3[i]) +str(response3[i+1])
        print(value1)
        value1 = int(value1,base=16)
        print(value1)        
        packet.append(value1)

    ser.write(packet)



def transmitStart(ser,UID):
    response= "5a5d0503" + UID + "0103"
    packet = bytearray()
    for i in range(0,len(response),2):
        value1 = str(response[i]) +str(response[i+1])
        print(value1)
        value1 = int(value1,base=16)
        print(value1)        
        packet.append(value1)
    ser.write(packet)

def transmitStop(ser,UID):
    response = "5a5d0503" + UID + "0003"
    packet = bytearray()
    for i in range(0,len(response),2):
        value1 = str(response[i]) +str(response[i+1])
        print(value1)
        value1 = int(value1,base=16)
        print(value1)        
        packet.append(value1)
    ser.write(packet)


def transmitProbeConfig(ser,UID,probe,status):
    response = "5a5d0406" + UID + probe + status + "15" + "03"
    packet = bytearray()
    for i in range(0,len(response),2):
        value1 = str(response[i]) +str(response[i+1])
        print(value1)
        value1 = int(value1,base=16)
        print(value1)        
        packet.append(value1)
    ser.write(packet)  