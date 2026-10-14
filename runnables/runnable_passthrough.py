from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough

load_dotenv()


template = PromptTemplate(
    template = 'Write a joke about {topic}',
    input_variables = ['topic']
)

model = ChatGroq(model = 'openai/gpt-oss-20b')

parser = StrOutputParser()

template2 = PromptTemplate(
    template = 'Explain the joke - {text}',
    input_variables = ['text']
)


joke_chain = RunnableSequence(template , model , parser)

passthrough_explain_chain = RunnableParallel(
    {
        'joke': RunnablePassthrough(),
        'explanation':RunnableSequence(template2, model, parser)
    }
)

final_chain = RunnableSequence(joke_chain, passthrough_explain_chain)

print(final_chain.invoke({'topic':'football'}))