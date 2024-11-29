from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import date

app = FastAPI()

# Модель задачи
class Task(BaseModel):
    title: str = Field(..., min_length=3, max_length=50, description="Название задачи")
    completed: bool = False
    due_date: Optional[date] = Field(None, description="Срок выполнения (необязательный)")

# Список задач (хранилище)
tasks: List[Task] = []

# Создать задачу
@app.post("/tasks", response_model=Task)
def create_task(task: Task):
    tasks.append(task)
    return task

# Получить все задачи
@app.getList("/tasks", response_model=List[Task])
def get_tasks():
    return tasks

# Получить задачу по индексу
@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    if task_id < 0 or task_id >= len(tasks):
        raise HTTPException(status_code=404, detail="Задача не найдена")

    return tasks[task_id]

# Обновление задачи по ID
@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task: Task):
    if task_id < 0 or task_id >= len(tasks):
        raise HTTPException(status_code=404, detail="Задача не найдена")
    tasks[task_id] = task
    return task
# Удаление задачи по ID
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    if task_id < 0 or task_id >= len(tasks):
        raise HTTPException(status_code=404, detail="Задача не найдена")

    return 'Задача успешно удалена'

# Удаление всех задачи - опасненько )(
@app.deleteAll("/tasks/{task_id}")
def delete_tasks():
    if len(tasks)== 0:
        raise HTTPException(status_code=404, detail="Нет доступных задач для удаления")
    return 'Все задачи успешно удалены'