
from fastapi import FastAPI, UploadFile, File
from domain.services.rag_service import RAG
from application.rag_pipeline import RAGRunner
from dotenv import load_dotenv
from utils import build_response 
from utils import DocumentAnalyzer
import os
from domain.models.document import QueryRequest
from application.genre_pipeline import GenreRunner


load_dotenv()

rag_service = RAG()
runner = RAGRunner(rag_service)

app = FastAPI()
UPLOAD_DIR = "uploads"
CURRENT_FILE = None

@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    global CURRENT_FILE
    try:
        os.makedirs(UPLOAD_DIR, exist_ok=True)

        if CURRENT_FILE and os.path.exists(CURRENT_FILE):
            os.remove(CURRENT_FILE)

        path = os.path.join(UPLOAD_DIR, file.filename)
        with open(path, "wb") as f:
            f.write(await file.read())

        CURRENT_FILE = path
        
        # return build_response(True, "File uploaded successfully", {"filename": file.filename})
        genre_result = DocumentAnalyzer().analyze_genre(path)

        return build_response(
            True,
            "File uploaded successfully",
            {
                "filename": file.filename,
                "genre_analysis": genre_result 
            }
        )

    except Exception as e:
        return build_response(False, f"Error uploading file: {str(e)}", status_code=500)

@app.post("/query")
async def query_document(request: QueryRequest):
    
    query = request.query
    global CURRENT_FILE

    if not CURRENT_FILE or not os.path.exists(CURRENT_FILE):
        return build_response(False, "No document uploaded", status_code=400)

    if not query.strip():
        return build_response(False, "Query cannot be empty", status_code=400)

    try:
        response = runner.execute(CURRENT_FILE, query)
        return build_response(True, "Query executed successfully", {"response": response})
    except Exception as e:
        return build_response(False, f"Error processing query: {str(e)}", status_code=500) 