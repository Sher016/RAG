import faiss
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings
from uuid import uuid4
from domain.ports.ports import IVectorStore

class VectorStoreAdapter(IVectorStore):
        
    def __init__(self, embeddings=None):
        #usa ollama por defecto, pero se puede configurar con embeddings de OpenAI u otros proveedores compatibles con Langchain
        if embeddings is None:
            embeddings = OllamaEmbeddings(model="llama3.2:3b")
        self.embeddings = embeddings
        self.persist_path = "faiss_index" #para no recalcular los embeddings cada vez
        
        try: 
            self.vector_store = FAISS.load_local(
                self.persist_path,
                self.embeddings,
                allow_dangerous_deserialization=True
            )
            
        except:
            #si no existe el índice, se crea uno nuevo
            dim = len(self.embeddings.embed_query("hola mundo"))
            self.index = faiss.IndexFlatL2(dim)
            self.vector_store = FAISS(
                embedding_function=self.embeddings,
                index=self.index,
                docstore=InMemoryDocstore(),
                index_to_docstore_id={}
            )

    def add_docs(self, list_docs):
        uuids = [str(uuid4()) for _ in range(len(list_docs))]
        self.vector_store.add_documents(documents=list_docs, ids=uuids)
        self

    def search_docs(self, query, k=5):
        return self.vector_store.similarity_search(query, k=k)
