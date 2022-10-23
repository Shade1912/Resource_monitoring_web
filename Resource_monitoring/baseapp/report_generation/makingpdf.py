import mysql.connector
from fpdf import FPDF
from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter
from splitpages import *

import db_connection as dbc
cursor = dbc.mydb.cursor()

def makingpdf(curr):

    try:
        for value in curr:

            session_ID = value[1]

            sql = '''SELECT * from session_%s;''' %session_ID

            cursor.execute(sql)

            result = cursor.fetchall()

            pdf=FPDF(format='A4', orientation='P', unit='mm')

            pdf.add_page()

            pdf.set_font('Times','',10.0) 

            epw = pdf.w - 2*pdf.l_margin

            col_width = epw/5                               # size of column
            line_height = pdf.font_size * 2.5

            data = (result)
            
            pdf.set_font('Times','B',22.0)              # font of heading
            pdf.cell(epw, 0.0, 'Session ID: %(id)s' %{'id':session_ID}, align='C')
            pdf.set_font('Times','',12.0)               # font of table data
            pdf.ln(8)
            
            th = pdf.font_size

            pdf.cell(col_width, 2*th, 'Number', border=1, align='C')
            pdf.cell(col_width, 2*th, 'Temperature', border=1, align='C')
            pdf.cell(col_width, 2*th, 'Humidity', border=1, align='C')
            pdf.cell(col_width, 2*th, 'Timestamp', border=1, align='C')
            pdf.ln(2*th)
            
            for row in data:
                for datum in row:
                    pdf.cell(col_width, 2*th, str(datum), border=1, align='C')          # to change data attributes of table
            
                pdf.ln(2*th)

            pdf.output('report_%s.pdf' %value[1],'F')

        merger = PdfFileMerger()

        for value in curr:
            merger.append('report_%s.pdf' %value[1])

        #Write out the merged PDF
        merger.write("merged_report.pdf")
        merger.close()

    except Exception as e:
        print("Error: ",e)