from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser


load_dotenv()


# llm = HuggingFaceEndpoint(
#     repo_id = "ibm-granite/granite-4.2-30b",
#     task = "text-generation"
# )

# model = ChatHuggingFace(llm=llm)

model = ChatGroq(model = 'openai/gpt-oss-20b')

#1st promot - > detailed prompt
template1 = PromptTemplate(
    template = "Write a detailed report on {topic}.",
    input_variables = ['topic']
)

#2nd prompt - > summary
template2 = PromptTemplate(
    template = "Write a 5 line summary on the following text {text}.",
    input_variables = ['text']
)


parser = StrOutputParser()

# /* Your original chain works because each component passes its output to the next component, and template2 has only one required variable. If you introduce more variables, you must ensure those values are supplied to template2 rather than expecting LangChain to invent or retrieve them automatically. */

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({'topic':'BlackHole'})

print(result)
