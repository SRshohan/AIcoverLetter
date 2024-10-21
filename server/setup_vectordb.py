from langchain.vectorstores.chroma import Chroma # Importing Chroma vector store from Langchain
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
    # Prepare the data for the template
    if os.path.exists(pdf_file):
        doc = fitz.open(pdf_file)
        text = ""
        for page in doc:
            text+=page.get_text()
        print(text)
        return text
    else:
        print("File doesnt exists!")


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

  # Create a new Chroma database from the documents using OpenAI embeddings
  db = Chroma.from_documents(
    chunks,
    embedding,
    persist_directory=CHROMA_PATH
  )

  # Persist the database to disk
  db.persist()
  print(f"Saved {len(chunks)} chunks to {CHROMA_PATH}.")

