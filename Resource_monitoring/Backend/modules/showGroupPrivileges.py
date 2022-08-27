import modules.db_connection as dbc

mycursor = dbc.mydb.cursor()

def showGroupPrivileges():
    try:
        query = "SELECT *  FROM group_privileges"
        mycursor.execute(query)
        result = mycursor.fetchall()

        print("\nGroup name & their privileges")
        for row in result:
            index=0
            print("\nGroup ID:",row[0],"| Group Name:",row[1])
            for privilege in row:
                if privilege == 1 and index > 0:
                    print("-->"+(mycursor.description[index][0]),end="\n")
                index += 1
        return 1
        
    except Exception as e:
        print("Error: ",e)
        return 0