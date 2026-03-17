from langchain_ollama import OllamaLLM
from domain.ports.ports import ILLM

class LLMAdapter(ILLM):
    def __init__(self, model="llama3.2:3b"):
        self.llm = OllamaLLM(model=model)

    def invoke(self, inputs):
        return self.llm.invoke(inputs)
