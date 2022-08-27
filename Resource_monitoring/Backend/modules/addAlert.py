import modules.db_connection as dbc

mycursor = dbc.mydb.cursor()

def addAlert(session_id, temperature, humidity, temperature_in_range, humidity_in_range):
    try:
        query = """ INSERT INTO alerts (session_id, temperature, humidity, temperature_in_range, humidity_in_range ) VALUES (%s, %s, %s, %s, %s) """ % (session_id,temperature,humidity,temperature_in_range,humidity_in_range)
        
        mycursor.execute(query)

        dbc.mydb.commit()

    except Exception as e:
        print("Error: ",e)

# addAlert(459,36,25,False,False)