import db_connection as dbc
import timestampRM  
mycursor = dbc.mydb.cursor()

try:
    print("Creating dumy_data table")
    query = ''' CREATE TABLE dumy_data (
                id INT AUTO_INCREMENT PRIMARY KEY,
                timstamp timestamp,
                Temp1 INT,
                Temp2 INT,
                Temp3 INT,
                Temp4 INT,
                Temp5 INT,
                Temp6 INT,
                Temp7 INT,
                Temp8 INT,
                Hum1 INT,
                Hum2 INT,
                Hum3 INT,
                Hum4 INT,
                Hum5 INT,
                Hum6 INT,
                Hum7 INT,
                Hum8 INT
                ) '''

    mycursor.execute(query)

    dbc.mydb.commit()

    print("successfull...")  
except Exception as err:
    print("Error creating dumy_data:",err)