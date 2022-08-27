import getpass

from requests import get
import modules.db_connection as dbc

import showGroupPrivileges

mycursor = dbc.mydb.cursor()


def verify_pass(username,typed_pass):

    search_pass_query = "SELECT password FROM user_details WHERE username = '%s'" % username
    mycursor.execute(search_pass_query)
    pass_in_db = mycursor.fetchone()[0]

    if pass_in_db == typed_pass:
        print("User verified....")
        editUser(username)

    else:
        print("Incorrect password...")

# Funtion to edit user details
def editUser(username):
    try:
        showGroupPrivileges.showGroupPrivileges()
        new_password = getpass.getpass("Enter new password: ")
        new_priv = int(input("Enter new group privilege id(Group name, Id  and privileges are given above): "))

        update_query = '''UPDATE user_details SET password='%s', group_name='%s' WHERE username = '%s' ''' % (new_password,new_priv,username,)

        mycursor.execute(update_query)
        dbc.mydb.commit()
        print("Profile updates successfully !...")
        return 1

    except Exception as e:
        dbc.mydb.rollback()
        print("Error: ",e)
        return 0

# get username and password to verify user
get_username = input("Enter username(for testing): ")
get_password = getpass.getpass("Enter password: ")

# fucntion to verify user
verify_pass(get_username,get_password)