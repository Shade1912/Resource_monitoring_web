import os
from PyPDF2 import PdfMerger, PdfFileReader, PdfFileWriter
from addingwatermark import *

def split_pages():

    try:

        fname = 'merged_report.pdf'
        fh = open(fname, "rb")
        input = PdfFileReader(fh)

        # pdf = PdfFileReader(open('merged_report.pdf', 'rb'))
        # fh.close()

        for page in range(input.getNumPages()):

            fname = 'merged_report.pdf'
            fh = open(fname, "rb")
            input = PdfFileReader(fh)

            pdf_writer = PdfFileWriter()
            pdf_writer.addPage(input.getPage(page))

            output_filename = 'page_{}.pdf'.format(page+1)

            with open(output_filename, 'wb') as out:
                pdf_writer.write(out)

            # put_watermark('page_{}.pdf'.format(page+1), 'page_{}.pdf'.format(page+1), 'watermark.pdf')

            print('Created: {}'.format(output_filename))

            fh.close()

        fh.close()

        for page in range(input.getNumPages()):
            put_watermark('watermark.pdf', 'page_{}.pdf'.format(page+1), 'page_{}.pdf'.format(page+1))

        merger = PdfMerger()

        #Iterate over the list of file names
        # for pdf_file in pdf_files:
        for page in range(input.getNumPages()):
            #Append PDF files
            merger.append('page_{}.pdf'.format(page+1))

        #Write out the merged PDF
        merger.write("final_report.pdf")
        merger.close()

        for page in range(input.getNumPages()):
            if os.path.exists('page_{}.pdf'.format(page+1)):
                os.remove('page_{}.pdf'.format(page+1))

    except Exception as e:
        print("Error: ",e)

