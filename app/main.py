from fastapi import FastAPI
from app.models import User

app = FastAPI()

@app.get('/api/check')
def api_check():
    return 'ok'

