import modules.db_connection as dbc 


mycursor = dbc.mydb.cursor()
def deleteSession(delete_id_list):
    try:

        for id in delete_id_list:
            print(id)
            delete_query = "DELETE FROM session_data WHERE session_ID = %s" %(id)
            mycursor.execute(delete_query)

            # Drop session table -
            # session_table = "session_%s" % id
            # try:
            #     drop_table_query = "DROP TABLE %s" % session_table
            #     mycursor.execute(drop_table_query)
            #     
            #     print("Deleted session table %s" % session_table)

            # except Exception as e:
            #     pass
        dbc.mydb.commit()
        print("Deleted session_data")
        return 1
    except Exception as e:
        dbc.mydb.rollback()
        print("Error: ",e)
        return 0

# delete_id_list = [] 

# deleteSession(delete_id_list)