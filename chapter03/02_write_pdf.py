# Open a PDF file and add a blank page to it
from PyPDF2 import PdfFileReader, PdfFileWriter

infile = PdfFileReader(open('Exercise.pdf', 'rb'))
outfile = PdfFileWriter()
outfile.addBlankPage(612, 792)
p = infile.getPage(0)
outfile.addPage(p)
with open('myPdf.pdf', 'wb') as f:
    outfile.write(f)
f.close()


# Add a new page to a PDF file and add a table with certain text
from fpdf import FPDF

pdf = FPDF(format='letter')
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 20, txt="Welcome to the Jungle!", ln=1, align="C")
pdf.cell(200,20,'Created by Tomek',0,1,'C')
pdf.output("automateit.pdf")


# Merge multiple PDF files to one PDF file
from PyPDF2 import PdfFileReader, PdfFileMerger
import os

merger = PdfFileMerger()
files = [x for x in os.listdir('.') if (x.endswith('.pdf') and not x.startswith('Encrypt'))] # jest jeden zaszyfrowany plik, trzeba go pominąć
for fname in sorted(files):
    merger.append(PdfFileReader(open(os.path.join('.', fname), 'rb')))
merger.write("output.pdf")


# Create a PDF file and manage header and footer across pages
from fpdf import FPDF


class PDF(FPDF):
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 6)
        self.cell(0, 10, 'Page %s' % self.page_no(), 0, 0, 'C')

    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(80)
        self.cell(30, 10, 'Automate It!', 1, 0, 'C')
        self.ln(20)


pdf = PDF(format='A5')
pdf.add_page()
pdf.set_font("Times", size=8)
for i in range(1, 50):
    pdf.cell(0, 8, "This my new line. line number is: %s" % i, ln=1, align='C')
    
pdf.output("header_footer.pdf")
