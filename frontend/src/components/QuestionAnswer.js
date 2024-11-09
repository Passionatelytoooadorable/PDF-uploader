// src/components/QuestionAnswer.js
import React, { useState, useEffect } from 'react';

const QuestionAnswer = ({ documentId }) => {
    const [question, setQuestion] = useState("");
    const [answer, setAnswer] = useState(null);
    const [socket, setSocket] = useState(null);
    const [connected, setConnected] = useState(false);

    useEffect(() => {
        const ws = new WebSocket(`ws://127.0.0.1:8000/ws/${documentId}`);
        ws.onopen = () => setConnected(true);
        ws.onclose = () => setConnected(false);
        ws.onmessage = (event) => {
            const data = JSON.parse(event.data);
            setAnswer(data.answer || data.error);
        };
        setSocket(ws);

        return () => {
            ws.close();
        };
    }, [documentId]);

    const handleQuestionSend = () => {
        if (socket && question) {
            socket.send(question);
            setQuestion("");
        }
    };

    return (
        <div>
            <h3>Ask a question about the document:</h3>
            <input
                type="text"
                value={question}
                onChange={(e) => setQuestion(e.target.value)}
                placeholder="Type your question"
            />
            <button onClick={handleQuestionSend} disabled={!connected}>
                Send
            </button>
            <div>
                <h4>Answer:</h4>
                <p>{answer}</p>
            </div>
        </div>
    );
};

export default QuestionAnswer;
