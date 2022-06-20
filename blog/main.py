from fastapi import FastAPI
from . import schemas
app = FastAPI()



@app.post('/blog')
def index(request: schemas.Blog):
    return request

