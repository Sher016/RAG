class Document:
    def dict(self):
        return {
            "content": self.content,
            "metadata": self.metadata
        }