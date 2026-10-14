from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda

load_dotenv()


template = PromptTemplate(
    template = 'Write a joke about {topic}',
    input_variables = ['topic']
)

model = ChatGroq(model = 'openai/gpt-oss-20b')

parser = StrOutputParser()

def word_count(text):
    return len(text.split())


joke_chain = RunnableSequence(template , model , parser)

parallel_chain = RunnableParallel(
    {
        'joke':RunnablePassthrough(),
        'word_count':RunnableLambda(word_count)

    }
)



# parallel_chain = RunnableParallel(
#     {
#         'joke':RunnablePassthrough(),
#         'word-count':RunnableLambda(lambda x : len(x.split()))

#     }
# )


final_chain = RunnableSequence(joke_chain, parallel_chain)

result = final_chain.invoke({'topic':'AI'})

final_result = 'Joke- {} \n WordCount- {}'.format(result['joke'], result['word_count'])

print(final_result)