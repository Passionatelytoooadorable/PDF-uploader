import pytest
from fastapi.testclient import TestClient
from main import app
import asyncio

client = TestClient(app)

@pytest.mark.asyncio
async def test_websocket_question_answer():
    with client.websocket_connect("/ws/1") as websocket:
        websocket.send_text("What is the topic?")
        response = websocket.receive_json()
        assert "answer" in response
