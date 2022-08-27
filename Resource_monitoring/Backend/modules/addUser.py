import getpass
import modules.db_connection as dbc

mycursor = dbc.mydb.cursor()



  # function to add/insert session data in database table session_data 
def addUser(user_details_dict):
  try:

    # Query to see is username exist
    search_username = "SELECT count(username) FROM user_details WHERE username = '%s'" % user_details_dict['username']
    mycursor.execute(search_username)
    get_count = mycursor.fetchall()[0][0]

    # if username doesn't exist 
    if get_count == 0:
      # MySql query insert dictionary data into session_data table in db
      insert_query =""" INSERT INTO user_details (username,password,group_name)
                        VALUES (%(username)s,%(password)s,%(group_name)s)"""
      
      mycursor.execute(insert_query,user_details_dict)

      dbc.mydb.commit()
      return print("Created User %s ....." % (user_details_dict['username']))

    # Error message for existing username
    else:
      print("Username exist please try another...")
      getCredentials()

    return 1

  except Exception as err:

    # rollback changes if error
    dbc.mydb.rollback()

    print("Error: ",err)

    return 0

try:
  def getCredentials():
    get_username = input('Enter Username: ')

    if " " in get_username:
      print("Error: Username should be of one word")
      getCredentials()

    else:
      get_password = getpass.getpass("Enter password: ")

      user_details_dict = {
          'username':get_username,
          'password':get_password,
          # By default group name is set to 1
          'group_name' : 1
      }
    addUser(user_details_dict)

except Exception as err:
  print("Error: ",err)

# getCredentials()
