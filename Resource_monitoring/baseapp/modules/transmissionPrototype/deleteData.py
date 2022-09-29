import modules.db_connection as dbc
mycursor = dbc.mydb.cursor()


try:
    print("Working...")
    #if db exist
    query = ''' DELETE FROM dumy_data ''' 

    mycursor.execute(query)

    dbc.mydb.commit()
    print("successfull...")                                              

except Exception as e:
    print("Error: ",e)