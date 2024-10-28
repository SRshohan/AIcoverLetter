from langchain_community.vectorstores import Chroma # Importing Chroma vector store from Langchain
import shutil
import fitz
from fpdf import FPDF
import os


def generate_pdf(filled_cover_letter):
    # Generate PDF using FPDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Times", size=12)

    # Split the filled cover letter into lines and add to PDF
    for line in filled_cover_letter.split('\n'):
        pdf.cell(200, 10, txt=line, ln=True)

def extract_data(pdf_file):
    # Check if the PDF file exists
    if pdf_file:
        # Open the PDF file from the BytesIO object
        doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
        text = ""
        
        # Iterate over each page in the document and extract text
        for page in doc:
            text += page.get_text()

        return text
    else:
        return "No file uploaded."



# Path to the directory to save Chroma database

def save_to_chroma(chunks, embedding, CHROMA_PATH):
  """
  Save the given list of Document objects to a Chroma database.
  Args:
  chunks (list[Document]): List of Document objects representing text chunks to save.
  Returns:
  None
  """

  # Clear out the existing database directory if it exists
  if os.path.exists(CHROMA_PATH):
    shutil.rmtree(CHROMA_PATH)

  # Create a new Chroma database from the documents 
  db = Chroma.from_documents(
    chunks,
    embedding,
    persist_directory=CHROMA_PATH
  )

  # Persist the database to disk
  db.persist()
  print(f"Saved {len(chunks)} chunks to {CHROMA_PATH}.")

