from langchain.prompts import ChatPromptTemplate
from langchain.vectorstores.chroma import Chroma # Importing Chroma vector store from Langchain
import shutil
import os



def query_rag(query_text, CHROMA_PATH):
    """
    Query a Retrieval-Augmented Generation (RAG) system using Chroma database and OpenAI.
    Args:
        - query_text (str): The text to query the RAG system with.
    Returns:
        - formatted_response (str): Formatted response including the generated text and sources.
        - response_text (str): The generated response text.
    """
    # Ensure embedding function is initialized
    embedding_function = embedding

    # Prepare the database
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    # Retrieving the context from the DB using similarity search
    results = db.similarity_search_with_relevance_scores(query_text, k=3)



    # Check if there are any matching results or if the relevance score is too low
    if len(results) == 0 or results[0][1] < 0.5:  # Lower the threshold for testing
        return "Unable to find matching results.", None

    # Combine context from matching documents
    context_text = "\n\n - -\n\n".join([doc.page_content for doc, _score in results])

    # Create prompt template using context and query text
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)

    # Generate response text based on the prompt
    response_text = llm.predict(prompt)  # Get the raw text response (not JSON)


    # # Format and return response including generated text and sources
    formatted_response = f"{response_text}"
    return formatted_response