from serialPort import serialPort
from readData import readData
from decodeData import decodeData
from transmit import *

serialData = serialPort()

Data = readData(serialData)

UID = decodeData(Data)

transmitOK(serialData,"01",UID)

transmitDeviceID(serialData)

transmitTimestamp(serialData)

transmitProbeConfig(serialData,UID,"00","01")

