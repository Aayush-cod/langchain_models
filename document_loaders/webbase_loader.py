from langchain_community.document_loaders import WebBaseLoader
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model = 'openai/gpt-oss-20b')

parser = StrOutputParser()

template = PromptTemplate(
    template = 'Answer the following - \n {question} from the given  - \n {text}',
    input_variables = ['question', 'text']
)


url = 'https://www.flipkart.com/apple-macbook-air-m2-16-gb-256-gb-ssd-macos-sequoia-mc7x4hn-a/p/itmdc5308fa78421'
loader = WebBaseLoader(url)

docs = loader.load()

# print(len(docs))
# print(docs[0].metadata)

chain = template | model | parser

print(chain.invoke({'question':'Mention the specs about this product.','text': docs[0].page_content}))
