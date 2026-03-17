from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from domain.ports.ports import IChunker

class ChunkerAdapter(IChunker):
    def __init__(self, chunk_size=1000, chunk_overlap=100):
        self.text_splitter = RecursiveCharacterTextSplitter(
            separators=["\n\n", "\n", " ", ".", "。"],
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len,
            is_separator_regex=False
        )

    def chunk_docs(self, docs):
        list_docs = []
        for doc in docs:
            tmp = self.text_splitter.split_text(doc.page_content)
            for chunk in tmp:
                list_docs.append(Document(page_content=chunk, metadata=doc.metadata))
        return list_docs
