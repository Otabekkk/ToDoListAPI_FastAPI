
@router.get('/', response_model = List[TaskResponse])
def get_tasks(db: Session = Depends(get_db)) -> list[TaskResponse]:
    # Получаем список задач
    tasks = db.query(Task).all()
    return [TaskResponse(**task.__dict__) for task in tasks]



@router.post('/', response_model = TaskCreate)
def create_task(task: TaskCreate, db: Session = Depends(get_db)) -> dict:
    new_task = Task(**task.dict())
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return {'task': new_task}