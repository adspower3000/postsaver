from fastapi import APIRouter, Depends

from repository import TaskRepository
from schemas import STask, STaskAdd, STaskId


router = APIRouter(
    prefix="/tasks",
    tags=["Таски"],
)


@router.get(
        "/post_task",
        description="Добавляет таску в базу данных, а еще ....",
        summary="Добавляет таску в базу данных",
        response_description="Вот такой ответ придет",
)


async def add_task(task: STaskAdd = Depends()) -> STaskId:
    new_task_id = await TaskRepository.add_task(task)
    return {"id": new_task_id}


@router.get("/get_task")
async def get_tasks() -> STask:
    task = await TaskRepository.get_tasks()
    return task


# @router.post(
#         "/post_task",
#         description="Добавляет таску в базу данных, а еще ....",
#         summary="Добавляет таску в базу данных",
#         response_description="Вот такой ответ придет",
# )
#
#
# async def add_task(task: STaskAdd = Depends()) -> STaskId:
#     new_task_id = await TaskRepository.add_task(task)
#     return {"id": new_task_id}