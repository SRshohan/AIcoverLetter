import fitz
from fpdf import FPDF


def generate_pdf(filled_cover_letter):
    # Generate PDF using FPDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Times", size=12)

    # Split the filled cover letter into lines and add to PDF
    for line in filled_cover_letter.split('\n'):
        pdf.cell(200, 10, txt=line, ln=True)

def extract_data(pdf_file):
    # Prepare the data for the template
    doc = fitz.open(pdf_file)
    text = ""
    for page in doc:
        text+=page.get_text()
    print(text)
    return text