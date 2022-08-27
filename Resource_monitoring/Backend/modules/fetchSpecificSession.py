import modules.db_connection as dbc

mycursor = dbc.mydb.cursor()



def displaySession():
    try:
        sql_query = "SELECT serial,ipaddress,session_ID FROM session_data"
        mycursor.execute(sql_query)
        display_query = mycursor.fetchall()
        
        dbc.mydb.commit()

        return display_query


    except Exception as e:
        return 0

# print(displaySession()[0][0])