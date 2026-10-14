from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

from langchain_core.runnables import RunnableSequence, RunnableParallel

load_dotenv()

model = ChatGroq(model = 'openai/gpt-oss-20b')

template1 = PromptTemplate(
    template = 'Generate a tweet about {topic}',
    input_varibales = ['topic']
)

template2 = PromptTemplate(
    template = 'Gnerate a linkedn post about {topic}',
    input_variables = ['topic']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel(
    {
        'tweet': RunnableSequence(template1, model, parser),
        'linkedn':RunnableSequence(template2, model, parser)
    }
)

result = parallel_chain.invoke({'topic':'AI'})

print(result,'\n')

print(result['tweet'],'\n')

print(result['linkedn'],'\n')