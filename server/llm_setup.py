from langchain.prompts import PromptTemplate
from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import JsonOutputParser
from langchain_community.vectorstores import LanceDB
from langchain_experimental.text_splitter import SemanticChunker
from langchain.embeddings.huggingface import HuggingFaceEmbeddings  # for free embeddings
from setup_input import extract_data, generate_pdf, job_description


def localllm():
    local_llm="llama3.2:3b"
    # LLM
    llm = ChatOllama(model=local_llm, format="json", temperature=0)
    return llm

def embeddings():
    embedding = HuggingFaceEmbeddings(model_name = "BAAI/bge-small-en")  # or "BAAI/bge-large-en" for a larger model
    return embeddings


def text_splitter_semantic(document_text, embedding):
    #  Initilize Text splitter
    text_splitter = SemanticChunker(embedding)
    docs = text_splitter.create_documents([document_text])

    return docs
