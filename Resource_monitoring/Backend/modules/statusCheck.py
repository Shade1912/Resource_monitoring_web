import modules.db_connection as dbc
from datetime import datetime

mycursor = dbc.mydb.cursor()

# check - wheather the current time and time of last entry has a difference of more than given time


def statusCheck(session_id):
    
    try:

        session_status_query = "SELECT session_status FROM session_data WHERE session_id = %s" % session_id
        mycursor.execute(session_status_query)
        session_status = mycursor.fetchone()
        print(session_status[0])

        session_table_name = "session_%s" % session_id
        recent_timestamp = "SELECT timestamp from %s ORDER BY id DESC" % session_table_name
        mycursor.execute(recent_timestamp)

        recent_session_timestamp = mycursor.fetchone()[0].timestamp() * 1000
        time_now = datetime.now().timestamp() * 1000

        print(recent_session_timestamp, time_now)

        diff_in_time = time_now - recent_session_timestamp 

        if diff_in_time <= 900000:
            print("Active")
        else:
            print("Inactive")


    except Exception as e:
        print("Error: ",e)


statusCheck(459)