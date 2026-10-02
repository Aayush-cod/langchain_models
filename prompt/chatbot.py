from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

# model = ChatGoogleGenerativeAI(model  ='gemini-3.8-flash')

# llm = HuggingFacePipeline.from_model_id(
#     model_id = 'TinyLlama/TinyLlama-1.1B-Chat-v1.0',
#     task = 'text-generation',
#     pipeline_kwargs = dict(
#             temperature = 0.5,
#             max_new_tokens = 100
#     )
# )

# model = ChatHuggingFace(llm = llm)


model = ChatGroq(model = 'openai/gpt-oss-20b')

chat_history = []

while True:
    user_input = input("You: ")
    chat_history.append({'role': 'user', 'content': user_input})

    if user_input == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append({'role': 'ai', 'content': result.content})

    print('AI: ', result.content)

print(chat_history)
