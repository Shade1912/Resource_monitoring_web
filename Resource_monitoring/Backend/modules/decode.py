# 02 - header | 01 -  0110010122162501072208021403

string = "020117070320001002030312345678"


# ========== DEFAULT DATA ==========
START  = string[0] + "" + string[1] 
HEADER = string[2] + "" + string[3] 
DATA_LENGTH = string[4] + "" + string[5]

# ========== DYNAMIC DATA ==========
# UID = string[6] + "" + string[7] +string[8] + "" + string[9]
# PROBE = string[10] 
# DATE = string[11] +""+ string[12]
# MONTH = string[13] + "" + string[14]
# YEAR = string[15] + "" + string[16] + "" + string[17] + "" +string[18]
# HOURS = string[19] + "" + string[20]
# MINUTES = string[21] + "" + string[22]
# SECONDS = string[23] + ""+ string[24]
# TEMPRATURE = string[25] + ""  + string[26] 
# HUMIDITY = string[27] + ""  + string[28] 
# END = string[29]+ "" + string[30]

if START == "02":
    DATA = string[6:int(DATA_LENGTH,16)+5]
    if HEADER == "01":
        UID = DATA[0:4]
        STATUS = DATA[4:6]
        print("device with UID:", UID , "has configuration:",STATUS )

    elif HEADER == "06":
        UID = DATA[0:4]
        PROBE = string[10] 
        DATE = string[11] +""+ string[12]
        MONTH = string[13] + "" + string[14]
        YEAR = string[15] + "" + string[16] + "" + string[17] + "" +string[18]
        HOURS = string[19] + "" + string[20]
        MINUTES = string[21] + "" + string[22]
        SECONDS = string[23] + ""+ string[24]
        TEMPRATURE = string[25] + ""  + string[26] 
        HUMIDITY = string[27] + ""  + string[28] 
        Time = HOURS+":"+MINUTES+":"+SECONDS 
        print("The data recieved from device ",UID,"is temperature:",TEMPRATURE,"and humidity:",HUMIDITY,"& the time is:",Time )