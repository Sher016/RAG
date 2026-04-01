
from fastapi import HTTPException
from infrastructure.adapters.pdf_loader import PdfLoaderAdapter
from domain.services.genre_service import HuggingFaceGenreModel

def build_response(success: bool, message: str, data: dict = None, status_code: int = 200):
    payload = {"status": "success" if success else "error", "message": message}
    if success:
        payload["data"] = data or {}
        return payload
    else:
        raise HTTPException(status_code=status_code, detail=payload)
    

class DocumentAnalyzer:
    def __init__(self):
        self.pdf_loader = PdfLoaderAdapter()
        self.genre_model = HuggingFaceGenreModel()
        
    def chunk_text(self, text: str, max_length=1000):
        """Divide el texto en fragmentos de longitud máxima"""
        return [text[i:i+max_length] for i in range(0, len(text), max_length)]

    def analyze_genre(self, file_path: str):
        try:
            docs = self.pdf_loader.read_file(file_path)
            text_content = " ".join([doc.page_content for doc in docs])
            
            chunks = self.chunk_text(text_content,max_length=1000)
            
            summaries = [self.genre_model.summarize(chunk) for chunk in chunks]
            combined_summary = " ".join(summaries)

            genre_result = self.genre_model.classify(combined_summary, use_summary=False)

            return genre_result

        except Exception as e:
            return {
                "genre": None,
                "confidence": None,
                "error": f"Error analyzing document: {str(e)}"
            }
    
    
