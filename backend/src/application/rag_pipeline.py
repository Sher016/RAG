

class RAGRunner:
    def __init__(self, rag_service):
        self.rag_service = rag_service

    def execute(self, file_path, query):
        return self.rag_service.run(file_path, query)
