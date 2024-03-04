from fastapi import Depends
from sqlalchemy import select, desc
from database import TaskOrm, new_session
from schemas import STaskAdd, STask


class TaskRepository:
    @classmethod
    async def add_task(cls, task: STaskAdd) -> int:
        async with new_session() as session:
            data = task.model_dump()
            new_task = TaskOrm(**data)

            session.add(new_task)
            await session.flush()
            await session.commit()
            return new_task.id

    @classmethod
    async def get_tasks(cls) -> STask:
        async with new_session() as session:
            query = select(TaskOrm).order_by(desc(TaskOrm.id))
            result = await session.execute(query)
            task_model = result.scalar()
            task = STask.model_validate(task_model)
            return task

    @classmethod
    async def get_code(cls, nickname: str) -> STask:
        async with new_session() as session:
            query = select(TaskOrm).filter_by(nickname=nickname).order_by(TaskOrm.id.desc()).limit(1)
            result = await session.execute(query)
            task_model = result.scalar()
            task = STask.model_validate(task_model)
            return task

    @classmethod
    async def find_by_id(cls, code_id: int):
        async with new_session() as session:
            query = select(TaskOrm).filter_by(id=code_id)
            result = await session.execute(query)
            task_model = result.scalar_one_or_none()
            task = STask.model_validate(task_model)
            return task

