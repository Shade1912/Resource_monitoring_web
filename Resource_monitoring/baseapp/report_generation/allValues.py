import db_connection as dbc
mycursor = dbc.mydb.cursor()

from posixpath import split
from makingpdf import *
from splitpages import *

def allValues(start_date, end_date, start_time, end_time):

    try:
        query = ''' SELECT * FROM session_data WHERE 
                    date between '%s' and '%s' 
                    and session_start_time >= '%s'
                    and session_end_time <= '%s' ''' %(start_date,end_date, start_time, end_time)

        mycursor.execute(query)

        result = mycursor.fetchall()

        makingpdf(result)
        split_pages()

        for value in result:
            if os.path.exists('report_%s.pdf' %value[1]):
                os.remove('report_%s.pdf' %value[1])

    except Exception as e:
        print("Error: ",e)

# if __name__ == "__main__":
#     allValues("2022-07-20", "2022-07-27", "21:25:19", "21:25:19")