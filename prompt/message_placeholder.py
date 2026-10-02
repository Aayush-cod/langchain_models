from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


chat_template = ChatPromptTemplate(
    [
        ('system', 'You are a helpful sustomer support agent'),
        MessagesPlaceholder(variable_name = 'chat_history'),
        ('human', 'where is my refund?')

    ]
)


chat_history = []

with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())

prompt = chat_template.invoke({'chat_history': chat_history})

print(prompt)