from langchain_community.document_loaders import PyMuPDFLoader
from domain.ports.ports import IPdfLoader

class PdfLoaderAdapter(IPdfLoader):
    def read_file(self, file_path):
        loader = PyMuPDFLoader(file_path)
        return loader.load()
#devuelve los documentos cargados desde el pdf, cada página es un documento separado