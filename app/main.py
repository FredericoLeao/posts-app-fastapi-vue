from fastapi import FastAPI, Depends
from app.schemas.post import PostInput, PostOutput
from app.db import get_session
from sqlmodel import Session
from app.services.post_service import PostService


app = FastAPI()

@app.get('/api/check')
def api_check():
    return 'ok'

@app.post('/api/post')
def post_create(post: PostInput, db: Session = Depends(get_session)) -> PostOutput:
    service = PostService(db)
    return service.create_or_update(post)
