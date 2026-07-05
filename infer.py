import subprocess
import sys
from llama_index.core import StorageContext, load_index_from_storage, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

Settings.embed_model = HuggingFaceEmbedding(model_name='BAAI/bge-small-en-v1.5')
Settings.llm = None

storage = StorageContext.from_defaults(persist_dir='data/index')
index = load_index_from_storage(storage)
retriever = index.as_retriever(similarity_top_k=3)

def ask(question):
    results = retriever.retrieve(question)
    context = "\n\n".join([r.text[:500] for r in results])
    prompt = "<|user|>\nYou are a Nigerian agricultural extension officer. Use the context to advise the farmer. Name the disease, explain the cause, give exact control measures.\n\nContext:\n" + context + "\n\nFarmer: " + question + "\n\nAdvice:<|end|>\n<|assistant|>\n"
    result = subprocess.run(
        ['/root/llama.cpp/build/bin/llama-cli',
         '-m', '/root/adtc-submission-repo/model/Phi-3-mini-4k-instruct-q4.gguf',
         '-p', prompt, '-n', '250', '--temp', '0.1', '-t', '4',
         '--no-display-prompt', '--log-disable'],
        capture_output=True, text=True
    )
    return result.stdout.strip()

if __name__ == "__main__":
    question = sys.argv[1] if len(sys.argv) > 1 else "What is the recommended NPK fertilizer for groundnut in Nigeria?"
    print(f"Q: {question}\n")
    print("A:", ask(question))
