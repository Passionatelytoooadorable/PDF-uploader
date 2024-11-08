import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_upload_pdf():
    with open("test_document.pdf", "rb") as pdf_file:
        response = client.post("/upload", files={"file": ("test_document.pdf", pdf_file, "application/pdf")})
    assert response.status_code == 200
    assert "filename" in response.json()
