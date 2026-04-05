from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_compile():
    response = client.post("/compile", json={
        "files": [
            {"filename": "test.tex", "content": "\\documentclass{article}\\begin{document}Hello\\end{document}"}
        ]
    })
    assert response.status_code == 200
