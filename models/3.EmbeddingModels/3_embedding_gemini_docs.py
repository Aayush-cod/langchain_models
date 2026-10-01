from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(model = 'gemini-embedding-001', dimensions = 32)

documents = [
    "Delhi is the capital of India.",
    "Kathmandu is the capital of Nepal.",
    "Paris is the capital of France."
]

result = embeddings.embed_documents(documents)

print(str(result))