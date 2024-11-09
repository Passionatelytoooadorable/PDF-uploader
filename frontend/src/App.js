// src/App.js
import React, { useState } from 'react';
import FileUpload from './components/FileUpload';
import QuestionAnswer from './components/QuestionAnswer';

const App = () => {
    const [documentData, setDocumentData] = useState(null);

    const handleUploadComplete = (data) => {
        setDocumentData(data); // Set the document data received from the backend
    };

    return (
        <div className="App">
            <h1>PDF Document Question Answering</h1>
            <FileUpload onUploadComplete={handleUploadComplete} />
            {documentData && (
                <QuestionAnswer documentId={documentData.id} />
            )}
        </div>
    );
};

export default App;
