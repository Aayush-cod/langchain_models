from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from pydantic import BaseModel , Field
from typing import Literal
from langchain_core.runnables import RunnableBranch, RunnableLambda, RunnablePassthrough


load_dotenv()

model = ChatGroq(model = 'openai/gpt-oss-20b')

class sentiment(BaseModel):
    sentiment : Literal['negative', 'positive'] = Field(description = "Give the sentiment of the feedback")

parser = StrOutputParser()
parser2 = PydanticOutputParser(pydantic_object = sentiment )

prompt1 = PromptTemplate(
    template='Classify the sentiment of the following feedback text into postive or negative \n {feedback} \n {format_instruction} ',
    input_variables=['feedback'],
    partial_variables = {'format_instruction': parser2.get_format_instructions()}

)

# using RunnablePassthrough.assign() to preserve the original feedback while adding the sentiment classification.
classifier_chain = RunnablePassthrough.assign(
    sentiment=prompt1 | model | parser2
)

print(classifier_chain.invoke({'feedback':'This is a terrible Phone.'}))

prompt2 = PromptTemplate(
    template='Write an appropriate response to this positive feedback \n {feedback}',
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template='Write an appropriate response to this negative feedback \n {feedback}',
    input_variables=['feedback']
)

branch_chain = RunnableBranch(
    #  (conditon1 , chain to execute)
     #  (conditon2 , chain to execute)
      #  Default chain

    #   (lambda x: x.sentiment == 'positive' , prompt2 | model | parser),
    #   (lambda x : x.sentiment == 'negative', prompt3 | model | parser),
    #   RunnableLambda(lambda x : 'could not find sentiment')

      (
        lambda x: x["sentiment"].sentiment == "positive",
        prompt2 | model | parser
    ),
    (
        lambda x: x["sentiment"].sentiment == "negative",
        prompt3 | model | parser
    ),
    RunnableLambda(lambda x: "Could not find sentiment")
)


chain = classifier_chain | branch_chain

print(chain.invoke({'feedback':'This is a terrible Phone.'}))

chain.get_graph().print_ascii()