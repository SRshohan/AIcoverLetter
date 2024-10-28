# AI-Powered Cover Letter Generator

This project is an AI-powered cover letter generator using the `ollama` model and Streamlit. The app extracts resume data from a PDF file, takes a job description as input, and generates a tailored cover letter using the `llama3.2:3b` model.

## Prerequisites

Ensure you have the following installed:
- Python 3.8 or higher
- `pip` (Python package installer)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-repo/cover-letter-generator.git
cd cover-letter-generator
```

2. Create and Activate a Virtual Environment
### On macOS/Linux:

```sh
python3 -m venv venv
source venv/bin/activate
```

### On Windows:
```sh
python -m venv venv
.\venv\Scripts\activate
```

3. Install Ollama CLI

### Ollama is needed to access the llama3.2:3b model

(Download Ollama)[https://ollama.com/download]

### Pull the Llama3.2:3b Model
### To use the llama3.2:3b model for generating cover letters, you need to pull the model:

```bash
ollama pull llama3.2:3b
```

5. Pull the Llama3.2:3b Model
```sh
pip install -r requirements.txt
```

6. Run the Streamlit Application
```sh
cd server
streamlit run app.py
```


### Explanation:
- **Virtual Environment Setup**: Instructions to create and activate a virtual environment depending on the operating system.
- **Ollama Installation**: Provides the command to install `ollama` using `pip`.
- **Pull Model**: Instructs how to pull the `llama3.2:3b` model using `ollama`.
- **Streamlit App**: Directs to navigate to the `server` folder and run the Streamlit app.
