import db_connection as dbc
mycursor = dbc.mydb.cursor()

from makingpdf import *
from splitpages import *

def noEndDate(start_date):

    try:
        query = ''' SELECT * FROM session_data
                    WHERE DATE(date) >= '%s' ''' %start_date

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
#     noEndDate("2022-07-27")
