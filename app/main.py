from fastapi import FastAPI
from app.routers import tasks
import uvicorn


app = FastAPI()


# Подключить маршруты
app.include_router(tasks.router, prefix = '/tasks', tags = ['Tasks'])



@app.get('/')
def index() -> dict:
    return {'answer': 'Hello World!'}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)