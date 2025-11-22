from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings

emb = OpenAIEmbeddings()
store = Chroma(collection_name="resume", embedding_function=emb)


def add(text):
    store.add_texts([text])


def search(query):
    return store.similarity_search(query)
