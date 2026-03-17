
from fastapi import FastAPI, UploadFile, File
from domain.services.rag_service import RAG
from application.rag_pipeline import RAGRunner
from dotenv import load_dotenv

load_dotenv()
rag_service = RAG()
runner = RAGRunner(rag_service)

app = FastAPI()

@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    content = await file.read()
    
    return {"message": "File uploaded successfully", "filename": file.filename}
    
@app.post("/query")
async def query_document(file: UploadFile = File(...), query: str = ""):
    response = runner.execute(file, query)
    return {"response": response}