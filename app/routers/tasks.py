from fastapi import APIRouter, HTTPException, Depends
from app.schemas.task import TaskCreate, TaskResponse, TaskUpdate
from typing import List
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate, TaskResponse

router = APIRouter()


# # Временно хранилище
# tasks = []

# # Id задач
# idd: int = 1


# Получение списка задач
@router.get('/', response_model=List[TaskResponse])
def get_tasks(db: Session = Depends(get_db)) -> list[TaskResponse]:
    # Получаем список задач
    tasks = db.query(Task).all()
    return [TaskResponse(**task.__dict__) for task in tasks]


# Добавление задачи
@router.post('/', response_model=TaskCreate)
def create_task(task: TaskCreate, db: Session = Depends(get_db)) -> dict:
    new_task = Task(**task.dict())
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return {'task': new_task}


# def create_task(data: dict) -> dict:
# Создание новой задачи
# task = {
#     'id': idd,
#     'title': data['title'],
#     'description': data['description'],
#     'is_done': False
# }

# task = {
#     'id': idd,
#     **task.model_dump()
# }

# tasks.append(task)
# idd += 1
# return task


# Поиск задачи
@router.get('/{task_id}', response_model=TaskResponse)
def get_task_by_id(task_id: int, db: Session = Depends(get_db)) -> TaskResponse:
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail='Task not found!')
    return TaskResponse(**task.__dict__)
    # for task in tasks: # tasks = [{'key': 'value'}, {'key': 'value'}]
    #     if task['id'] == id:
    #         return task

    # raise HTTPException(status_code = 404, detail = 'Task not found!')


# Обновление задачи
@router.put('/{task_id}', response_model=TaskResponse)
def update_task(task_id: int, task_update: TaskUpdate, db: Session = Depends(get_db)) -> TaskResponse:
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail='Задача не найдена!')

    update_data = task_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(task, key, value)

    db.commit()
    db.refresh(task)
    return TaskResponse(**task.__dict__)


# Обноваление задачи
# @router.put('/{task_id}', response_model = TaskUpdate)
# def update_task(task_id: int, task_update: TaskUpdate, db: Session = Depends(get_db)) -> TaskResponse:
#   task = db.query(Task).filter(Task.id == task_id).first()
#  if not task:
#     raise HTTPException(status_code = 404, detail = 'Task not found!')
#
# update_data = task_update.model_dump(exclude_unset = True)

# for key, value in update_data.items():
# setattr(task, key, value)

#  db.commit()
#  db.refresh()

# return task

# for task in tasks:
#     if task['id'] == id:
#         update_data = task_update.model_dump(exclude_unset = True)

#         for key, value in update_data.items():
#             task[key] = value
# ------------------------------------------------------------------------------ #
# if title is not None:

#     task['title'] = title
# if description is not None:

#     task['description'] = description

# if is_done is not None:
#     task['is_done'] = is_done
# ------------------------------------------------------------------------------ #
# return task

# raise HTTPException(status_code = 404, detail = 'Task not found!')

# Удаление задачи
@router.delete('/{task_id}', response_model=TaskResponse)
def delete_task(task_id: int, db: Session = Depends(get_db)) -> TaskResponse:
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail='Task not found!')
    db.delete(task)
    db.commit()

    return task
    # for task in tasks:
    #     if task['id'] == id:
    #         tasks.remove(task)

    #         return {'Status': 'Deleted!'}

    # raise HTTPException(status_code = 404, detail = 'Task not found!')


# Удаление задачи Bayaman
@router.delete('/{task_id}')
def delete_task(task_id: int, db: Session = Depends(get_db)) -> TaskResponse:
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail='Task not found!')
    db.delete(task)
    db.commit()
    return task


# Удаление всех задачи Bayaman
@router.deleteAll('/}')
def delete_tasks(db: Session = Depends(get_db)) -> TaskResponse:
    tasks = db.query(Task).all()
    if not tasks:
        raise HTTPException(status_code=404, detail='Tasks not found!')
    db.delete(tasks)
    db.commit()
    return 'All deleted'

