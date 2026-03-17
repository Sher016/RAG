
class IPdfLoader:
    def read_file(self, file_path): pass

class IChunker:
    def chunk_docs(self, docs): pass

class IVectorStore:
    def add_docs(self, list_docs): pass
    def search_docs(self, query, k=5): pass

class ILLM:
    def invoke(self, inputs): pass
