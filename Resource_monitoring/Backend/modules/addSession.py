import random
import modules.db_connection as dbc
import datetime

mycursor = dbc.mydb.cursor()
# number/header/serial/probe/value/date/time/checksum/end - for sending data values

timestamp = datetime.datetime.now()
#For accessing db

#db_connection

# TEST - Random number generated for test ID of session data 
random_number = random.randint(0,500)


# TEST - test dictionary data for inserting in databasee
session_data_dict={
      'ip_address' : "192.168.18.90",
      'session_id' : random_number,
      'Number' : 123 ,
      'serial' : "12asa121a2",
      'probe' : 100,
      'date' : (timestamp.strftime("%Y-%m-%d")),
      'session_start_timestamp' : (timestamp.strftime("%X")),
      'session_end_timestamp' : (timestamp.strftime("%X")),
      'session_status' : "active",
      'temp_highest_level' : 35,
      'temp_lowest_level' : 33,
      'humidity_highest_level' : 35,
      'humidity_lowest_level' : 32,
}

try:

  # function to add/insert session data in database table session_data 
  def addSession(session_data_dict):

    # MySql query insert dictionary data into session_data table in db
    insert_query =""" INSERT INTO session_data (ipaddress,session_ID,Number,serial,probe,date,session_start_time,session_end_time,session_status,temp_highest_level,temp_lowest_level,humidity_highest_level,humidity_lowest_level)
                      VALUES (%(ip_address)s,%(session_id)s,%(Number)s,%(serial)s,%(probe)s,%(date)s,%(session_start_timestamp)s,%(session_end_timestamp)s,%(session_status)s,%(temp_highest_level)s,%(temp_lowest_level)s,%(humidity_highest_level)s,%(humidity_lowest_level)s)"""
    
    # MySql query insert dictionary data into backup_session_data table in db
    insert_query_for_backup =""" INSERT INTO backup_session_data (ipaddress,session_ID,Number,serial,probe,date,session_start_time,session_end_time,session_status,temp_highest_level,temp_lowest_level,humidity_highest_level,humidity_lowest_level)
                      VALUES (%(ip_address)s,%(session_id)s,%(Number)s,%(serial)s,%(probe)s,%(date)s,%(session_start_timestamp)s,%(session_end_timestamp)s,%(session_status)s,%(temp_highest_level)s,%(temp_lowest_level)s,%(humidity_highest_level)s,%(humidity_lowest_level)s)"""
    
    #Executing both query
    mycursor.execute(insert_query,session_data_dict)
    mycursor.execute(insert_query_for_backup,session_data_dict)

    # Creating session table for session data strored with column temperature, humidity and timestamp (N tables)
    try:
      session_name = "Session_%s" % session_data_dict['session_id']
      print(session_name)
      create_session_table = """ CREATE TABLE %s (id INT AUTO_INCREMENT PRIMARY KEY, temperature INT(3), humidity  INT(3), timestamp timestamp , CONSTRAINT unique_timestamp UNIQUE (timestamp) )""" % session_name
      mycursor.execute(create_session_table)
      dbc.mydb.commit()

      print("Session table %s created successfully" % session_name)

      return 1

    except Exception as e:
      # rollback changes if error
      dbc.mydb.rollback()
      print("Error creating session table:",e)
      return 0

    dbc.mydb.commit()


except Exception as err:

  # rollback changes if error
  dbc.mydb.rollback()

  print("Error: ",err)

# addSession(session_data_dict)