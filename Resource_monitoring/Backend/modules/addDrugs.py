import modules.db_connection as dbc

mycursor = dbc.mydb.cursor()

def addDrugs(drug_details):
    try:

        insert_group_previleges = """INSERT INTO drug_template (name,max_temperature,min_temperature,max_humidity,min_humidity) values (%(name)s,%(max_temp)s,%(min_temp)s,%(max_humidity)s,%(min_humidity)s )"""

        mycursor.execute(insert_group_previleges,drug_details)
        dbc.mydb.commit()
        
        return 1

    except Exception as e:

        dbc.mydb.rollback()
        print("Error: ",e)
        return 0



drug_details = {}
drug_details['name'] = "Drug"
drug_details['max_temp'] = 32.5
drug_details['min_temp'] = 32.5
drug_details['max_humidity'] = 32.5
drug_details['min_humidity'] = 32.5

# addDrugs(drug_details)