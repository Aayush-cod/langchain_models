from langchain_community.document_loaders import DirectoryLoader , PyPDFLoader

loader = DirectoryLoader(
    path = 'document_loaders/books',
    # golb denotes which file to load like pdf or txt ..
    glob = '*.pdf',
    loader_cls = PyPDFLoader
)


# docs = loader.load()
docs = loader.lazy_load()

# print(len(docs))

# print(docs[0].page_content)
# print(docs[409].metadata)

for document in docs:
    print(document.metadata)

    