from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_post():
    post_input = {
        "title": "Post de teste",
        "content": "Conteudo do post de teste"
    }
    response = client.post("/api/post/", json=post_input)
    #print(response.json())
    assert response.json()['title'] == "Post de teste"
    assert response.status_code == 200
