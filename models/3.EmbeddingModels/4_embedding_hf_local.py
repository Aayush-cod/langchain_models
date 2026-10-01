from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

# text = "Delhi is the capital of India."
documents = [
    "Delhi is the capital of India.",
    "Kathmandu is the capital of Nepal.",
    "Paris is the capital of France."
]

# vector = embeddings.embed_query(text)
vector = embeddings.embed_documents(documents)

print(str(vector))