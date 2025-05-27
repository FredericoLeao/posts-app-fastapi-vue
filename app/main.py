from fastapi import FastAPI, Depends
from app.schemas.post import PostInput, PostInputUpdate, PostOutput
from app.db import get_session
from sqlmodel import Session
from app.services.post_service import PostService
from app.repositories.post_repository import PostRepository

app = FastAPI()

def get_post_repository(db: Session = Depends(get_session)) -> PostRepository:
    return PostRepository(db)

@app.get('/api/check')
def api_check():
    return 'ok'

@app.post('/api/post')
def post_create(post: PostInput, repository = Depends(get_post_repository)) -> PostOutput:
    service = PostService(repository)
    return service.create_or_update(post)

@app.patch('/api/post')
def post_update(post: PostInputUpdate, repository = Depends(get_post_repository)) -> PostOutput:
    service = PostService(repository)
    return service.create_or_update(post)
