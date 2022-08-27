import modules.db_connection as dbc
import generateToken

mycursor = dbc.mydb.cursor()

try:
    def login(username,password):
        get_user_detail_query = ''' SELECT username, password from user_details WHERE username = '%s' and password = '%s' ''' % (username,password)
        mycursor.execute(get_user_detail_query)
    
        get_user = mycursor.fetchone()


        if get_user == None:
            print("Enter valid credentials")
        else:
            username = get_user[0]
            secret_token = generateToken.encodeToken(username)

            token_query = ''' UPDATE user_details SET session_tokens = '%s' WHERE  username = '%s' ''' % (secret_token, username)
            mycursor.execute(token_query)
            dbc.mydb.commit()

            print("Logged in successfully")
            return secret_token

        return 0

except Exception as err:
     print("Error: "+err)

login("vatsasdsal","vatsal")