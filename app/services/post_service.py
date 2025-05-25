from sqlmodel import Session
from app.models import Post
from app.schemas.post import PostInput, PostOutput
from fastapi.exceptions import HTTPException

class PostService:
    def __init__(self, db: Session):
        self.db = db

    def create_or_update(self, post_input: PostInput) -> PostOutput:
        ''' Cria ou atualiza Post '''
        if post_input.id:
            # TODO: adicionar condicional do user_id apos imp do login
            # para restringir e melhorar a segurança garantindo que só
            # o author do post pode modifica-lo
            db_post = self.db.get(Post, post_input.id)
        else:
            db_post = Post()
            db_post.user_id = 1 # hardcoded até imp o login

        if not db_post:
            raise HTTPException(status_code=404, detail="Post não encontrado")

        post_input_data = post_input.model_dump(exclude_unset=True)
        db_post.sqlmodel_update(post_input_data)

        # save (substituir por um repository)
        self.db.add(db_post)
        self.db.commit()
        self.db.refresh(db_post)

        # TODO: salvar content revision

        # Retornar um PostOuput (converte automaticamente conforme o type hint)
        return db_post
