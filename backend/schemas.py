from pydantic import BaseModel

class DocumentUploadResponse(BaseModel):
    id: int
    filename: str
    upload_date: str

class QuestionRequest(BaseModel):
    question: str
