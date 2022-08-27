import modules.db_connection as dbc

mycursor = dbc.mydb.cursor()

def deleteGroup(group_name):
    try:
        delete_query = "DELETE FROM group_privileges WHERE group_name = '%s' " % group_name
        mycursor.execute(delete_query)
        dbc.mydb.commit()
        return 1
    except Exception as e:
        return 0


deleteGroup("Admin2")