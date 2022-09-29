import db_connection as dbc

mycursor = dbc.mydb.cursor()

string = "5A5D0A0A12344F4B03"
newString = "5A5D061286400F0214160F172E2D3403"

# Function to convert hex to integer
def hexToInt(hexString):
    # Returning as string while converting as int 
    return str(int(hexString,16))
try:
    def decodeData(data):
        # ========== DEFAULT DATA ==========
        START  = data[0] + "" + data[1] + "" + data[2] + "" + data[3]
        HEADER = hexToInt(data[4]) + "" + hexToInt(data[5]) 
        DATA_LENGTH = int(hexToInt(data[6]) + hexToInt(data[7]))
        UID = None

        if START == "5A5D":
            DATA = data[8:int(DATA_LENGTH)+7]
            if DATA[4:8] == "4F4B":
                print("Header:",HEADER,"says Okay")

            if HEADER == "01":
                UID = DATA[0:4]
                STATUS = hexToInt(DATA[4:6])
                print("device with UID:", UID , "has configuration:",STATUS )

            elif HEADER == "06":
                UID = DATA[0:4]
                PROBE = hexToInt(data[10])
                DATE = hexToInt(data[12] +""+ data[13])
                MONTH = hexToInt(data[14] + "" + data[15])
                YEAR =   hexToInt(data[16] + "" + data[17]) + "" + hexToInt(data[18] + "" + data[19]) 
                HOURS = hexToInt(data[20] + "" + data[21])
                MINUTES = hexToInt(data[22] + "" + data[23])
                SECONDS = hexToInt(data[24] + ""+ data[25])
                TEMPRATURE = hexToInt(data[26] + ""  + data[27]) 
                HUMIDITY = hexToInt(data[28] + ""  + data[29])
                HEADER_TIME = HOURS+":"+MINUTES+":"+SECONDS 

                print("The data recieved from device ",UID,"is temperature:",TEMPRATURE,"and humidity:",HUMIDITY,"& the time is:",HEADER_TIME )
                
                # TIMESTAMPP = "2022-07-16 15:58:45"
                HEADER_TIMESTAMP = YEAR +"-"+ MONTH +"-"+ DATE +" "+ HEADER_TIME
                print(HEADER_TIMESTAMP)
                
                # if timestamp == is_already_present_in_db:
                #     then pass
                # else: create a row with new timestamp:

                if PROBE == "0":
                    temp_col = "Temp1"
                    hum_col = "Hum1"

                elif PROBE == "1":
                    temp_col = "Temp2"
                    hum_col = "Hum2"

                elif PROBE == "2" :
                    temp_col = "Temp3"
                    hum_col = "Hum3"

                elif PROBE == "3":
                    temp_col = "Temp4"
                    hum_col = "Hum4"

                elif PROBE == "4":
                    temp_col = "Temp5"
                    hum_col = "Hum5"

                elif PROBE == "5":
                    temp_col = "Temp5"
                    hum_col = "Hum5"

                elif PROBE == "6":
                    temp_col = "Temp7"
                    hum_col = "Hum7"

                elif PROBE == "7":
                    temp_col = "Temp8"
                    hum_col = "Hum8"

                probe_update(HEADER_TIMESTAMP,temp_col,hum_col,TEMPRATURE,HUMIDITY)

        else:
            print("Er1")

        return UID
except Exception as err:
    print("Error decoding:",err)

try:
    def probe_update(HEADER_TIME,temp_col,hum_col,Temp_value,Hum_value):
        query = ''' SELECT COUNT(timestamp) from dumy_data WHERE timestamp = "%s" ''' % (HEADER_TIME)

        mycursor.execute(query)
        count = mycursor.fetchall()[0][0]
        
        if count > 0:
            query = ''' UPDATE dumy_data SET %s = %s ,%s= %s WHERE timestamp ='%s' ''' % (temp_col,Temp_value,hum_col,Hum_value,HEADER_TIME)
            print("Probe set exist..")
        else:
            query = ''' INSERT INTO dumy_data (timestamp,%s,%s) VALUES('%s',%s,%s) ''' % (temp_col,hum_col,HEADER_TIME,Temp_value,Hum_value)
            print("Probe set data creating...")
        
        mycursor.execute(query)
        dbc.mydb.commit()
        print("Success")
except Exception  as err:
    print("Error", err)

# decodeData(newString)