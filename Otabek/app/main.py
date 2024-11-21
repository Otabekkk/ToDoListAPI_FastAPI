from fastapi import FastAPI
from app.routers import tasks


app = FastAPI()


# Подключить маршруты
app.include_router(tasks.router, prefix = '/tasks', tags = ['Tasks'])



@app.get('/')
def index() -> dict:
    return {'answer': 'Hello World!'}