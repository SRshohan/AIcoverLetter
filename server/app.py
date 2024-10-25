from llm_setup import convert_to_json, localllm, embeddings, text_splitter_semantic
from setup_RAG import query_rag
from setup_vectordb import generate_pdf, extract_data, save_to_chroma
from langchain_community.chat_models import ChatOllama


def generate_cover_letter_open_source(job_description, resume):
    generate_rag = query_rag("Find valuable information like job title, company name, company vison, goals & culture", "Chroma_jo")
    prompt = (f"Do the following steps: "
              f"1. Read the following job description,"
              f"2. Read the following resume, "
              f"3. Write a formal cover letter to the hiring manager for the job description based on the given resume, "
              # f"4. The cover letter MUST BE within {output_size_range[0]} to {output_size_range[1]} words. "
              # f"4. The cover letter MUST BE within 100 words. "
              f"4. Return ONLY the cover letter ONCE, nothing else. "
              f"Job Description: '{job_description}'. Resume: '{resume}'")

    # prompt = "What is an LLM"

    llm = ChatOllama(
    model="llama3.2:3b",
    temperature=0,
    # other params...
    )

    llm_response = llm.invoke(prompt)

    return llm_response
