from langchain_core.prompts import PromptTemplate 
#from langchain_ollama import OllamaLLM 
from langchain_openai import OpenAI
from infrastructure.adapters.pdf_loader import PdfLoaderAdapter 
from infrastructure.adapters.chunker import ChunkerAdapter  
from infrastructure.adapters.vector_store import VectorStoreAdapter 


class RAG: 
    def __init__(self): 
        self.instructor_prompt = """Instrucción: Eres un experto solucionador de problemas.
        Responde la pregunta del usuario con el contexto proporcionado.
        Pregunta del usuario: {user_query} 
        Contexto de la respuesta: {answer_context} 
        """
        self.prompt = PromptTemplate.from_template(self.instructor_prompt) 
        #self.llm = OllamaLLM(model="llama3.2:3b") 
        self.llm = OpenAI(model="gpt-4.1") 
        self.vectorStore = VectorStoreAdapter() 
        self.pdfloader = PdfLoaderAdapter() 
        self.chunker = ChunkerAdapter() 

    def run(self, filePath, query): 
        docs = self.pdfloader.read_file(filePath) 
        list_docs = self.chunker.chunk_docs(docs) 
        self.vectorStore.add_docs(list_docs) 
        results = self.vectorStore.search_docs(query) 
        answer_context = "\n\n".join([res.page_content for res in results]) 
        chain = self.prompt | self.llm 
        response = chain.invoke({"user_query": query, "answer_context": answer_context}) 
        return response 

if __name__ == "__main__": 
    rag = RAG() 
    filePath = "narraciones_extraordinarias.pdf" 
    query = "¿De que tratan los cuentos y quien es el autor?" 
    response = rag.run(filePath, query) 
    print(response)
