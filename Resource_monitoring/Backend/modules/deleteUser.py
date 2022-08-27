import modules.db_connection as dbc 
import showUsers

mycursor = dbc.mydb.cursor()
def delete_session(username):
    try:
        search_user = "SELECT count(username) FROM user_details WHERE username = '%s'" % username
        mycursor.execute(search_user)
        row_count =  mycursor.fetchall()[0][0]

        if row_count > 0:
            delete_query = "DELETE FROM user_details WHERE username = '%s'" %(username)
            mycursor.execute(delete_query)
            dbc.mydb.commit()

            print("User Deleted")
        else:
            print("User not found")

        return 1

    except Exception as e:
        dbc.mydb.rollback()
        print("Error: ",e)
        return 0
        
showUsers.showUsers()
username_to_delete = input('Enter username to delete: ') 

confirm_delete = input('Are you sure you want to delete user '+ username_to_delete+' (y/n):')

if confirm_delete == 'y' or confirm_delete == 'Y':
    print("Deleting user "+username_to_delete+"...")
    delete_session(username_to_delete)
else:
    print("User not deleted")
