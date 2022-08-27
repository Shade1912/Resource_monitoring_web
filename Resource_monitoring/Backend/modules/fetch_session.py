import modules.db_connection as dbc
from pprint import pprint 
mycursor = dbc.mydb.cursor()

def fetch_session(session_id):
    try:
        session_table_name = "session_%s" % session_id
        sql_query = "SELECT * FROM %s" % session_table_name

        mycursor.execute(sql_query)
        display_query = mycursor.fetchall()
        
        dbc.mydb.commit()

        return display_query


    except Exception as e:
        print("Error: ",e)
        return 0


pprint(fetch_session("459"))