# PDF Document Question Answering Backend with Real-time WebSocket

This project is a backend service that allows users to upload PDF documents and ask questions based on the content of these documents. It uses Natural Language Processing (NLP) to process the documents and provides real-time answers via WebSocket. The backend is built using **FastAPI** and **WebSocket**, with **LangChain** or **LlamaIndex** for document analysis. The frontend is built using **React** for a smooth user experience.

## Features
- **PDF Upload**: Users can upload PDF documents, which are processed for further querying.
- **Real-time Question Answering**: Using WebSockets, users can ask questions and get answers based on the content of the uploaded PDF document.
- **Session-based Context**: The backend maintains context for follow-up questions within a WebSocket session.
- **Rate Limiting**: Protects the API and WebSocket connections from excessive requests using rate limiting.

## Technologies Used
- **Backend**: FastAPI, WebSocket
- **NLP Processing**: LangChain, LlamaIndex
- **Database**: SQLite or PostgreSQL for metadata storage
- **File Storage**: Local filesystem or AWS S3 for storing PDFs
- **Frontend**: React
- **Testing**: Pytest, Unittest for API and WebSocket testing

## Setup Instructions

### Backend Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/pdf-question-answering-backend.git
   cd pdf-question-answering-backend

2. Set up a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`

3. Install dependencies:
   ```bash
   pip install -r requirements.txt

4. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload

  The backend will now be running at http://127.0.0.1:8000.

5. You can use the /upload endpoint to upload PDFs and interact with the WebSocket API at /ws/{document_id}.

### Frontend Setup

1. Clone the frontend repository:
   ```bash
   git clone https://github.com/yourusername/pdf-question-answering-frontend.git
   cd pdf-question-answering-frontend


2. Install the dependencies:
   ```bash
   npm install

3. Start the frontend development server:
   ```bash
   npm start

The frontend will be running at http://localhost:3000. Ensure that the backend is also running to interact with the app.

### Testing

1. Backend API tests are written using Pytest. To run the tests:
   ```bash
   pytest tests/

2. Frontend tests can be run using Jest:
   ```bash
   npm test

## File Upload and WebSocket Interaction
- <b> File Upload:</b> To upload a PDF, navigate to the file input and select a document. The file will be uploaded to the backend, and the extracted text content will be stored.
- <b> Ask Questions:</b> Once the file is uploaded, you can ask questions about the document in the input box. The backend will process the question and return an answer based on the document’s content.

## API Endpoints
### PDF Upload Endpoint

- <b> POST / upload </b>
    - Accepts a PDF file upload and processes it.
    - Responds with metadata of the uploaded document.
  
### WebSocket Question Answering Endpoint 
- <b> WebSocket /ws/{document_id} </b>
    - Allows users to send questions related to the uploaded PDF.
    - Responds in real-time with the generated answer from the document's content.

## Rate Limiting
The project uses rate limiting to ensure that users cannot overload the backend or WebSocket service. The rate limiting rules can be adjusted as needed to fit your use case.

## Contributions
Contributions are welcome! If you’d like to contribute to the project:
1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Make your changes and commit them (git commit -am 'Add new feature').
4. Push to the branch (git push origin feature-branch).
5. Create a new Pull Request.

## License
This project is licensed under the MIT License.

