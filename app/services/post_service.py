from app.models import Post
from app.schemas.post import PostInput, PostOutput
from fastapi.exceptions import HTTPException
from app.repositories.post_repository import PostRepository


class PostService:
    def __init__(self, repository: PostRepository):
        self.repository = repository

    def create_or_update(self, post_input: PostInput) -> PostOutput:
        ''' Cria ou atualiza Post '''
        if post_input.id:
            # TODO: adicionar condicional do user_id apos impl. do login
            # para restringir e melhorar a segurança garantindo que só
            # o author do post possa modifica-lo
            db_post = self.repository.get(post_input.id)
        else:
            db_post = Post()
            db_post.user_id = 1 # hardcoded até imp o login

        if not db_post:
            raise HTTPException(status_code=404, detail="Post não encontrado")

        post_input_data = post_input.model_dump(exclude_unset=True)
        db_post.sqlmodel_update(post_input_data)

        # save
        self.repository.save(db_post)
        self.repository.save_revision(db_post)

        # Retornar um PostOuput (converte automaticamente conforme o type hint)
        return db_post
