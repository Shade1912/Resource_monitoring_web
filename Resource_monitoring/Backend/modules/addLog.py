import db_connection as dbc


mycursor = dbc.mydb.cursor()

try:
    def addLog(username,log):
        insert_log_query = "INSERT INTO user_log (username, logs) VALUES('%s','%s')" % (username,log)
        mycursor.execute(insert_log_query)

        dbc.mydb.commit()

except Exception as err:
    print("Error in updating log: "+ err)

addLog(1,"Testing logs")