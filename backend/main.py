from fastapi import FastAPI, WebSocket, UploadFile, Depends, HTTPException
from fastapi_limiter import FastAPILimiter
from fastapi_limiter.depends import RateLimiter
from sqlalchemy.orm import Session
from .config import Config
from .models import Document
from .database import SessionLocal, init_db
from .services.pdf_processor import extract_text_from_pdf
from .services.nlp_service import answer_question
import os
import shutil

app = FastAPI()

# Initialize the database
@app.on_event("startup")
async def startup():
    init_db()
    await FastAPILimiter.init()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# PDF Upload Endpoint
@app.post("/upload", response_model=DocumentUploadResponse)
async def upload_pdf(file: UploadFile, db: Session = Depends(get_db)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")
    
    file_location = f"{Config.PDF_STORAGE_PATH}/{file.filename}"
    with open(file_location, "wb") as f:
        shutil.copyfileobj(file.file, f)

    text_content = extract_text_from_pdf(file_location)
    
    document = Document(filename=file.filename, text_content=text_content)
    db.add(document)
    db.commit()
    db.refresh(document)
    
    return DocumentUploadResponse(id=document.id, filename=document.filename, upload_date=document.upload_date)

# WebSocket Endpoint for Real-Time Q&A
@app.websocket("/ws/{document_id}")
async def websocket_endpoint(websocket: WebSocket, document_id: int, db: Session = Depends(get_db)):
    await websocket.accept()
    document = db.query(Document).filter(Document.id == document_id).first()
    if not document:
        await websocket.send_json({"error": "Document not found"})
        await websocket.close()
        return
    while True:
        try:
            data = await websocket.receive_text()
            question = data
            answer = answer_question(document.text_content, question)
            await websocket.send_json({"answer": answer})
        except Exception as e:
            await websocket.send_json({"error": str(e)})
            await websocket.close()
            break
