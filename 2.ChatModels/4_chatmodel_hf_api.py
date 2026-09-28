from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    # repo_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    # repo_id = "Qwen/Qwen2.5-1.5B-Instruct",
    repo_id = "ibm-granite/granite-4.2-30b",
    task = "text-generation"
)

model = ChatHuggingFace(llm=llm )

result = model.invoke("What is the capital of India")

print(result.content)