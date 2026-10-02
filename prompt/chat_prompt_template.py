from langchain_core.prompts import ChatPromptTemplate


chat_template = ChatPromptTemplate(
    [
        ('system', 'You are a helful {domain} expert.'),
        ('human', 'Explain in terms, what is {topic}')
    ]
)

prompt = chat_template.invoke({
    'domain':'cricke',
    'topic':'bat'
})

print(prompt)



