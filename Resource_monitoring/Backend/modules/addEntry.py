import modules.db_connection as dbc

mycursor = dbc.mydb.cursor()

def addEntry(session_id):
    try:
        session_table_name = "session_%s" % session_id
        insert_query = "Insert into %s (temperature,humidity) values (34,26)" % session_table_name
        mycursor.execute(insert_query)

        dbc.mydb.commit()

        return 1
    except Exception as e:
        print("Error: ",e)
        return 0

print(addEntry('459'))