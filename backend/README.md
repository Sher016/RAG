documentation > https://docs.langchain.com/oss/python/langchain/rag 

# 📄 Proyecto RAG 

Este proyecto implementa un sistema **RAG (Retrieval-Augmented Generation)** en Python

---

## Características
- Carga de documentos PDF con `PyMuPDFLoader`.
- Fragmentación de texto con `RecursiveCharacterTextSplitter`.
- Almacenamiento vectorial con FAISS y embeddings de Ollama.
- Recuperación de contexto y generación de respuestas con LLM.

---


## 🔧 Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tuusuario/proyecto-rag.git
   cd proyecto-rag
Crea un entorno virtual:

bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
Instala dependencias:

bash
pip install -r requirements.txt
##
Uso
Ejecuta el sistema RAG con:

bash
python main.p
