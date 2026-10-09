from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.output_parsers import JsonOutputParser


load_dotenv()



model = ChatGroq(model = 'openai/gpt-oss-20b')

parser = JsonOutputParser()

template = PromptTemplate (
    template = "Give me the name, age and city of a fictional person \n {format_instruction}",
    input_variables = [],
    partial_variables = {'format_instruction': parser.get_format_instructions()}
)
prompt = template.format()

# print(prompt)

# result = model.invoke(prompt)

# final_result = parser.parse(result.content)


chain = template | model | parser

# As in template there is a input variable but empyt so even if there is no input field to fill still we have to send a empty dictionary
final_result = chain.invoke({})

print(final_result)
# print(final_result['name'])

print(type(final_result))


# Flaw or problem ; We can't enforce a  wished or own schema or json in json output parser -> Soln - Structured Output Parser - we can enforce predefined schemas