from langchain_core.runnables import RunnableLambda


def word_count(text):
    return len(text.split())


runnable_wordcount = RunnableLambda(word_count)

print(runnable_wordcount.invoke('Hi I am Aayush Bohara.'))