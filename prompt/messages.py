from langchain_core.messages import SystemMessage , HumanMessage, AIMessage
from langchain_groq import ChatGroq

from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model = 'openai/gpt-oss-20b')

messages = [
    SystemMessage(content = 'You are a helpful ai assistant'),
    HumanMessage(content='Tell me about langchain in one line and 10 words.')
]


result = model.invoke(messages)

messages.append(AIMessage(content = result.content))

print(messages)

