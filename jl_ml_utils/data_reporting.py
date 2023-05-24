import PyPDF2
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os
import datetime

class DataReporting :
    def __init__(self):
        self.author = "Jean-Louis Macle"

    # Report path related functions
    def set_pdf_report_file_name(self, file_name):
        self.file_name = file_name

    def set_report_folder_path(self, path_to_folder):
        self.path_to_folder = path_to_folder    

    # Margins and spacing used within page
    def set_margin_from_left_side(self, left_margin):
        self.left_margin = left_margin

    def set_margin_from_top(self, top_margin):
        self.top_margin = top_margin

    def set_spacing_between_inputs(self, spacing):
        self.Y = spacing    

    # Setting the writer
    def set_pdf_writer(self):
        self.pdf_writer = canvas.Canvas(os.path.join(self.path_to_folder, self.file_name), 
                                   pagesize=letter, bottomup=0)

    # Functions related to the metadata
    def set_metadata_title(self, title):
        self.pdf_writer.setTitle(title)
        self.title = title

    def set_metadata_author(self, author):
        self.pdf_writer.setAuthor(author)
        self.author = author

    
    # Functions related to finishing a page and the document
    def finish_page(self):
        self.pdf_writer.showPage()

    def finish_document(self):
        self.pdf_writer.save()

    # Functions related to the first page of the report   
    def set_title(self):
        self.pdf_writer.drawCentredString(letter[0]/2, self.top_margin, self.title)

    def set_date(self):
        self.pdf_writer.drawString(self.left_margin, self.top_margin+self.Y*2, "Date: "+str(datetime.date.today()))
    
    def set_author(self):
        self.pdf_writer.drawString(self.left_margin, self.top_margin+self.Y*3, "Author: "+self.author)

    # Functions related to added string data

    def add_string_data(self, string_data, y_increment):
        self.pdf_writer.drawString(self.left_margin, self.top_margin+self.Y*y_increment, string_data)
        
    # Misc
    def add_page_number(self):
        self.pdf_writer.drawCentredString(letter[0]/2, 750, str(self.pdf_writer.getPageNumber()))

    def set_font(self, font_name, font_size):
        self.pdf_writer.setFont(font_name, font_size)
        

