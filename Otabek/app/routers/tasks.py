from fastapi import APIRouter, HTTPException
from typing import List


router = APIRouter()

# Временно хранилище
tasks = []

# Id задач
idd: int = 1



# Получение списка задач
@router.get('/')
def get_tasks() -> list[dict]:
    # Получаем список задач
    return tasks



# Добавление задачи
@router.post('/')
def create_task(title: str, description: str = '') -> dict:
    global idd

# def create_task(data: dict) -> dict:
    # Создание новой задачи
    # task = {
    #     'id': idd,
    #     'title': data['title'],
    #     'description': data['description'],
    #     'is_done': False
    # }

    task = {
        'id': idd,
        'title': title,
        'description': description,
        'is_done': False
    }

    tasks.append(task)
    idd += 1
    return task


# Поиск задачи
@router.get('/{task_id}')
def get_task_by_id(id: int) -> dict:
    for task in tasks: # tasks = [{'key': 'value'}, {'key': 'value'}]
        if task['id'] == id:
            return task
        
    raise HTTPException(status_code = 404, detail = 'Task not found!')


# Обноваление задачи
@router.put('/{task_id}')
def update_task(id: int, title: str = None, description: str = None, is_done: bool = None) -> dict:
    for task in tasks:
        if task['id'] == id:

            if title is not None:
               
                task['title'] = title
            if description is not None:
               
                task['description'] = description
            
            if is_done is not None:
                task['is_done'] = is_done

            return task
        
    raise HTTPException(status_code = 404, detail = 'Task not found!')


# Удаление задачи
@router.delete('/{task_id}')
def delete_task(id: int) -> dict:
    for task in tasks:
        if task['id'] == id:
            tasks.remove(task)

            return {'Status': 'Deleted!'}
    
    raise HTTPException(status_code = 404, detail = 'Task not found!')

