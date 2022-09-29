HEADER = "4652" 
DATA = "12345679"
DATALENGTH = str(len(DATA))

# 01 Broadcast (New Connection)
# 02 Device ID
# 03 Date and time
# 04 Probe Config
# 05 Start/Stop
# 06 Data
# 02 011707034F4B10020303123456 03

def encodeData(data):
    if HEADER == "01":
        pass
    elif HEADER == "02":
        pass
    elif HEADER == "03":
        pass
    elif HEADER == "04":
        pass
    elif HEADER == "05":
        pass
    elif HEADER == "06":
        pass

DATATEST = "02" + HEADER + DATALENGTH + DATA + "03"

print(DATATEST)