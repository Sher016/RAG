import faiss
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings
from uuid import uuid4
from domain.ports.ports import IVectorStore

class VectorStoreAdapter(IVectorStore):
    def __init__(self):
        self.embeddings = OllamaEmbeddings(model="llama3.2:3b")
        self.index = faiss.IndexFlatL2(len(self.embeddings.embed_query("hola mundo")))
        self.vector_store = FAISS(
            embedding_function=self.embeddings,
            index=self.index,
            docstore=InMemoryDocstore(),
            index_to_docstore_id={}
        )

    def add_docs(self, list_docs):
        uuids = [str(uuid4()) for _ in range(len(list_docs))]
        self.vector_store.add_documents(documents=list_docs, ids=uuids)

    def search_docs(self, query, k=5):
        return self.vector_store.similarity_search(query, k=k)
