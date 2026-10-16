from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader


# text = """ 
# LangChain is a framework for building applications
# powered by language models. Text splitting helps
# divide large documents into smaller chunks.
# """

loader = PyPDFLoader('document_loaders/dl-curriculum.pdf')

docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size = 50,
    # lets u repeat last 10 charcters of first chunk also in next chunks so the meaning or connection bteween chunks is meaningful lets say
    # chunk_overlap = 10,
    chunk_overlap = 0,
    separator = ''
)

# result = splitter.split_text(text)

result = splitter.split_documents(docs)

print(result[0].page_content)