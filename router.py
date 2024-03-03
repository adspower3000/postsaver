from fastapi import APIRouter, Depends

from repository import TaskRepository
from schemas import STask, STaskAdd, STaskId

router = APIRouter(
    prefix="/code",
    tags=["Ваши коды"],
)


@router.post(
        "/post_code",
        description="Добавляет код в базу данных, а еще ....",
        summary="Добавляет код в базу данных",
        response_description="Вот такой ответ придет",
)
async def add_task(task: STaskAdd) -> STaskId:
    new_task_id = await TaskRepository.add_task(task)
    return {"id": new_task_id}


@router.get("/get_last_code")
async def get_tasks() -> STask:
    task = await TaskRepository.get_tasks()
    return task


@router.get("/get_code_by_id/{code_id}")
async def get_tasks_by_id(code_id: int) -> STask:
    task = await TaskRepository.find_by_id(code_id)
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