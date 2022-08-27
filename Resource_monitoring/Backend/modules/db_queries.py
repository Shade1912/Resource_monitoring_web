import db_connection as dbc

print("Connection:",dbc.mydb)

mycursor = dbc.mydb.cursor()

# ========== Table queries ==========

# creating table for session_data
try:
    mycursor.execute('''CREATE TABLE session_data (Ipaddress char(30),
                                                    Session_ID char(10) primary key,
                                                    Number int(2),
                                                    serial char(20),  
                                                    probe char(20),
                                                    date date,
                                                    session_start_time char(15),
                                                    session_end_time char(15),
                                                    session_status char(15),
                                                    temp_highest_level char(5),
                                                    temp_lowest_level char(5),
                                                    humidity_highest_level char(5),
                                                    humidity_lowest_level char(5)),
                                                    time_interval time SET DEFAULT '00:15:00' '''
                                                    )
    print(""" Table session_data created........ """)                                              

except Exception as e:
    print("Error: ",e)



try:
    mycursor.execute('''CREATE TABLE backup_session_data (Ipaddress char(30),
                                                    Session_ID char(10) primary key,
                                                    Number int(2),
                                                    serial char(20),  
                                                    probe char(20),
                                                    date date,
                                                    session_start_time char(15),
                                                    session_end_time char(15),
                                                    session_status char(15),
                                                    temp_highest_level char(5),
                                                    temp_lowest_level char(5),
                                                    humidity_highest_level char(5),
                                                    humidity_lowest_level char(5))
                                                    time_interval time SET DEFAULT '00:15:00' '''
                                                    )
    print(""" Table backup_session_data created........ """)                                              

except Exception as e:
    print("Error: ",e)
    

# db query to create user details table
try:
    mycursor.execute('''CREATE TABLE user_details ( id INT AUTO_INCREMENT PRIMARY KEY,
                                                username char(50) unique key, 
                                                password char(50),
                                                group_name INTEGER,
                                                session_tokens chart(200),
                                                FOREIGN KEY (group_name) REFERENCES group_privileges(id)) ''')
    print(""" Table user_details created........ """)                                              
except Exception as e:
    print("Error: ",e)

#db query to create group_privileges table
try:
    mycursor.execute('''CREATE TABLE group_privileges ( id INT AUTO_INCREMENT PRIMARY KEY,group_name char(20), user_access_control boolean, print_report boolean, view_time_table boolean, view_channel_info boolean, create_user boolean, delete_user boolean, create_grp boolean, delete_grp boolean, grp_list boolean ,add_session boolean , delete_session boolean )''')
    print(""" Table group_privileges created........ """)                                              

except Exception as e:
    print("Error: ",e)




#db query to create Alerts table
try:
    print("Creating Alerts table")
    query = ''' CREATE TABLE alerts (
                        ID INT auto_increment primary key,
                        session_id char(10),
                        temperature float(2),
                        humidity float(2),
                        temperature_in_range bool,
                        humidity_in_range bool,   
                        FOREIGN KEY (session_ID) REFERENCES session_data(session_ID))'''

    mycursor.execute(query)

    dbc.mydb.commit()

    print("Alerts Table created successfully")                                              

except Exception as e:
    print("Error: ",e)

#db query to create drug_template table
try:
    print("Creating drug_template table")
    query = '''CREATE TABLE Drug_Template (
                        ID INT auto_increment primary key,
                        name char(100) unique key,
                        max_temperature float(3),
                        min_temperature float(3),
                        max_humidity float(3),
                        min_humidity float(3) )'''

    mycursor.execute(query)

    dbc.mydb.commit()

    print("drug_template Table created successfully")                                              

except Exception as e:
    print("Error: ",e)

#db query to create user logs table
try:
    print("Creating user logs table")
    query = ''' CREATE TABLE user_log (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username INTEGER,
                logs char(50),
                timestamp timestamp,
                FOREIGN KEY (username) REFERENCES user_details(id)
    ) '''

    mycursor.execute(query)

    dbc.mydb.commit()

    print("successfull...")                                              

except Exception as e:
    print("Error creating user log table: ",e)

# table - dumydata
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