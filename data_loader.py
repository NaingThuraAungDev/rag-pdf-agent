from google import genai
from llama_index.readers.file import PDFReader
from llama_index.core.node_parser import SentenceSplitter
from dotenv import load_dotenv


load_dotenv()

# Create a single client object
client = genai.Client()

EMBED_MODEL = "gemini-embedding-001"  # Example Gemini embedding model
EMBED_DIM = 3072  # Update to Gemini's embedding dimension if known

splitter = SentenceSplitter(chunk_size=1000, chunk_overlap=200)

def load_and_chunk_pdf(path: str):
    docs = PDFReader().load_data(file=path)
    texts = [d.text for d in docs if getattr(d, "text", None)]
    chunks = []
    for t in texts:
        chunks.extend(splitter.split_text(t))
    return chunks


def embed_texts(texts: list[str]) -> list[list[float]]:
    try:
        result = client.models.embed_content(
        model="gemini-embedding-001",
        contents=texts)
        print(f"Embedding succeeded for {len(texts)} texts.")
    
        return [v.values for v in result.embeddings] # Returns a list of lists
        
    except Exception as e:
        print(f"Embedding failed: {e}")
        return []