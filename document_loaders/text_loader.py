from langchain_community.document_loaders import TextLoader
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model = 'openai/gpt-oss-20b')

parser = StrOutputParser()

template = PromptTemplate(
    template = 'Write a summary on following poem - \n {poem}',
    input_variables = ['poem']
)

loader = TextLoader('document_loaders/cricket.txt', encoding = 'utf-8')

docs = loader.load()

print(type(docs))

print(len(docs))

print(type(docs[0]))

print(docs[0].page_content)

print(docs[0].metadata)


#Step1 : To add document loader as runnable lambda

# loaded_runnable = RunnableLambda(lambda x : docs[0].page_content)


#Step2 : To add document loader as runnable lambda
def load_document(_):
    docs = TextLoader('document_loaders/cricket.txt', encoding = 'utf-8').load()

    return docs[0].page_content
    
loaded_runnable = RunnableLambda(load_document)




chain = loaded_runnable | template | model | parser


#Step3 : To add document loader as runnable lambda
# Normal way directly invoking in template - chain = template | model | parser

# print(chain.invoke({'poem':docs[0].page_content}))

print(chain.invoke({}))