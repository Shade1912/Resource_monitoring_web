import transmissionPrototype.db_connection as dbc
from pprint import pprint 
mycursor = dbc.mydb.cursor()

def fetch_session():
    try:
        sql_query = "SELECT * FROM dumy_data"
        mycursor.execute(sql_query)
        display_query = mycursor.fetchall()
        
        dbc.mydb.commit()

        return display_query


    except Exception as e:
        print("Error: ",e)
        return 0


pprint(fetch_session())