import streamlit as st
import datetime
from langchain_community.chat_models import ChatOllama
from setup_vectordb import extract_data
import fitz

# Function to generate cover letter
def generate_cover_letter_open_source(job_description, resume):
    name = 'Sohanur'
    address = "Bronx, New York, 10462"
    email = "srahman06@manhattan.edu"
    phone = "(929) 412 6398"
    date = datetime.date.today()

    # Create the prompt for the LLM
    prompt = (f"Imagine you are a world-renowned career strategist with decades of experience in creating compelling resumes that have helped countless individuals land their dream jobs. "
              f"Your expertise lies in crafting resumes that not only showcase a candidate's skills and experiences but also weave in their unique story in a way that resonates with leading employers across various industries. "
              f"Your secret lies in your ability to humanize each resume, transforming it into a narrative that highlights the candidate’s journey, achievements, and aspirations.\n\n"
              f"1. Read the following job description, like job titles, company name, responsibility culture, etc.\n"
              f"2. Read the following resume.\n"
              f"3. Write a formal cover letter to the hiring manager for the job description based on the given resume. Include 4 paragraphs: "
              f"a) An intro with the job title and resume summary, "
              f"b) 2 paragraphs highlighting experience related to the resume and job description, "
              f"c) A final paragraph explaining why the company might be interested in the candidate based on the given company info.\n"
              f"Return ONLY a cover letter with the following structure:\n"
              f"{name}\n{address}\n{email}\n{phone}\n{date}\n\n"
              f"Job Description: '{job_description}'. Resume: '{resume}'")

    # Initialize the language model
    llm = ChatOllama(model="llama3.2:3b", temperature=0)
    llm_response = llm.invoke(prompt)

    return llm_response

# Streamlit app
st.title('AI-Powered Cover Letter Generator')

# Input fields for the job description
job_description = st.text_area("Enter the Job Description", height=300)

# Upload PDF for the resume
uploaded_file = st.file_uploader("Upload Your Resume (PDF)", type="pdf")

if uploaded_file:
    # Extract resume data from PDF
    resume_text = extract_data(uploaded_file)

    # Display the extracted resume for confirmation
    st.subheader("Extracted Resume:")
    st.text(resume_text)

# Generate button
if st.button('Generate Cover Letter'):
    if job_description and uploaded_file:
        cover_letter = (generate_cover_letter_open_source(job_description, resume_text)).content
        st.subheader("Generated Cover Letter:")
        st.write(cover_letter)
    else:
        st.error("Please enter the job description and upload your resume.")
