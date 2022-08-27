import modules.db_connection as dbc

mycursor = dbc.mydb.cursor()

def showUsers():

    try:
        get_users_query = "SELECT username FROM user_details"
        mycursor.execute(get_users_query)
        get_users = mycursor.fetchall()
        for users in get_users:
            print(users[0])
        return 1
    except Exception as e:
        return 0