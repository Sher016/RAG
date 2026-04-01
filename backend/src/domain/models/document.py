from pydantic import BaseModel

class Document:
    def dict(self):
        return {
            "content": self.content,
            "metadata": self.metadata
        }

class QueryRequest(BaseModel):
    query: str