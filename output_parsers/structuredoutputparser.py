from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.output_parsers import JsonOutputParser
from langchain_classic.output_parsers import StructuredOutputParser, ResponseSchema


load_dotenv()



model = ChatGroq(model = 'openai/gpt-oss-20b')

schema = [
    ResponseSchema(name = 'fact_1', description = "Fact 1 about topic."),
    ResponseSchema(name = 'fact_2', description = "Fact 2 about topic."),
    ResponseSchema(name = 'fact_3', description = "Fact 3 about topic.")
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template = 'Give 3 facts about {topic} \n {format_instructions}',
    input_variables = ['topic'],
    partial_variables = {'format_instructions':parser.get_format_instructions()}

)

# prompt = template.invoke({'topic':'black hole'})

# result = model.invoke(prompt)

# final_result = parser.parse(result.content)

# print(final_result)

chain = template | model | parser

result = chain.invoke({'topic':'black hole'})

print(result)




