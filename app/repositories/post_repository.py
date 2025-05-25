from sqlmodel import Session
from app.models import Post, PostRevision

class PostRepository:
    def __init__(self, db: Session):
        self.db = db

    def save(self, post: Post) -> Post:
        self.db.add(post)
        self.db.commit()
        self.db.refresh(post)
        return post

    def save_revision(self, post: Post) -> Post:
        post_revision = PostRevision()
        post_revision.post_id = post.id
        post_revision.content = post.content
        self.db.add(post_revision)
        self.db.commit()
        self.db.refresh(post_revision)
        return post

    def get(self, post_id) -> Post:
        return self.db.get(Post, post_id)
