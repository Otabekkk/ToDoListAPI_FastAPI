from pydantic import BaseModel
# from typing import Optional


class TaskBase(BaseModel):
    title: str | None = None
    description: str | None = None
    is_done: bool | None = False


class TaskCreate(TaskBase):
    pass


class TaskUpdate(TaskBase):
    title: str | None = None
    description: str | None = None
    is_done: bool | None = False


class TaskResponse(TaskBase):
    id: int

    class Config:
        orm_mode = True
