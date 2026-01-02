# RAG PDF Agent

## Description
Retrieval-Augmented Generation (RAG) agent for working with PDF documents. Load, process, and query PDF files using vector databases and language models. Includes a Streamlit web interface for interactive use.
## Features
- Load and process PDF documents
- Store and search document embeddings in a vector database
- Query documents using LLM
- Streamlit web interface for interactive use
## Installation
 - Ensure Python 3.8+ is installed.
 - Docker desktop is installed
 - Clone this repository.
 - Create virtual environment:
	 ```bash
	 python -m venv pdf-agent-venv
	 ```
 - Install dependencies:
	 ```bash
	 pip install -r requirements.txt
	 ```
 - Vector Database Setup:
	 ```bash
	 docker run -d --name qdrantRagDb -p 6333:6333 -v "$(pwd)/qdrant_storage:/qdrant/storage" qdrant/qdrant
	 ```
## Usage
 - Place your PDF files in the appropriate directory.
 - Run the main application:
   - For CLI:
     ```bash
     python main.py
     ```
   - For Streamlit app:
     ```bash
     streamlit run streamlit_app.py
     ```
## Configuration
- Edit configuration variables in the code as needed (e.g., file paths, model settings).
- Set any required environment variables before running.

## File Structure
...
## Contributing
 - Pull requests are welcome.
 - For major changes, please open an issue first to discuss what you would like to change.

## License
MIT License. See LICENSE file for details.

## Contact / Support
For questions or support, please open an issue in this repository.

## Acknowledgements
- Inspired by open-source RAG and PDF processing projects.
# PDF Analyzer


<img width="713" height="822" alt="rag-ss-1" src="https://github.com/user-attachments/assets/2182041f-1044-419b-b6d9-4b8a31bb78d8" />
