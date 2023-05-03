import db_connection as dbc
mycursor = dbc.mydb.cursor()

from noEndDate import *
from nostartdate import *
from bothDates import *
from allValues import *

def report(start_date, end_date, start_time, end_time):
    try:
        if(start_date == -1):
            nostartdate(end_date)
        elif (end_date == -1):
            nostartdate(start_date)
        elif (start_time == -1 and end_time == -1):
            bothDate(start_date, end_date)
        else: allValues(start_date, end_date, start_time, end_time)

        
        if os.path.exists('merged_report.pdf'):
            os.remove("merged_report.pdf")
    except Exception as e:
        print("Error: ",e)

if __name__ == "__main__":
    report("2022-08-02", "2022-08-05",-1,-1)