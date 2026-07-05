import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

# Use local embedding model - no internet needed
Settings.embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-en-v1.5"
)

# No LLM from llama_index - we call llama.cpp directly
Settings.llm = None

DOCS_PATH = os.path.join(os.path.dirname(__file__), "data/docs")
INDEX_PATH = os.path.join(os.path.dirname(__file__), "data/index")

def build_index():
    print("Loading documents...")
    documents = SimpleDirectoryReader(DOCS_PATH).load_data()
    print(f"Loaded {len(documents)} document chunks")
    print("Building vector index...")
    index = VectorStoreIndex.from_documents(documents)
    index.storage_context.persist(persist_dir=INDEX_PATH)
    print(f"Index saved to {INDEX_PATH}")
    return index

if __name__ == "__main__":
    build_index()
