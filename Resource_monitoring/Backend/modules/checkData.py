import modules.db_connection as dbc
import addAlert

mycursor = dbc.mydb.cursor()

def checkData(session_id, temperature , humidity):
    try:
        select_data_query = " SELECT temp_highest_level, temp_lowest_level, humidity_highest_level, humidity_lowest_level FROM session_data WHERE session_id = %s" % session_id
        
        mycursor.execute(select_data_query)
        data = mycursor.fetchone()


        high_temperature = int(data[0])
        low_temperature = int(data[1])
        high_humidity = int(data[2])
        low_humidity = int(data[3])

        print(high_temperature, low_temperature, high_humidity, low_humidity, temperature, humidity)

        temp_in_range = True
        humidity_in_range = True

        if temperature >= high_temperature or temperature <= low_temperature:
            temp_in_range = False
        
        if humidity >= high_humidity or humidity <= low_humidity:
            humidity_in_range = False

        return temp_in_range,humidity_in_range


    except Exception as e:
        print("Error: ",e)

print(checkData(459,36,25))