import PyPDF2
from reportlab.pdfgen import canvas
import os

class DataReporting :
    def set_pdf_report_file_name(self, file_name):
        self.file_name = file_name

    def set_report_folder_path(self, path_to_folder):
        self.path_to_folder = path_to_folder

    def set_title(self, title):
        self.title = title

    def set_margin_from_left_side(self, left_margin):
        self.left_margin = left_margin

    def set_margin_from_top(self, top_margin):
        self.top_margin = top_margin

    def set_spacing_between_inputs(self, spacing):
        self.Y = spacing    
    
    def generate_pdf_report(self):
        pdf_writer = canvas.Canvas(os.path.join(self.path_to_folder, self.file_name))
        # Metadata
        pdf_writer.setAuthor("Jean-Louis Macle")
        pdf_writer.setTitle(self.title)

        # Content
        pdf_writer.drawString(self.left_margin, self.top_margin, self.title)
        pdf_writer.drawString(self.left_margin, self.top_margin, self.title.upper())

        pdf_writer.save()


