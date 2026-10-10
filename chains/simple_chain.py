from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = PromptTemplate(
    template = 'Generate 5 interesting facts about {topic}',
    input_variables = ['topic']
)

model = ChatGroq(model = 'openai/gpt-oss-20b')

parser = StrOutputParser()

# LCEL(langchain expression language) - we use pipe operator - |
chain = prompt | model | parser

result = chain.invoke({'topic':'Cricket'})

print(result)

# This code helps u vizualize your chain pipeline - how it is flowing or working step by step
chain.get_graph().print_ascii()

