import db_connection as dbc
mycursor = dbc.mydb.cursor()

from makingpdf import *
from splitpages import *

def bothDate(start_date, end_date):

    try:
        query = ''' SELECT * FROM session_data WHERE date between '%s' and '%s' ''' %(start_date,end_date)

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
#     bothDate("2022-07-21", "2022-07-30")
