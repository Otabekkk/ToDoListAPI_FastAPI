from fastapi import FastAPI
from app.routers import tasks
from app.database import engine, Base

app = FastAPI()
Base.metadata.create_all(bind = engine)

# Подключить маршруты
app.include_router(tasks.router, prefix = '/tasks', tags = ['Tasks'])



@app.get('/')
def index() -> dict:
    return {'answer': 'Hello World!'}
