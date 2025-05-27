from fastapi import Depends
from sqlmodel import Session, select
from fastapi.testclient import TestClient
from app.main import app
from app.db import get_session, engine
from app.models import PostRevision

client = TestClient(app)

def test_create_post():
    post_input = {
        "title": "Post de teste",
        "content": "Conteudo do post de teste"
    }
    response = client.post("/api/post/", json=post_input)

    assert response.status_code == 200
    assert response.json()['title'] == "Post de teste"
    post_id = response.json()['id']

    post_input_update = {
        "id": post_id,
        "content": "Alterando conteudo do post de teste, deve gerar uma revision",
    }
    response = client.patch("/api/post/", json=post_input_update)
    assert response.status_code == 200
    assert response.json()['id'] == post_id
    assert response.json()['title'] == "Post de teste"
    with Session(engine) as db:
        post_revision = db.exec(select(PostRevision).where(PostRevision.post_id == post_id))
        post_revision_result = post_revision.all()
    assert len(post_revision_result) >= 2
