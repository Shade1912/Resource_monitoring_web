import modules.db_connection as dbc

mycursor = dbc.mydb.cursor()

def deleteDrug(drug_name):
    try:
        delete_query = "DELETE FROM drug_template WHERE name = '%s'" %(drug_name)

        mycursor.execute(delete_query)

        dbc.mydb.commit()
        
        print("Deleted session_data")
        return 1
    except Exception as e:
        dbc.mydb.rollback()
        print("Error: ",e)
        return 0

deleteDrug("Drug")